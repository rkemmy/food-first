import unittest
import json
from app import create_app
from unittest import TestCase
from flask_restful import Resource

from app.api.v1.views import Order, GetOneOrder, AcceptOrder, Status, DeclineOrder, CompleteOrder


class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_orders(self):
        res = self.client.get('/api/v1/orders', content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data)['message'], "empty list")

    def test_list_not_empty(self):
        create_data = {
        "name":"ugali",
        "description":"spicy",
        "price":50,
        "status": "pending"
        }
        res = self.client.post(
            "api/v1/orders",
            data = json.dumps(create_data),
            headers = {"content-type":"application/json"}
        )

        res = self.client.get('/api/v1/orders', content_type='application/json')

        self.assertEqual(res.status_code, 200 )
        print(res)
        self.assertEqual(json.loads(res.data)['Orders'], [{'description': 'spicy', 'id': 4,'name': 'ugali', 'price': 50, 'status': 'pending'}])

        
       

    def test_post_orders(self):
        '''test create food item'''
        create_data = {
            "name":"ugali beef",
            "description":"spicy",
            "price":50,
            "status": "pending"
        }
        response = self.client.post(
            "api/v1/orders",
            data = json.dumps(create_data),
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,201)
        self.assertEqual(json.loads(response.data)['message'], "order successfully created")
        
    # def test_delete_order(self):
    #     res = self.client.delete('/api/v1/orders/1', content_type='application/json')

    def test_get_by_id(self):
        response = self.client.get(
            '/api/v1/orders/1',
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,200)

    def test_complete_order(self):
        response = self.client.put(
            'api/v1/orders/completeorder/1',
            headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)
        

    def test_decline_order(self):
        response = self.client.put(
            "api/v1/orders/decline/1",
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,200)


