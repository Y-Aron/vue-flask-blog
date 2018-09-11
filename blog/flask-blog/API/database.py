from flask import Blueprint, request, send_file
from config import STATUS
from API.base import get_argument, respData
from model.port import database_model

database = Blueprint('database', __name__, url_prefix='/api')


@database.route('/database/index', methods=['GET'])
def fetchDataBases():
    ret = database_model.fetchData()
    return respData(**ret)

@database.route('/database/backup', methods=['POST'])
def dbBackup():
    table_list = get_argument('table_list')
    ret = database_model.dbBackup(table_list)
    return respData(**ret)

@database.route('/database/backup', methods=['GET'])
def fetchBackup():
    ret = database_model.fetchBackup()
    return respData(**ret)

@database.route('/database/backup/recovery/<timestamp>', methods=['PUT'])
def backupRecovery(timestamp):
    ret = database_model.dbRecovery(timestamp)
    return respData(**ret)

@database.route('/database/backup', methods=['DELETE'])
def removeBackup():
    timestamp = get_argument('id')
    ret = database_model.removeBackup(timestamp)
    return respData(**ret)