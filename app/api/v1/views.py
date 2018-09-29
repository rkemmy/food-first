import re

from flask_restful import Resource, reqparse
from flask import request

from .models import orders, Order



class Orders(Resource):

    def get(self):
        ''' Method that gets all orders '''
        if len(orders) == 0:
            return {"message":"empty list"}, 200
        else:
            return {"Orders": [order.serialize() for order in orders]}, 200

    def post(self):
        ''' Method that posts an order '''
        
        data = request.get_json(force=True)

        if data['name'].strip() == "" or data['description'].strip() == "":
            return ({'message': 'Input data not complete'}, 400)

        # elif re.match(r'!@#$%^&*(){}[]/<>:;\|,.', data):
        #     return {'message': 'get serious'}

        elif not isinstance(data['name'], str) or not isinstance(data['description'], str):
            return {'message': 'Input should be a string'}
        
        else:
            if not isinstance(data['price'], int):
                return {'message': 'Input integer'}

    

        name = data['name']
        description = data['description']
        price = data['price'] 
        status = data['status']
        
        new_order = Order(name, description, price, status)
        
        for item in orders:
            if item.name == name:
                return {'message': 'Order already exists'}, 400
            else:
                break
        orders.append(new_order)

        return {"message":"order successfully created",
                "order":new_order.serialize()
                },201

class GetOneOrder(Resource):
    
    def get(self, id):
        ''' Method that gets a specific order by id '''
        
        order  = Order().get_by_id(id)
        if not order:
            return {"Message":"Order not found"},200

        return {"Orders": order.serialize()},200
        

    def put(self, id):
        ''' Method that updates a specific order '''
        
        order = Order().get_by_id(id)
        data = request.get_json(force=True)
        if data['name'].strip() == "" or data['description'].strip() == "":
            return ({'message': 'Input data not complete'}, 400)

        elif not isinstance(data['name'], str) or not isinstance(data['description'], str):
            return {'message': 'Input should be a string'}
        
        else:
            if not isinstance(data['price'], int):
                return {'message': 'Input integer'}
        if order:
            data = request.get_json()
            order.name= data['name']
            order.description = data['description']
            order.price = data['price']
            order.status = data['status']
            return {"message":order.serialize()},201
        
        return {"Message":"Order not found"},404


    def delete(self, id):
        ''' Method that deletes a specific id '''
        order  = Order().get_by_id(id)
        if not order:
            return {"Message":"Order not found"},404

        orders.remove(order)
        return {"message":"order deleted successfully"}, 200
class AcceptOrder(Resource):
    
    def put(self,id):
        order  = Order().get_by_id(id)
        if order:
            if order.status !="pending":
                return {"message":"order has already been {}".format(order.status)}
            
            order.status = "approved"
            return {"message":"keep tight,your order has been approved!!"}
        
        return {"message":"uhh,we seem not to find any orders"}

class Status(Resource):
    
    def get_args(self, querystrings):
        parser = reqparse.RequestParser()
        for query in querystrings:
            parser.add_argument(query, type=str)
        return parser.parse_args()        
    
    def get(self):
        norder = Order().get_by_id(id)
        args = self.get_args(['status', 'approved'])
        norder = self.get_args(['name', 'name'])
        return {'order': [norder.serialize() for norder in orders if norder.status == 'pending'], 'status': args['status']}, 200
    

#TODO 
#create a class for returning a list of orders depending on status

