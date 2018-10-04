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
            CreateTables.drop()
            CreateTables.create_tables()
            CreateTables.add_admin()


    


        

        