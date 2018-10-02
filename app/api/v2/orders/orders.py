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


        order = Order(username=current_user['username'], title=meal_item.name, description=meal_item.description,
                      price=meal_item.price)
        order.add()

        return {"message": "order placed sucessfully"}, 201
    
    @jwt_required
    def get(self):

        ''' get all orders'''
        order_items = Order().get_all_orders()
        if order_items:
            return {
                "orders": [order_item.serialize() for order_item in order_items]
            }, 200
        return {"message": "No orders found"}

class SpecificOrder(Resource):
    @jwt_required
    def get(self, id):
        '''get a specific order by id'''

        order = Order().get_by_id(id)

        if order:
            return {"order": order.serialize()}, 200

        return {"message": "Order not found"}, 404
