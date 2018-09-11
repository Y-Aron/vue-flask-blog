
from flask import Blueprint, request, abort, jsonify, Response
from utils import logger
import random
from API.base import get_argument, respData
test = Blueprint('test',__name__, url_prefix='/api')

@test.route('/test', methods=['GET'])
def test_index():
   print(request.remote_addr)
   return 'get'

@test.route('/test', methods=['POST'])
def test_post():

   return 'post'

@test.route('/test', methods=['PUT'])
def test_put():

   return 'put'

@test.route('/test/<int:id>', methods=['DELETE'])
def test_del(id):

   return 'del'
