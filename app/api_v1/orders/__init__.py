from flask import Blueprint

from app.api_v1.orders.views import Orders

orders_bp = Blueprint('orders', __name__)