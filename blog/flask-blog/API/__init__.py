from API.user import user as userBlueprint
from API.port import port as portBlueprint
from API.test import test as testBlueprint
from API.arctype import arctype as arctypeBlueprint
from API.archive import archive as archiveBlueprint
from API.front import front as frontBlueprint
from API.comment import comment as commentBlueprint
from API.config import config as configBlueprint
from API.database import database as dbBlueprint
from API.login_log import login_log as logBlueprint
from API.auth import token_auth

@token_auth
def before_request():
    pass

# token_auth　视图
userBlueprint.before_request(before_request)
arctypeBlueprint.before_request(before_request)
archiveBlueprint.before_request(before_request)
commentBlueprint.before_request(before_request)
configBlueprint.before_request(before_request)
dbBlueprint.before_request(before_request)
logBlueprint.before_request(before_request)