import json
import unittest

from app import create_app
from testdb import CreateTables


from .base_test import TestApp

class TestMeals(TestApp):


    def helper_admin_login_all_data_ok(self):
        admin_data = {
                "username":"Useradmin",
                "email":"admin@gmail.com",
                "password": "Admin123"}
        
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(admin_data),
            headers={'content-type': 'application/json'}
        )

        return (json.loads(response.data)["token"])
        
    def helper_valid_meal_item(self):
        meal_item = {
                "name": "chai mayai",
                "description": "tamu",
                "price": 400
            }
        return meal_item


    def test_post_valid_data(self):
        admin_token = self.helper_admin_login_all_data_ok()
        meal_item = self.helper_valid_meal_item()
        response = self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(admin_token)},
            data=json.dumps(meal_item)
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)["message"], "Meal successfully created")


    def test_post_invalid_price(self):
        admin_token = self.helper_admin_login_all_data_ok()

        meal_item = {
            "name": "chai mayai",
            "description": "tamu",
            "price": -400
        }
        response = self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(admin_token)},
            data=json.dumps(meal_item)
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Price must be an integer greter than zero")

    def test_post_invalid_price_2(self):
        admin_token = self.helper_admin_login_all_data_ok()

        meal_item = {
            "name": "chai mayai",
            "description": "tamu",
            "price": "400"
        }
        response = self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(admin_token)},
            data=json.dumps(meal_item)
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Price must be an integer greter than zero")

    

    def test_post_invalid_name(self):
        admin_token = self.helper_admin_login_all_data_ok()

        meal_item = {
            "name": "12345",
            "description": "tamu",
            "price": 400
        }

        response = self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(admin_token)},
            data=json.dumps(meal_item)
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "valid food name should contain alphabetic characters")

    def test_post_invalid_name_2(self):
        admin_token = self.helper_admin_login_all_data_ok()

        meal_item = {
            "name": "mealtamu333",
            "description": "tamu",
            "price": 400
        }
        response = self.client.post('/api/v2/menu',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(admin_token)},
            data=json.dumps(meal_item)
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "valid food name should contain alphabetic characters")

    
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

    

    

