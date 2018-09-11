from utils.crypto.RSA import Rsa
from config import BACKUP_PATH
from utils.logger import logger
from utils.captcha.VerifyCode import ImageCode
from utils.mysql import MySQL
import hashlib, os, time
from urllib import parse

# 百度ip定位
def IPLocation(ip:str):
    logger.debug(ip)
    import requests
    AK = 'wTr9iUUsqRAN4WtKi8gzomOfqTVE469E'

    SK = 'lWRLKBEfgmFtrglacDr2HjsmibQez1dZ'

    queryStr = '/location/ip?ip={ip}&ak={ak}&coor=BD09ll'.format(ip=ip, ak=AK)

    encodeStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodeStr + SK
    sn = hashlib.md5(parse.quote_plus(rawStr).encode('utf-8')).hexdigest()

    url = 'http://api.map.baidu.com{qs}&sn={sn}'.format(qs=queryStr, sn=sn)
    resp_data = dict(
        province = '',
        district = '',
        city = ''
    )
    logger.debug(url)

    try:
        ret = requests.get(url, timeout=5)
        json = ret.json()
    except Exception as e:
        logger.debug(e)
        return resp_data
    else:
        if json['status'] == 0:
            address_detail = json['content']['address_detail']
            resp_data['city'] = address_detail['city']
            resp_data['province'] = address_detail['province']
            resp_data['district'] = address_detail['district']
        return resp_data

# 创建 redis连接
def fetchRedis():
    import redis
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r

# 生成图形验证码
def gene_image_code():
    image_code = ImageCode()
    return image_code.gene_code()

# rsa 算法解密
def rsa_decrypt(encrypt_data):
    if not encrypt_data: return encrypt_data
    rsa = Rsa()
    ret = rsa.decrypt(encrypt_data)
    return ret

# rsa 算法签字验证
def rsa_verify(data, signature):
    if data is None or signature is None:
        return False
    rsa = Rsa()
    ret = rsa.verify(str(data), signature)
    return ret


# rsa 算法签字
def rsa_signature(data):
    if not data: return data
    str_data = str(data)
    rsa = Rsa()
    ret = rsa.signature(data=str_data)
    return ret

# rsa 算法加密
def rsa_encrypt(data):
    if not data: return data
    rsa = Rsa()
    encrypt_data = rsa.encrypt(data)
    return encrypt_data

# md5 加密
def md5_encrypt(data):
    if not data: return data
    md5 = hashlib.md5(data.encode(encoding='utf-8'))
    return md5.hexdigest()

# hash sha1 算法计算文件大小
def calc_sha1(steam):
    sha1 = hashlib.sha1()
    sha1.update(steam)
    return sha1.hexdigest()

# 获取指定目录下的所有文件名列表
def get_file_list(root_dir):
    file_list = []
    if not root_dir: return file_list
    for parent, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_name = os.path.join(parent, filename)
            file_list.append(file_name)
    return file_list

# 根据文件名 获取上传文件的绝对路径
def get_file_path(filename):
    from utils.file import UploadFile
    up = UploadFile()
    ret = up.get_file_path(filename)
    if ret['exists']:
        return ret['file_path']
    # return file_path

# 文件的上传与保存 返回文件的sha1()编码
def upload(file):
    if not file: return None
    from utils.file import UploadFile
    up = UploadFile(file)
    up.make_file()
    return up

# 获取 uuid节点的所有父节点对象 ~
def parents(array, uuid):
    if uuid == 0: return []
    ret = []
    copy_dict = dict()
    for vol in array:
        copy_dict[vol['id']] = vol

    ret.append(copy_dict[uuid])
    while uuid != 0:
        pid = copy_dict[uuid]['pid']
        if pid != 0:
            ret.append(copy_dict[pid])

        uuid = pid
    ret.reverse()
    return ret

# 生成子孙树
def make_tree(data, pk_name:str='id', p_name:str='pid', child_name:str='children'):

    lists, tree = [], {}

    parent_id = ''
    for vol in data:
        tree[vol[pk_name]] = vol

    root = None

    for vol in data:
        obj = vol
        if not obj[p_name]:
            root = tree[obj[pk_name]]
            lists.append(root)
            continue
        parent_id = obj[p_name]

        if child_name not in tree[parent_id]:
            tree[parent_id][child_name] = []
        tree[parent_id][child_name].append(tree[obj[pk_name]])
    return lists

# 获取无限级树
def getTree(arr, p_name:str='pid', c_name:str='value', t_name:str='text'):
    if not arr: return []
    tree = []
    def getList(pid=0, level=0):
        for row in arr:
            if row[p_name] == pid:
                row['level'] = level
                row[t_name] = '　　├ ' * row['level'] + row[t_name]
                tree.append(row)
                getList(row[c_name], level + 1)

    getList()
    return tree

# MySQL数据库备份
def backup(user:str, passwd:str, dbname:str, host:str='localhost',
           port:int=3306, table_list=None, ext='sql'):

    if table_list is None:
        table_list = []

    # 初始化备份文件路径
    DATETIME = time.strftime('%Y%m%d%H%M%S')
    TODAYBACKUPPATH = os.path.join(BACKUP_PATH, DATETIME)

    # 创建备份文件目录
    if not os.path.exists(TODAYBACKUPPATH):
        os.makedirs(TODAYBACKUPPATH)

    # 初始化备份文件 *.sql 路径
    sql_path = '{todaybackuppath}{sep}{dbname}.{ext}'.format(
        todaybackuppath = TODAYBACKUPPATH,
        sep = os.path.sep,
        dbname = dbname,
        ext = ext
    )

    # 初始化备份 shell 命令
    dumpcmd = 'mysqldump -h {host} -P {port} -u {user} -p{passwd} {dbname} {table_list} > {sql_path}'.format(
        port = port,
        host = host,
        user = user,
        passwd = passwd,
        dbname = dbname,
        sql_path = sql_path,
        table_list = ' '.join(table_list)
    )

    os.system(dumpcmd)

# MySQL数据库恢复
def recovery(user:str, passwd:str, dbname:str, sql_path:str,
             host:str='localhost',port:int=3306):

    # 初始化恢复 shell 命令
    cmd = 'mysql -h {host} -P {port} -u {user} -p{passwd} {dbname} < {sql_path}'.format(
        port = port,
        host = host,
        user = user,
        passwd = passwd,
        dbname = dbname,
        sql_path = sql_path,
    )
    os.system(cmd)
