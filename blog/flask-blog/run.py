from gevent import monkey
from gevent.pywsgi import WSGIServer
from app import app
from utils import logger

monkey.patch_all()

def run(port:int=80, host:str='127.0.0.1'):
    http_server = WSGIServer((host, port), app)
    logger.info('server is started at http://{host}:{port}'.format(host=host, port=port))
    http_server.serve_forever()

if __name__ == '__main__':

    run(port=8888)