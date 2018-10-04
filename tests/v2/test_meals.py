import json
import unittest

from app import create_app
from testdb import CreateTables
from .base_test import TestApp

class TestMeals(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()


    # def test_add_with_authorization(self):
    #     sample = {
    #         "name": "Kuku",
    #         "description": "Tehhshshs",
    #         "price": 300
    #     }
    #     test_user = {
    #         "username": "Useradmin",
    #         "password": "Admin123"
    #     }
 
    #     login_response = self.client.post("/api/v2/auth/login", data=json.dumps(test_user),
    #     content_type="application/json"
    #     )
        
    #     login_response_obj = json.loads(login_response.data)
    #     response = self.client.post("/api/v2/menu", data=json.dumps(sample),
    #       headers = {
    #           "Content-Type":"application/json",
    #           "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzg2NjM1NTYsIm5iZiI6MTUzODY2MzU1NiwianRpIjoiNDBjYWQyMGYtNTExZS00OThiLTlhMGUtZGE0MzBkYjE4MDg5IiwiZXhwIjoxNTM4NzIzNTU2LCJpZGVudGl0eSI6WyJVc2VyYWRtaW4iLHRydWVdLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.xwbnpchWowgzj0EQ0C5B89tfCM0F2ofmeHtTWehEArI"
    #       }
    #     )
    #     response_obj = json.loads(response.data)
    #     message = response_obj.get("msg", response_obj.get("message", ""))
    #     self.assertEqual(message, "Meal successfully created")

    def test_get_all_meals(self):
        response = self.client.get(
            'api/v2/menu'
        )

        self.assertEqual(response.status_code, 200)

    # def
