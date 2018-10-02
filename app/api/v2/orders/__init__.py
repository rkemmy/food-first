from flask import Blueprint

from .orders import PostOrder

post_order_blueprint = Blueprint('post_orders', __name__)