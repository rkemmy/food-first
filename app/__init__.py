from flask import Flask
from flask_restful import Api
from app.api_v1.orders.views import Orders, GetOneOrder,AcceptOrder,ApprovedOrders,DeclineOrder,DeclinedOrders,PendingOrders,CompleteOrder,CompletedOrders
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
    api.add_resource(AcceptOrder,'/orders/accept/<int:id>')
    api.add_resource(ApprovedOrders,'/orders/approved')
    api.add_resource(DeclineOrder,'/orders/decline/<int:id>')
    api.add_resource(DeclinedOrders,'/orders/declined')
    api.add_resource(PendingOrders,'/orders/pending')
    api.add_resource(CompleteOrder,'/orders/completeorder/<int:id>')
    api.add_resource(CompletedOrders,'/orders/completed')




    return app