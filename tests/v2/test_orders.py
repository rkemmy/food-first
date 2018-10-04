import unittest
import json


from app import create_app

from testdb import CreateTables

class TestApp(unittest.TestCase):
    def setup(self):
        """ set up test """

        self.app = create_app("testing")
        self.app_client = self.app.test_client()
        with self.app.app_context():
            CreateTables.drop()
            CreateTables.create_tables()
            CreateTables.add_admin()
        

        self.create_user_data = {
            "username":"",
            "email":"",
            "password": ""
        }
        

    def signup(self):
        """ sign up method """
        res = self.app_client.post(
            
        )