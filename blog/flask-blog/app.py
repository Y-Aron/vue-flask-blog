
from flask import Flask,Blueprint
from flask_session import Session
import config
import API

def add_routes(flask):
    for attr in dir(API):
        if attr.startswith('_'):
            continue

        val = getattr(API, attr)

        if isinstance(val, Blueprint):
            flask.register_blueprint(val)
    return flask

def before_first_request():
    print('before_first_request')

def before_request():
    print('before_request')

def after_request(params):
    print('...')
    return params

def create_app():
    flask = Flask(__name__)
    flask.config.from_object(config)
    flask = add_routes(flask)
    # flask.before_first_request(before_first_request)
    # flask.before_request(before_request)
    # flask.after_request(after_request)

    Session(flask)
    return flask

app = create_app()
