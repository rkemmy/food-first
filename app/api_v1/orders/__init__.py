from flask import Blueprint

from .views import Orders

orders_bp = Blueprint('orders', __name__)