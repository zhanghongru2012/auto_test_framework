import unittest
import requests


class TestRecv(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_goobe_search(self):
        url = 'https://goobe.io/search.aspx?k=python'
        r = requests.get(url)
        self.assertEqual(200, r.status_code)


if __name__ == '__main__':
    unittest.main()
