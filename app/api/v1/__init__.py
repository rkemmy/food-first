from flask import Blueprint

from app.api.v1.views import Orders

orders_bp = Blueprint('orders', __name__)