from flask_restful import Resource, reqparse

from flask import request
from app.models import orders, Order



class Orders(Resource):

    def get(self):
        ''' Method that get all orders '''
        if len(orders) == 0:
            return {"message":"empty list"}, 200
        else:
            return {"Orders": [order.serialize() for order in orders]}, 200

    def post(self):
        ''' Method that posts an order '''
        data = request.get_json(force=True)
        if data['name'].strip() == "" or data['description'].strip() == "":
            return ({'message': 'Input data not complete'}, 400)

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

        if name in orders:
            return {'message': 'Order already exists'}
        
        orders.append(new_order)

        return {"message":"order successfully created",
                "order":new_order.serialize()
                },201

class GetOneOrder(Resource):
    
    def get(self, id):
        ''' Method that gets a spedific order by id '''
        
        order  = Order().get_by_id(id)
        if not order:
            return {"Message":"Order not found"},200

        return {"Orders": order.serialize()},200
        

    def put(self, id):
        ''' Method that updates a specific order '''
        
        order = Order().get_by_id(id)
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
    
    def get_declined_orders(self):
        declinedorders = []
        for order in orders:
            if order.status == "declined":
                declinedorders.append(order)
                return {"message":[order.serialize() for order in declinedorders]},200

        return {"message":"there are no declined orders"},200

    def get_pending_orders(self):
        pendingorders = []
        for order in orders:
            if order.status == "pending":
                pendingorders.append(order)
            return {"pending orders":[order.serialize() for order in pendingorders]}

        return {"message":"there are no declined orders"},200

class DeclineOrder(Resource):

    def put(self,id):

        order = Order().get_by_id(id)
        if order:
            if order.status != "pending" and order.status == "declined":
                return {"message":"order already {}".format(order.status)}
            
            order.status = "declined"
            return {"message":"yeah,the order declined successfully"}
        
        return {"message":"Damn!Your order was not found"}


class CompleteOrder(Resource):
    def put(self,id):
        order = Order().get_by_id(id)
        if order:
            if order.status != "approved":
                return {"message":"The order is already {}".format(order.status)}
            if order.status == "approved":
                order.status = "completed"
                return {"message":"Order has beeen completed and will be delivered"}
        return {"message":"order not found"}

#TODO 
#create a class for returning a list of orders depending on status

