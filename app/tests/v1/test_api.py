import unittest
import json
from app import create_app
from unittest import TestCase
from flask_restful import Resource

from app.api_v1.orders.views import Order, GetOneOrder


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
       

    def test_post_orders(self):
        '''test create food item'''
        create_data = {
            "name":"ugali",
            "description":"spicy",
            "price":50
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

    def test_get_completed_orders(self):
        response = self.client.get(
            'api/v1/orders/completed',
            headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)


    def test_get_pending_orders(self):
        response = self.client.get(
            'api/v1/orders/pending',
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

    def test_declined_orders(self):
        response = self.client.get(
            "api/v1/orders/declined",
        headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)

    def test_get_approved_orders(self):
        response = self.client.get(
            "api/v1/orders/approved",
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,200)

