from flask_restful import Resource
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
        if not data:
            return ({'message': 'No input data provided'}, 400)

        name = data['name']
        description = data['description']
        price = data['price'] 
        
        new_order = Order(name, description, price)

        if name in orders:
            return {'message': 'Order already exists'}
        
        orders.append(new_order)

        return {"message":"order successfully created",
                "order":new_order.serialize()
                },201

    # def delete(self):
    #     all_orders = Order.get_all()
    #     return all_orders
    #      if orders.remove(all_orders):
    #          return {'message': 'all orders deleted'}       


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

class ApprovedOrders(Resource):

    def get(self):
        approvedorders = []
        for order in orders:
            if order.status == "approved":
                approvedorders.append(order)
                return {"message":[order.serialize() for order in approvedorders]},200

        return {"message":"unfortunately there are no approved orders"},200


class DeclineOrder(Resource):

    def put(self,id):

        order = Order().get_by_id(id)
        if order:
            if order.status != "pending" and order.status == "declined":
                return {"message":"order already {}".format(order.status)}
            
            order.status = "declined"
            return {"message":"yeah,the order declined successfully"}
        
        return {"message":"Damn!Your order was not found"}

class DeclinedOrders(Resource):
    
    def get(self):

        declinedorders = []
        for order in orders:
            if order.status == "declined":
                declinedorders.append(order)
        
        
        return {"declined orders":[order.serialize() for order in declinedorders]}
        

class PendingOrders(Resource):
    def get(self):
        pendingorders = []
        for order in orders:
            if order.status == "pending":
                pendingorders.append(order)
        return {"pending orders":[order.serialize() for order in pendingorders]}


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
class CompletedOrders(Resource):
    def get(self):
        completedorders = []
        for order in orders:
            if order.status == "completed":
                completedorders.append(order)
        return {"completed orders":[order.serialize() for order in completedorders]}
        



        


