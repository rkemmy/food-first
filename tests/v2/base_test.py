import os
import json

import unittest

from app import create_app

from testdb import CreateTables

class TestApp(unittest.TestCase):

    def setUp(self):
        """ set up test """
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            CreateTables().drop()
            CreateTables().create_tables()
            CreateTables().add_admin()

        self.create_user_data = {
            "username":"Useradmin",
            "email":"admin@gmail.com",
            "password": "Admin123"
        }

        self.order = {
            "username": "remmy",
	        "name":"ugali 4",
	        "description": "djss"
        }
        self.meal = {
            "name":"ugali 4",
            "description": "djss",
            "price": 23
        }

        

    def signup(self):
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(self.create_user_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login(self):
        login_data = {
            "username": "Useradmin",
            "password": "Admin123"
        }
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )
        return response

        
    def get_token(self):
        """ function to get user token """

        self.signup()
        response = self.login()
        token = json.loads(response.data).get('token', None)
        return token

    


        

        