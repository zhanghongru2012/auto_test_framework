import unittest
import requests
import json
import time
from Base.retry_func import retry_method, retry_class
from Base.FuncApi.api_funcs import submit_order, get_user_info


class TestRecv(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    # @retry_method(2)
    def test_mobile_submit_order(self):
        self.assertEqual(200, submit_order())

    def test_mobile_order_check(self):
        get_user_info()


if __name__ == '__main__':
    unittest.main()
