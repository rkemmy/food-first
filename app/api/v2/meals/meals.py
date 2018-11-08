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
        name = (data['name']).lower()
        description = data['description']
        price = data['price']
        img = data['img']

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401

        if data['name'].strip() == "" or data['description'].strip() == "" or data['img'].strip() == "":
            return ({'message': 'Input data not complete'}, 400)
        
        if MealItem().get_by_name(name):
            return {'message': f'meal with name {name} already exists'}, 400

        if not re.match('^[a-zA-Z ]+$', name):
            return {'message': "valid food name should contain alphabetic characters"}, 400

        if not re.match('^[a-zA-Z ]+$', description):
            return {'message': "valid description should contain alphabetic characters"}, 400

        if not isinstance(data['price'], int) or data['price'] <= 0:
            return {'message': 'Price must be an integer greter than zero'}, 400 

        mealitem = MealItem(name, description, price, img)

        mealitem.add()

        return {"message": "Meal successfully created"}, 201


    def get(self):
        '''return a list of created mealitems'''
        # q = request.args.get('q')
        meal_items = MealItem().get_all_meals()
        # meal_items = MealItem().search(q)

        if meal_items:
            return {
                "food_items": [meal_item.serialize() for meal_item in meal_items]
            }, 200

        return {"message": "meal item not found"}, 400

class SpecificMeal(Resource):

    @jwt_required
    def put(self, id):
        """Edit a meal item."""
        meal_item = MealItem().get_by_id(id)
        # print("<***>" * 30)
        print("MEAL item", meal_item.serialize())
        try:
            if meal_item:
                data = request.get_json()
                MealItem().update_meal(data['name'], id)
                meal_item.name= data['name']
                return {"message":meal_item.serialize()}, 200
                # meal_item.name = data["name"]
                # meal_item.price = data["price"]
                # meal_item.img = data["img"]
                # meal_item.description = data["description"]
                # meal_item.add()
                return {"message", "Meal item updated successfully"}, 200
            else:
                return {"message": "Meal item does not exist."}, 400
        except Exception as e:
            return {"message", str(e)}, 500


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