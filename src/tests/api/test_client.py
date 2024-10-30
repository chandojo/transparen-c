from api.client import Client
import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client("testurl.com", {'Accept': 'application/json'})

    def test_client_args(self):
        self.assertEqual(self.client.url, "testurl.com")
        self.assertEqual(self.client.headers, {'Accept': 'application/json'})

    def test_client_get_exception(self):
        self.assertRaises(Exception, self.client.get())

    def tearDown(self):
        del self.client


if __name__ == '__main__':
    unittest.main()
