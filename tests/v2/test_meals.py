import json
import unittest

from app import create_app
from testdb import CreateTables
from .base_test import TestApp

class TestMeals(TestApp):

    
    def test_get_all_meals(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )
        response = self.client.get(
            'api/v2/menu'
        )

        self.assertEqual(response.status_code, 200)

    def test_del_meal(self):
        token = self.get_token()
        self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        response = self.client.delete('/api/v2/menu/1', headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},)

        
        self.assertEqual(response.status_code, 200)

    

