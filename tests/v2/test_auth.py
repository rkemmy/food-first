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
            "username":"Useradmin",
            "email":"admin@gmail.com",
            "password": "Admin123"
        }
            
        with self.app.app_context():
            db = CreateTables()
            db.drop()
            db.create_tables()
            db.add_admin()

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

    # 


    
