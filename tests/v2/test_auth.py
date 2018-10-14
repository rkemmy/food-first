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
        self.assertEqual(json.loads(response.data)["message"], "Valid email should be alphanumeric with the @ and . symbol")

    def test_invalid_username(self):
        create_user_data = {
                "username":"1234wer",
                "email":"remmykgmail.com",
                "password": "Password123"}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Valid username should be alphabetic, between 6 and 20 characters")

    def test_invalid_password(self):
        create_user_data = {
                "username":"remmymiss",
                "email":"remmyk@gmail.com",
                "password": "        "}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Valid password should be alphanumeric, between 8 to 20 characters")

    def test_duplicated_username(self):
        create_user_data = {
                "username":"remmymiss",
                "email":"remmyk@gmail.com",
                "password": "password129"}

        create_user_data_2 = {
                "username":"remmymiss",
                "email":"dennisb@gmail.com",
                "password": "password129"}
        
        self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data_2),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "username already in use")

    def test_duplicated_email(self):
        create_user_data = {
                "username":"dennisb",
                "email":"dennisb@gmail.com",
                "password": "password129"}

        create_user_data_2 = {
                "username":"remmymiss",
                "email":"dennisb@gmail.com",
                "password": "password129"}
        
        self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data_2),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "email already in use")

    def test_registration_all_data_ok(self):
        create_user_data = {
                "username":"dennisb",
                "email":"dennisb@gmail.com",
                "password": "password129"}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)["message"], "Account created successfully")

    def test_login_all_data_ok(self):
        create_user_data = {
                "username":"dennisb",
                "email":"dennisb@gmail.com",
                "password": "password129"}
        
        self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["message"], "You were successfully logged in dennisb")
        self.assertTrue(json.loads(response.data)["token"])

    def test_login_wrong_password(self):
        create_user_data = {
                "username":"dennisb",
                "email":"dennisb@gmail.com",
                "password": "password129"}

        wrong_password = {
                "username":"dennisb",
                "password": "wrongpassword"}
        
        self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(wrong_password),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Wrong password")

    def test_login_non_existent_user(self):
        not_user = {
                "username":"kenyamoja",
                "password": "apassword"}
        
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(not_user),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)["message"], "user not found")


    def test_admin_login_all_data_ok(self):
        admin_data = {
                "username":"Useradmin",
                "email":"admin@gmail.com",
                "password": "Admin123"}
        
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(admin_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["message"], "You were successfully logged in Useradmin")
        self.assertTrue(json.loads(response.data)["token"])

    # 


    
