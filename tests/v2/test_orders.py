import json
import unittest

from app import create_app
from testdb import CreateTables
from .base_test import TestApp

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    # def test_post_order(self):
        
    #     response = self.client.post('api/v2/users/orders',
    #         headers = {"content-type":"application/json"}
    #     )
    #     self.assertEqual(response.status_code, 201)
