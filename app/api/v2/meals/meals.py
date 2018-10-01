from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from ..models import MealItem, User

class Meals(Resource):
    @jwt_required
    def post(self):
        ''' Method that creates a meal item '''
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        mealitem = MealItem(name, description, price)

        mealitem.add()

        return {"message": "meal item created"}