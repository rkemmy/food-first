from flask_restful import Resource
from flask import request
from app.models import orders, Order


class Orders(Resource):

    def get(self):
        if len(orders) == 0:
            return {"message":"empty list"}, 404
        else:
            return {"Orders": [order.serialize() for order in orders]}, 200

    def post(self):
        data = request.get_json(force=True)
        if not data:
            return ({'message': 'No input data provided'}, 400)

        name = data['name']
        description = data['description']
        price = data['price'] 
        
        new_order = Order(name, description, price)

        # if name in orders:
        #     return {'message': 'Order already exists'}
        
        orders.append(new_order)

        return {
            "Message": "Order created",
            "order":new_order.serialize()
            }, 200

    # def delete(self):
    #     all_orders = Order.get_all()
    #     if orders.remove(all_orders):
    #         return {'message': 'all orders deleted'}       


class GetOneOrder(Resource):
    
    def get(self, id):
        
        order  = Order().get_by_id(id)
        if not order:
            return {"Message":"Order not found"},400

        return {"Orders": order.serialize()},200
        

    


    def delete(self, id):
        order  = Order().get_by_id(id)
        if not order:
            return {"Message":"Order not found"},400

        orders.remove(order)
        return {"message":"order deleted successful"}, 200
