import json
import unittest

from app import create_app
from testdb import CreateTables
from .base_test import TestApp

from .test_meals import TestMeals


class TestOrders(TestApp):
    
    def test_post_order(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        response = self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )
        print(response.data)
        self.assertEqual(response.status_code, 201)

    
    def test_get_all_orders(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.get('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
        )


        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_orders(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.get('/api/v2/users/orders/1',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
        )

        self.assertEqual(response.status_code, 200)

    def test_get_all_orders(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.put('/api/v2/users/orders/1',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps({"status":"Processing"})
        )


        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_delete_order(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.delete('/api/v2/users/orders/1',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            )
        
        self.assertEqual(response.status_code, 200)

    def test_get_user_order_history(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.get('api/v2/users/history',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
        
        )

        self.assertEqual(response.status_code, 200)




