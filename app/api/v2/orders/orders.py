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

        meal_item = MealItem().get_by_name(name)
        print(meal_item)
        if not meal_item:
            return {"message": "food item not found"}, 404


        order = Order(username=current_user[0], title=meal_item.name, description=meal_item.description,
                      price=meal_item.price)
        order.add()

        return {"message": "order placed sucessfully"}, 201
    
    @jwt_required
    def get(self):

        ''' get all orders'''
        order_items = Order().get_all_orders()

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401

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

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401

        if order:
            return {"order": order.serialize()}, 200

        return {"message": "Order not found"}, 404

    @jwt_required
    def put(self, id):
        ''' Method that updates a specific order '''
        
        order = Order().get_by_id(id)
        data = request.get_json(force=True)

        user = get_jwt_identity()

        if not (user[1]):
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

        user = get_jwt_identity()

        if not (user[1]):
            return {'message':'You cannot access this route'}, 401

        if order:
            order.delete(id)
            return {"message": "order deleted successfully"}

        return {"message": "Order not found"}

class UserHistory(Resource):
    @jwt_required
    def get(self):
        ''' Method to get all orders of a particular user '''
        username = get_jwt_identity()[0]
        

        order_items = Order().get_order_history(username)

        if order_items:
            return {
                "username": username,
                "orders": [order_item.serialize() for order_item in order_items]
                
            }, 200

        return {"message": "User Not Found"}
