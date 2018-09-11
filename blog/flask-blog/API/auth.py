from flask import request, abort
from utils import fetchRedis, rsa_verify, logger
from model.user import auth_rule_model
import functools, ast

def auth(path:str, method:str, user_info:str):

    def verify(route_path:str):
        path_array = path.split('/')
        route_path_array = route_path.split('/')

        ret = True
        for pk, rk in zip(path_array, route_path_array):
            if pk != rk: ret = False
        return ret

    user_id = ast.literal_eval(user_info)['uid']
    error = 'id={id}的用户不拥有此权限~'.format(id=user_id)

    # 开始验证权限
    # 1. 根据user_info 的 user_id 查询用户组id
    # 2. 根据group_id method 从tb_auth_rule表中获取routes []
    routes = auth_rule_model.fetchRoutes(user_id, method)

    # 4. 匹配路由
    if routes is None: abort(403, error)
    # 4. 遍历路由列表进行匹配
    isOK = False
    for route in routes:
        if verify(route):
            isOK = True
            break
    if not isOK: abort(403, error)

def token_auth(func):
    @functools.wraps(func)
    def check(*args, **kwargs):
        method = request.method
        path = request.path
        token = request.headers.get('Authorization')
        if token:
            # token = token.split(' ')[1]
            # 获取redis
            redis = fetchRedis()
            # 将字符串转dict
            user_info = redis.get(token)

            if user_info is None: abort(401, 'token已过期~ 请重新登陆!')

            # token 验证成功 ~
            if  rsa_verify(user_info, token):
                # 0. method : GET -> OK, POST/PUT/DELETE -> 检查权限
                if method != 'GET':
                    # 验证权限
                    auth(path, method,user_info)
                # 进入路由
                return func(*args, **kwargs)
        abort(401, 'token 验证失败~')
    return check