from flask import Blueprint

from .meals import Meals, SpecificMeal

meal_blueprint = Blueprint('meals', __name__)