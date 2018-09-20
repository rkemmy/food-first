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
        self.new_order = {"name": "eggs", "price": 20, "description": "good", "status": "pending"}

    def test_get_orders(self):
        res = self.client.get('/api/v1/orders', content_type='application/json')

        self.assertEqual(res.status_code, 200)

    def test_post_orders(self):
        res = self.client.post('/api/v1/orders', data = json.dumps(self.new_order), content_type='application/json')

        self.assertEqual(res.status_code, 201)

    def test_delete_order(self):
        res = self.client.delete('/api/v1/orders/1', content_type='application/json')

        self.assertEqual(res.status_code, 404)

    def test_get_one_order(self):
        res = self.client.get('/api/v1/orders/1', content_type='application/json')

        self.assertEqual(res.status_code, 200)

    # def test_update_order(self):
    #     res = self.client.put('.api/v1/orders/1', content_type='application/json')

    #     self.assertEqual(res.status_code, 201)

if __name__ == '__main__':
    unittest.main()