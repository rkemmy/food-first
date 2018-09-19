import unittest
import json
from app import create_app



class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def getOrders(self):
        res = self.client.get('/api/v1/orders', content_type='application/json')

        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()