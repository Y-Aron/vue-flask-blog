import os, time, redis
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEB_VIEWS = 'VIEWS'
TOKEN_EXPIRE = 60 * 60

RSA_PRIVATE_KEY_PASSPHRASE = 'admin'

SESSION_TYPE = 'redis'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = False
SESSION_KEY_PREFIX = 'session'
SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')


DEBUG = True

# 数据库备份路径
BACKUP_PATH  = os.path.join(BASE_DIR, 'database','backup')


# pymysql
MySQL = dict(
    host='127.0.0.1', port=3306, user='youruser', passwd='yourpassword', db='blog', charset='utf8',
    read_timeout = 5, write_timeout = 10,
)

# DATABASE = {
#     'mysql': {
#         'dialect':'mysql',
#         'driver':'pymysql',
#         'username': 'root',
#         'password': 'admin',
#         'host': 'localhost',
#         'port': '3306',
#         'database': 'learn',
#         'coding': 'utf8'
#     }
# }

# # flask-SQLAlchemy 配置
# SQLALCHEMY_DATABASE_URI = u'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={coding}'.format(**DATABASE['mysql'])
#
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# # 如果设置为True SQLAlchemy将记录发送到stderr的所有语句，这对调试很有用。
# SQLALCHEMY_ECHO = False
# # 数据库池的大小。默认为引擎的默认值（通常为5）
# SQLALCHEMY_POOL_SIZE = 10
# # 指定池的连接超时（以秒为单位）
# SQLALCHEMY_POOL_TIMEOUT = 5
# # 控制池达到其最大大小后可以创建的连接数。当这些附加连接返回到池时，它们将被断开连接并被丢弃。
# SQLALCHEMY_MAX_OVERFLOW = 20

# 状态类
class STATUS(object):
    # API操作状态
    OK =                        0
    IMAGE_CODE_ERROR =          4000
    DB_ERR =                    -1
    DATA_EXISTS_ERR =           -1000
    DATA_NULL_ERR =             -2000
    DATA_MATCH_ERR =            -3000
    DATA_NOT_CHANGE_ERR =       -4000
    DATA_CREATE_ERR =           -5000
    DARA_DELETE_ERR =           -6000


    # OK = dict(code = 0,error = 'OK!')
    # IMAGE_CODE_ERROR = dict(code = 4000, error = '图片验证码错误!')
    # # 数据库操作状态
    # DB_ERR = dict(code = -1, error = '数据库操作失败!')
    # DATA_EXISTS_ERR = dict(code= -1000, error='数据已存在!')
    # DATA_NULL_ERR = dict(code = -2000, error = '查询数据不存在!')
    # DATA_MATCH_ERR = dict(code = -3000, error = '数据匹配错误!')
    # DATA_NOT_CHANGE_ERR = dict(code = -4000, error ='数据没有改变哦~')
    # DATA_CREATE_ERR = dict(code = -5000, error='数据创建失败!')
    # DARA_DELETE_ERR = dict(code = -6000, error='数据删除失败!')

