from flask import Flask
from flask_restful import Api
from app.api_v1.orders.views import Orders, GetOneOrder
from instance.config import app_config



def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])
    app.config.from_pyfile('config.py')

    
    from .api_v1.orders import orders_bp as orders_blueprint
    api = Api(orders_blueprint)
    app.register_blueprint(orders_blueprint, url_prefix='/api/v1')

    api.add_resource(Orders, '/orders')
    api.add_resource(GetOneOrder, '/orders/<int:id>')
    



    return app