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

        return {
            "Message": "Order created",
            "order":new_order.serialize()
            }, 201

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
        return {"message":"order deleted successful"}, 200
