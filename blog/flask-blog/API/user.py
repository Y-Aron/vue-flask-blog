from flask import Blueprint, request
from API.base import respData, get_argument
from model.user import user_model, auth_group_model, auth_rule_model
from utils import upload, logger

user = Blueprint('user', __name__, url_prefix='/api')


@user.route('/user/option', methods=['GET'])
def fetchOption():
    ret = user_model.fetchOption()
    return respData(**ret)

@user.route('/user/index', methods=['GET'])
def fetchList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)

    ret = user_model.fetchList(start, length)
    return respData(**ret)

@user.route('/user/<int:uuid>', methods=['GET'])
def fetchData(uuid):
    ret = user_model.fetchData(uuid)
    return respData(**ret)


@user.route('/user/index', methods=['DELETE'])
def remove():
    uuid = get_argument('id')
    ret = user_model.remove(uuid)
    return respData(**ret)


# edit page => put
@user.route('/user/<int:uuid>',methods=['PUT'])
def putUser(uuid):
    user_data = dict(
        nickname = get_argument('nickname'),
        email = get_argument('email'),
        mobile = get_argument('mobile'),
        status = get_argument('status')
    )
    up = None

    avatar = request.files.get('avatar') or get_argument('avatar')
    if not isinstance(avatar, str):
        up = upload(avatar)
    if up: avatar = up.file_name
    user_info_data = dict(
        avatar = avatar,
        sex = get_argument('sex'),
        qq = get_argument('qq'),
        birthday = get_argument('birthday'),
        info = get_argument('info')
    )

    ret = user_model.edit(user_data, user_info_data, uuid, up)
    return respData(**ret)

def makeData() -> dict:
    data = dict(
        username=get_argument('username', required=True),
        password=get_argument('password', required=True),
        nickname=get_argument('nickname'),
        email=get_argument('email'),
        mobile=get_argument('mobile'),
        status=get_argument('status'),
    )
    return data

# edit page => post
@user.route('/user', methods=['POST'])
def postUser():
    register_ip = request.remote_addr
    data = makeData()
    data['register_ip'] = register_ip
    ret = user_model.create(data)
    return respData(**ret)


# ------------------------------------  auth_group
@user.route('/user/group/index', methods=['GET'])
def fetchGroupList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = auth_group_model.fetchList(start, length)
    return respData(**ret)

@user.route('/user/group/index', methods=['DELETE'])
def removeGroup():
    uuid = get_argument('id')
    ret = auth_group_model.remove(uuid)
    return respData(**ret)

@user.route('/user/group/<int:uuid>', methods=['GET'])
def fetchGroup(uuid):
    ret = auth_group_model.fetchData(uuid)
    return respData(**ret)


def makeGroupData():
    data = dict(
        description = get_argument('description'),
        level = get_argument('level'),
        module = get_argument('module', required=True),
        name = get_argument('name', required=True),
        rule_array = get_argument('rule_array', required=True)
    )
    return data

@user.route('/user/group', methods=['POST'])
def postGroup():
    data = makeGroupData()

    ret = auth_group_model.create(data)
    return respData(**ret)

@user.route('/user/group/<int:uuid>', methods=['PUT'])
def putGroup(uuid):
    data = makeGroupData()
    ret = auth_group_model.edit(data, uuid)
    return respData(**ret)

@user.route('/user/rules', methods=['GET'])
def fetchRules():
    ret = auth_rule_model.fetchRules()
    return respData(**ret)


# --------------------------  auth_rule

@user.route('/user/group/rule/index', methods=['GET'])
def fetchRuleList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = auth_rule_model.fetchList(start, length)

    return respData(**ret)

@user.route('/user/group/rule/index', methods=['DELETE'])
def removeRule():
    uuid = get_argument('id')
    ret = auth_rule_model.remove(uuid)
    return respData(**ret)

@user.route('/user/group/rule/options', methods=['GET'])
def fetchRuleOptions():
    ret = auth_rule_model.fetchOptions()
    return respData(**ret)

def makeRuleData():
    data = dict(
        method = get_argument('method'),
        name = get_argument('name', required=True),
        pid = get_argument('pid'),
        route = get_argument('route', required=True),
        status = get_argument('status'),
        type = get_argument('type', required=True),
        sorts = get_argument('sorts')
    )
    return data

@user.route('/user/group/rule', methods=['POST'])
def postRule():
    data = makeRuleData()
    ret = auth_rule_model.create(data)
    return respData(**ret)

@user.route('/user/group/rule/<int:uuid>', methods=['PUT'])
def putRule(uuid):
    data = makeRuleData()
    ret = auth_rule_model.edit(data, uuid)
    return respData(**ret)

@user.route('/user/group/rule/<int:uuid>', methods=['GET'])
def fetchRule(uuid):
    ret = auth_rule_model.fetchData(uuid)
    return respData(**ret)\



@user.route('/user/auth/<int:uuid>', methods=['GET'])
def fetchUserAuth(uuid):
    ret = auth_group_model.fetchUserAuth(uuid)
    return respData(**ret)

@user.route('/user/auth', methods=['GET'])
def fetchGroups():
    ret = auth_group_model.fetchGroup()
    return respData(**ret)

@user.route('/user/auth', methods=['POST'])
def postUserAuth():
    uuid = get_argument('uid')
    auth_group = get_argument('group_array')
    ret = auth_group_model.editAuth(uuid, auth_group)
    return respData(**ret)