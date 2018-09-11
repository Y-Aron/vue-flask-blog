
from flask import Blueprint, request
from API.base import get_argument, respData, logger
from model.comment import comment_model

comment = Blueprint('comment', __name__, url_prefix='/api')


@comment.route('/comment/archive/index', methods=['GET'])
def fetchList():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = comment_model.fetchList(start, length, guestbook = False)
    return respData(**ret)

@comment.route('/comment/guestBook/index', methods=['GET'])
def fetchGuestBook():
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    ret = comment_model.fetchList(start, length, guestbook = True)
    return respData(**ret)

@comment.route('/comment/<int:uuid>', methods=['GET'])
def fetchComment(uuid):
    ret = comment_model.fetchData(uuid)
    return respData(**ret)

@comment.route('/comment/archive/index', methods=['DELETE'])
def removeArchiveComment():
    uuid = get_argument('id')
    ret = comment_model.remove(uuid)
    return respData(**ret)

@comment.route('/comment/guestBook/index', methods=['DELETE'])
def removeGuestBookComment():
    uuid = get_argument('id')
    ret = comment_model.remove(uuid)
    return respData(**ret)

@comment.route('/comment', methods=['POST'])
def postComment():
    postData = dict(
        pid=get_argument('reply_id'),
        type=get_argument('reply_type'),
        username=get_argument('reply_username'),
        content=get_argument('reply_content')
    )

    putData = dict(
        id = get_argument('id'),
        status = get_argument('status'),
        content = get_argument('content')
    )
    ret = comment_model.create(postData, putData,isAdmin=True)
    return respData(**ret)

@comment.route('/comment/refstate', methods=['PUT'])
def refStatus():
    status = get_argument('status')
    uuid = get_argument('id')
    ret = comment_model.editStatus(uuid, status)
    return respData(**ret)