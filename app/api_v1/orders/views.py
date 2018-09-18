from flask_restful import Resource
from flask import request
from app.models import orders, Order


class Orders(Resource):

    def get(self):
        if len(orders) == 0:
            return {"message":"empty list"}, 404
        else:
            return {"Orders": [order.serialize() for order in orders]}, 200