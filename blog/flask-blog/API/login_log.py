from flask import Blueprint, request
from API.base import respData, get_argument
from model.port import login_log_model

login_log = Blueprint('login_log', __name__, url_prefix='/api')



@login_log.route('/login_log/index', methods=['GET'])
def fetchLoginLog():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = login_log_model.fetchList(start, length)
    return respData(**ret)

@login_log.route('/login_log/index', methods=['DELETE'])
def removeLoginLog():
    pk = get_argument('id')
    ret = login_log_model.remove(pk)
    return respData(**ret)