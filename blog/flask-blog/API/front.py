from flask import Blueprint
from model.archive import archive_model
from model.arctype import arctype_model
from model.comment import comment_model
from API.base import respData, get_argument, logger
from utils import fetchRedis
from config import WEB_VIEWS

front = Blueprint('/front', __name__, url_prefix='/api')

#　－－－－－－－－－－－－－－－－－－ front
@front.route('/archive/front/type_id/<int:tid>', methods=['GET'])
def fetchListByTid(tid):
    ret = archive_model.fetchDataByTid(tid)
    return respData(**ret)


@front.route('/archive/front/id/<int:uuid>', methods=['GET'])
def fetchDataById(uuid):
    redis = fetchRedis()
    redis.incr(WEB_VIEWS, 1)
    ret = archive_model.fetchDataById(uuid)
    return respData(**ret)

# ------------------------- front
@front.route('/arctype/front', methods=['GET'])
def fetchTreeList():
    ret = arctype_model.fetchTreeList()
    return respData(**ret)

@front.route('/arctype/front/id/<int:uuid>', methods=['GET'])
def fetchParents(uuid):
    ret = arctype_model.fetchParents(uuid)
    return respData(**ret)

@front.route('/arctype/front/type_id/<int:uuid>', methods=['GET'])
def fetchArctype(uuid):
    ret = arctype_model.fetchArctype(uuid)
    return respData(**ret)

@front.route('/archive/front/like/id/<int:uuid>', methods=['PUT'])
def refreshLike(uuid):
    ret = archive_model.refreshLike(uuid)
    return respData(**ret)

@front.route('/comment/front', methods=['POST'])
def postComment():
    data = dict(
        pid = get_argument('reply_id'),
        type = get_argument('reply_type'),
        username = get_argument('username', required=True),
        email = get_argument('email', required=True),
        content = get_argument('content', required=True)
    )
    ret = comment_model.create(data)
    return respData(**ret)

@front.route('/comment/front/treeList/<int:type_id>', methods=['GET'])
def fetchCommentTreeList(type_id):

    ret = comment_model.fetchTreeList(type_id)
    return respData(**ret)

@front.route('/front/hot', methods=['GET'])
def fetchHot():
    archive_ret = archive_model.fetchHotList()
    arctype_ret = arctype_model.fetchHotList()
    data = dict(
        hot_archive = archive_ret,
        hot_arctype = arctype_ret
    )
    return respData(data=data)