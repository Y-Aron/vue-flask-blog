from flask import Blueprint, request
from model.config import config_model
from API.base import respData, get_argument


config = Blueprint('config', __name__, url_prefix='/api')

@config.route('/config/index', methods=['GET'])
def fetchList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = config_model.fetchList(start, length)
    return respData(**ret)

@config.route('/config/index', methods=['DELETE'])
def removeConfig():
    uuid = get_argument('id', default=0)
    ret = config_model.remove(uuid)
    return respData(**ret)

@config.route('/config/<int:uuid>', methods=['GET'])
def fetchConfig(uuid):
    ret = config_model.fetchData(uuid)
    return respData(**ret)


def makeData():
    return dict(
        key = get_argument('key'),
        value = get_argument('value'),
        description = get_argument('description'),
        type = get_argument('type')
    )

@config.route('/config/<int:uuid>', methods=['PUT'])
def putConfig(uuid):
    data = makeData()
    ret = config_model.edit(uuid, data)
    return respData(**ret)


@config.route('/config', methods=['POST'])
def postConfig():
    data = makeData()
    ret = config_model.create(data)
    return respData(**ret)