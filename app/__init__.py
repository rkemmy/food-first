from flask import Flask
from flask_restful import Api
from app.api.v1.views import Orders, GetOneOrder,AcceptOrder,DeclineOrder,CompleteOrder,Status
from instance.config import app_config



def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])

    from .api.v1 import orders_bp as orders_blueprint
    api = Api(orders_blueprint)
    app.register_blueprint(orders_blueprint, url_prefix='/api/v1')

    api.add_resource(Orders, '/orders')
    api.add_resource(GetOneOrder, '/orders/<int:id>')
    api.add_resource(AcceptOrder,'/orders/accept/<int:id>')
    api.add_resource(DeclineOrder,'/orders/decline/<int:id>')
    api.add_resource(CompleteOrder,'/orders/completeorder/<int:id>')
    api.add_resource(Status, '/orderss')


    return app