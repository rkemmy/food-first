import unittest
import json

from app import create_app
# from flask import jsonify, current_app
from testdb import CreateTables

from  .base_test import TestApp

class TestUser(TestApp):

    def setUp(self):
        """ set up test """

        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.create_user_data = {
                "username":"risperk",
                "email":"remmyk@gmail.com",
                "password": "Password123"
            }
            
        with self.app.app_context():
            db = CreateTables()
            db.drop()
            db.create_tables()
            db.add_admin()

    def signup(self):
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(self.create_user_data),
            headers={'content-type': 'application/json'}
        )

        return response

    def login(self):
        login_data = {
            "username": "risperk",
            "password": "Password123"
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
        print(token)
        return token

    def test_user_signup(self):
        
        response = self.signup()

        print(response)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)["message"], "Account created successfully")
       

    def test_user_login(self):
        self.test_user_signup()

        response = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["message"], "You were successfully logged in risperk")

    def test_invalid_email(self):
        create_user_data = {
                "username":"risperk",
                "email":"remmykgmail.com",
                "password": "Password123"}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Invalid email")

    def test_invalid_password_fields(self):
        user = {
                "username":"risperk",
                "email":"remmyk@gmail.com",
                "password": ""}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Enter a valid password")


    def test_empty_invalid_username(self):
        create_user_data = {
                "username":"",
                "email":"remmyk@gmail.com",
                "password": "Password123"}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Please enter a valid username")
    


    
