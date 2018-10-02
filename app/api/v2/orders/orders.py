from flask import Flask, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User, Order, MealItem


class PostOrder(Resource):
    @jwt_required
    def post(self):
        '''post an order by the user'''

        data = request.get_json()

        
        current_user = get_jwt_identity()
        name = data['name']

        meal_item = MealItem().get_meal_by_name(name)

        if not meal_item:
            return {"message": "food item not found"}, 404


        order = Order(current_user, meal_item.name, meal_item.description,
                      meal_item.price)

        order.add()

        return {"meassage": "order placed sucessfully"}, 201