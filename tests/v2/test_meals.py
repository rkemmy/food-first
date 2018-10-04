import json


from test_orders import TestApp


class Testing(TestApp):

    def test_signup(self):
        
        res = self.signup()

        self.assertEqual(res.status_code, 201)
