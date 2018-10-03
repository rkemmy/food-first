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

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401
       
        if MealItem().get_by_name(name):
            return {'message': f'meal with name {name} alredy exists'}, 400

        if not re.match('^[a-zA-Z 0-9]+$', name):
            return {'message': "Enter a valid food name"}, 400

        if not re.match('^[a-zA-Z0-9 ]+$', description):
            return {'message': "Enter a valid food description"}, 400

        if type(price) != int:
            return {'message': "Invalid price"}, 400


        mealitem = MealItem(name, description, price)

        mealitem.add()

        return {"message": "Meal successfully created"}


    def get(self):
        '''return a list of created mealitems'''

        meal_items = MealItem().get_all_meals()
        if meal_items:
            return {
                "food_items": [meal_item.serialize() for meal_item in meal_items]
            }, 200

        return {"message": "meal item not found"}

class SpecificMeal(Resource):

    @jwt_required
    def delete(self, id):
        ''' Method that deletes a specific order '''

        meal_item = MealItem().get_by_id(id)

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401

        if meal_item:
            meal_item.delete(id)
            return {"message": "meal deleted successfully"}

        return {"message": "Order not found"}