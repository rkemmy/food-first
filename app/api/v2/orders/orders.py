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

        meal_item = MealItem().get_by_id(id)
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

    @jwt_required
    def put(self, id):
        ''' Method that updates a specific order '''
        
        order = Order().get_by_id(id)
        data = request.get_json(force=True)

        if not (get_jwt_identity()['is_admin']):
            return {'message':'You cannot access this route'}, 401

        elif data['status'].strip() == "":
            return ({'message': 'Enter valid status input'}, 400)

        else:
            if not isinstance(data['status'], str):
                return {'message': 'Input should be a string'}
        
        if order:
            order.status = data['status']
            return {"message":order.serialize()},201
        
        return {"Message":"Order not found"},404

    @jwt_required
    def delete(self, id):
        ''' Method that deletes a specific order '''

        order = Order().get_by_id(id)

        if order:
            order.delete(id)
            return {"message": "order deleted successfully"}

        return {"message": "Order not found"}

class UserHistory(Resource):
    @jwt_required
    def get(self, username):
        ''' Method to get all orders of a particular user '''
        user = User().get_user_by_username(username)
        

        order_items = Order().get_order_history(user)

        if order_items:
            return {
                "orders": [order_item.serialize() for order_item in order_items]
            }, 200

        return {"message": "User Not Found"}
