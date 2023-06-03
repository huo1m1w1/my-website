import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Your Website!', response.data)

    def test_ai(self):
        response = self.app.get('/ai')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the AI page.', response.data)

    def test_data_engineering(self):
        response = self.app.get('/data-engineering')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data Engineering', response.data)
        self.assertIn(b'ETL (Extract, Transform, Load)', response.data)        

    def test_cloud(self):
        response = self.app.get('/cloud')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cloud Computing', response.data)
        self.assertIn(b'Types of Cloud Services', response.data)    

    def test_python(self):
        response = self.app.get('/python')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the Python page.', response.data)

    def test_submit(self):
        response = self.app.post('/submit', data={'name': 'John Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)


if __name__ == '__main__':
    unittest.main()






