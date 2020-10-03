from flask import Blueprint
from flask_restful import  Api



main_bp = Blueprint('main', __name__)
main_api = Api(main_bp)


class Main(Resource):
    def get(self):
        

        return {"0":"1"}


main_api.add_resource(Main, '/')
