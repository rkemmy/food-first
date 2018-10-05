from flask import Flask, redirect
from flask_restful import Api
from datetime import timedelta
from flask_jwt_extended import JWTManager
from app.api.v1.views import Orders, GetOneOrder,AcceptOrder,DeclineOrder,CompleteOrder,Status
from instance.config import app_config
from app.api.v2.auth import Signup, Login
from app.api.v2.meals import Meals, SpecificMeal
from app.api.v2.orders import PostOrder, SpecificOrder, UserHistory

jwt = JWTManager()

def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1000)

    jwt.init_app(app)

    @app.route('/')
    def index():
        return redirect('https://app.swaggerhub.com/apis-docs/andela59/Food-First/1.0')

    from app.api.v2.auth import auth_blueprint as auth_bp
    auth = Api(auth_bp)
    app.register_blueprint(auth_bp, url_prefix='/api/v2/auth')

    from app.api.v2.meals import meal_blueprint as meal_bp
    meal = Api(meal_bp)
    app.register_blueprint(meal_bp, url_prefix='/api/v2')

    from app.api.v2.orders import orderly_blueprint as orderly_bp
    orderly = Api(orderly_bp)
    app.register_blueprint(orderly_bp, url_prefix='/api/v2')


    from .api.v1 import orders_bp as orders_blueprint
    api = Api(orders_blueprint)
    app.register_blueprint(orders_blueprint, url_prefix='/api/v1')
    # app.add_resource(Home, '/')
    auth.add_resource(Signup, '/signup')
    auth.add_resource(Login, '/login')
    api.add_resource(Orders, '/orders')
    orderly.add_resource(PostOrder, '/users/orders')
    orderly.add_resource(SpecificOrder, '/users/orders/<int:id>')
    orderly.add_resource(UserHistory, '/users/history')
    meal.add_resource(SpecificMeal, '/menu/<int:id>')
    meal.add_resource(Meals, '/menu')
    api.add_resource(GetOneOrder, '/orders/<int:id>')
    api.add_resource(AcceptOrder,'/orders/accept/<int:id>')
    api.add_resource(DeclineOrder,'/orders/decline/<int:id>')
    api.add_resource(CompleteOrder,'/orders/completeorder/<int:id>')
    api.add_resource(Status, '/orderss')


    return app