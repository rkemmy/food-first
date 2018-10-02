from flask import Blueprint

from .meals import Meals

meal_blueprint = Blueprint('meals', __name__)