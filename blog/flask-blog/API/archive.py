from flask import Blueprint, request
from API.base import get_argument, respData
from utils import upload, logger
from model.archive import archive_model

archive = Blueprint('archive', __name__, url_prefix='/api')

# index page => get data list
@archive.route('/archive/index', methods=['GET'])
def index():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = archive_model.fetchList(start, length)
    return respData(**ret)

# index page => delete data by id
@archive.route('/archive/index', methods=['DELETE'])
def remove():
    uuid = get_argument('id')
    ret = archive_model.remove(uuid)
    return respData(**ret)

# edit page => make post/put data
def makeData():
    up = None
    litpic = request.files.get('litpic') or get_argument('litpic')
    if not isinstance(litpic, str):
        up = upload(litpic)
    if up: litpic = up.file_name

    type_id = get_argument('type_id', type=int, required=True)
    data = dict(
        type_id = type_id,
        uid = get_argument('uid', type=int, required=True),
        title = get_argument('title', required=True),
        flag = get_argument('flag'),
        litpic = litpic,
        content = get_argument('content'),
        jumplink = '/detail/{}'.format(type_id),
        keywords = get_argument('keywords'),
        description = get_argument('description', required=True)
    )
    return data, up

# edit page post
@archive.route('/archive', methods=['POST'])
def post():
    post_data, up = makeData()
    ret = archive_model.create(data=post_data, up=up)
    return respData(**ret)

# edit page put
@archive.route('/archive', methods=['PUT'])
def put():
    data, up = makeData()
    uuid = get_argument('id', type=int)
    ret = archive_model.edit(data, up, uuid)
    return respData(**ret)

# edit page get
@archive.route('/archive/<int:uuid>', methods=['GET'])
def fetchData(uuid):
    ret = archive_model.fetchData(uuid)
    return respData(**ret)