
from flask import Blueprint, make_response, session, send_file, request
from utils import gene_image_code
from utils import logger, get_file_path, upload, fetchRedis, rsa_verify, rsa_signature, IPLocation
from API.base import respData, get_argument
from config import STATUS, WEB_VIEWS, TOKEN_EXPIRE
from model.user import user_model
from model.port import login_log_model, admin_model, database_model
from model.config import config_model
from model.comment import comment_model
import time, uuid, ast
from API.auth import token_auth

port = Blueprint('port', __name__, url_prefix='/api')


def create_login_log(user, ip, location):

    if isinstance(user, str):
        user = ast.literal_eval(user)

    data = dict(
        uid = user['uid'],
        ip = ip,
        country = '中国',
        province = location['province'],
        city = location['city'],
        district = location['district'],
    )
    login_log_model.create(data)

@port.route('/logout', methods=['PUT'])
def logout():
    token = request.headers.get('Authorization')
    redis = fetchRedis()
    redis.delete(token)
    session.clear()
    return respData(STATUS.OK)


@port.route('/login', methods=['POST'])
def login():
    token = request.headers.get('Authorization')
    username = get_argument('username', decrypt=True)
    password = get_argument('password', decrypt=True)
    real_ip = request.headers['X-Forwarded-For']
    if len(real_ip.split(',')) > 1:
        ip = real_ip.split(",")[1]
    else:
        ip = real_ip

    location = IPLocation(ip)
    redis = fetchRedis()
    if token:
        # 读取  redis: token -> { id, [nickname]}
        user_info = redis.get(token)
        if rsa_verify(user_info, token):
            # 验证 token 成功直接登陆
            create_login_log(user_info, ip, location)
            return respData(data=eval(user_info))

    # token 验证失败
    ret = user_model.login(username, password)

    if ret['code'] == STATUS.OK:
        create_login_log(ret['data'], ip, location)
        # 根据 { id, [nickname], uuid:time.time()} 使用rsa签字生成token
        # 生成动态 token
        key = uuid.uuid4().hex
        ret['data'][key] = time.time()
        token = rsa_signature(ret['data'])

        # key:token / value: { id, [nickname], uuid=time.time()}
        redis.set(token, ret['data'], ex=TOKEN_EXPIRE)

        # token 写入响应
        ret['data']['token'] = token

    return respData(**ret)

@port.route('/image_code',methods=['GET'])
def make_image_code():
    image, code = gene_image_code()
    resp = make_response(image)
    resp.mimetype = 'image/png'
    session['image_code'] = code
    return resp

@port.route('/image_code/validation', methods=['POST'])
def validationCode():
    # token 存在 无需验证验证码
    token = request.headers.get('Authorization')
    if token:
        return respData(STATUS.OK)

    image_code = get_argument('image_code')
    real_image_code = session.get('image_code')
    session.pop('image_code', None)
    if not real_image_code or not image_code:
        return respData(STATUS.IMAGE_CODE_ERROR, error='图片验证失败~')

    if real_image_code.lower() != image_code.lower():
        return respData(STATUS.IMAGE_CODE_ERROR, error='图片验证失败~')

    return respData(STATUS.OK)

@port.route('/download/<filename>', methods=['GET'])
def download(filename):
    file_path = get_file_path(filename)
    if file_path:
        resp = make_response(send_file(file_path))
        return resp
    return respData(STATUS.DATA_NULL_ERR, error='请求资源不存在~')


@port.route('/upload', methods=['POST'])
def upload_file():
    file =  request.files.get('filename')
    up = upload(file)
    if not up is None:
        up.save()
        url = '/api/download/' + up.file_name
        return respData(error='文件上传成功~', data=url)
    return respData(STATUS.DATA_CREATE_ERR, data='文件上传失败~')


@token_auth
@port.route('/admin', methods=['GET'])
def init_index():
    ret = admin_model.fetchData()
    return respData(**ret)

@port.route('/config/web_config', methods=['GET'])
def fetchWebConfig():
    data = config_model.fetchConfig(type='web')
    comment_total = comment_model.fetchCount()
    redis = fetchRedis()
    views = redis.get(WEB_VIEWS)
    data['web_views'] = views
    data['comments'] = comment_total
    return respData(data=data)


@port.route('/database/backup/download/<timestamp>', methods=['GET'])
def fetchBackupDownload(timestamp):
    file_path, file_name = database_model.fetchBackupFile(timestamp)
    if file_path:
        resp = send_file(file_path)
        resp.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
        return resp
    return respData(STATUS.DATA_NULL_ERR, error='备份文件不存在哦~')