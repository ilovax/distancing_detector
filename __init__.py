from flask import Flask
from flask_restful import Resource, Api

from .main import main_bp


class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    api.add_resource(Ping, '/ping')
    app.register_blueprint(main_bp, url_prefix='/')

    return app
