from flask import Blueprint, request
from model.arctype import arctype_mod_model, arctype_model
from API.base import respData, get_argument
from API.auth import token_auth
from utils import upload, logger

arctype = Blueprint('arctype', __name__, url_prefix='/api')


def makeModelData():
    data = dict(
        name = get_argument('name', required=True),
        operation = get_argument('operation', required=True),
        sorts = get_argument('sorts', type=int),
        status = get_argument('status', type=int)
    )
    return data

# index => list page get
@arctype.route('/arctype/model/index', methods=['GET'])
def fetchModelList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    ret = arctype_mod_model.fetchList(start, length)
    return respData(**ret)

# edit page => get
@arctype.route('/arctype/model/<int:mid>', methods=['GET'])
def fetchModel(mid):
    ret = arctype_mod_model.fetchData(mid)
    return respData(**ret)

# edit page => get options
@arctype.route('/arctype/model/option', methods=['GET'])
def fetchModelOptions():
    ret = arctype_mod_model.fetchOptions()
    return respData(**ret)

# edit page => put
@arctype.route('/arctype/model/<int:mid>',methods=['PUT'])
def putModel(mid):
    data = makeModelData()
    ret = arctype_mod_model.edit(data, mid)
    return respData(**ret)

# edit page => post
@arctype.route('/arctype/model', methods=['POST'])
def postModel():
    data = makeModelData()
    ret = arctype_mod_model.create(data)
    return respData(**ret)

# index => list page delete
@arctype.route('/arctype/model/index', methods=['DELETE'])
def removeModel():
    pk = get_argument('id')
    ret = arctype_mod_model.remove(pk)
    return respData(**ret)



# ------------------------ arctype route
# index page => get list
@arctype.route('/arctype/index', methods=['GET'])
def index():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = arctype_model.fetchList(start, length)
    return respData(**ret)

# index page => delete data
@arctype.route('/arctype/index', methods=['DELETE'])
def remove():
    uuid = get_argument('id', default=0)
    logger.debug(uuid)
    ret = arctype_model.remove(uuid)
    return respData(**ret)

# edit page => get data options
@arctype.route('/arctype/option', methods=['GET'])
def fetchOptions():
    ret = arctype_model.fetchOptions()
    return respData(**ret)

# edit page => get data by uuid
@arctype.route('/arctype/<int:uuid>', methods=['GET'])
def fetchData(uuid):
    ret = arctype_model.fetchData(uuid)
    logger.debug(ret)
    return respData(**ret)

# make post/ put data
def makeData():
    dirs = get_argument('dirs', required=True)
    up = None
    litpic = request.files.get('litpic') or get_argument('litpic')
    if not isinstance(litpic, str):
        up = upload(litpic)
    if up: litpic = up.file_name

    post_data = dict(
        id = get_argument('id', type=int),
        pid = get_argument('pid', type=int),
        model_id = get_argument('model_id', type=int),
        typename = get_argument('typename', required=True),
        jumplink='/category/' + dirs,
        dirs = dirs,
        litpic = litpic,
        desctiption = get_argument('description'),
        sorts = get_argument('sorts'),
        keywords = get_argument('keywords'),
        status = get_argument('status'),
        icon=get_argument('icon') or '<i class="fa fa-circle-o"></i>'
    )

    return post_data, up

# edit page => post data
@arctype.route('/arctype', methods=['POST'])
def post():
    post_data, up = makeData()

    ret = arctype_model.create(post_data, up)
    return respData(**ret)

# edit page => put data
@arctype.route('/arctype', methods=['PUT'])
def put():
    data, up = makeData()
    ret = arctype_model.edit(data, up)
    return respData(**ret)
