from flask import jsonify, request, abort, make_response, Blueprint, Response
from utils import logger, rsa_decrypt, fetchRedis, rsa_verify
from config import STATUS

def respData(code:int=STATUS.OK, error:str=None, data=None):
    resp = dict(
        code=code,
        error=error,
        data=data
    )
    return jsonify(resp)



def get_argument(key:str, type=None, default='', decrypt:bool=False, required=False, error:str=None):
    value = None

    if request.json:
        value = request.json.get(key)
    else:
        value = request.form.get(key)

    error = error or 'argument ({key}) is not exists !'.format(key=key)

    # key不存在
    if value is None: abort(400, error)

    # 验证是否存在 str:'' 400, int:0 正常
    if not value and required:

        if isinstance(value, str):
            abort(400, error)
        if isinstance(value, int):
            return value

    # 数据是否解密
    if decrypt: value = rsa_decrypt(value)

    # 数据转型
    if type: value = type(value)

    return value










