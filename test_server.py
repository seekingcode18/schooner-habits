import unittest
from server import server

class TestServer(unittest.TestCase):
    print(server)
    def setUp(self):
        server.testing = True
        self.server = server.test_client()

    def test_home_renders(self):
        response = self.server.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_renders_correctly(self):
        response = self.server.get('/')
        self.assertTrue(b'Home page' in response.data)

    def test_dashboard_renders(self):
        response = self.server.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_renders_correctly(self):
        response = self.server.get('/dashboard')
        self.assertTrue(b'Habits' in response.data)

if __name__ == "__main__":
    unittest.main()