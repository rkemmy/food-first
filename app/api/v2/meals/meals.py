import re

from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import MealItem, User

class Meals(Resource):
    @jwt_required
    def post(self):

        ''' Method that creates a meal item '''
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        if not (get_jwt_identity()['is_admin']):
            return {'message':'You cannot access this route'}, 401
       
        if MealItem().get_meal_by_name(name):
            return {'message': f'meal with name {name} alredy exists'}, 400

        if not re.match('^[a-zA-Z 0-9]+$', name):
            return {'message': "Enter a valid food name"}, 400

        if not re.match('^[a-zA-Z0-9 ]+$', description):
            return {'message': "Enter a valid food description"}, 400

        if type(price) != int:
            return {'message': "Invalid price"}, 400


        mealitem = MealItem(name, description, price)

        mealitem.add()

        return {"message": "meal successfully created"}


    def get(self):
        '''return a list of created mealitems'''

        meal_items = MealItem().get_all_meals()
        return {
            "food_items": [meal_item.serialize() for meal_item in meal_items]
        }, 200

        return {"message": "meal item created"}