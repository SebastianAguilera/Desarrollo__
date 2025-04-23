import unittest
from flask import current_app
from app import create_app
from app.models import Facultad

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cart(self):
        facultad= Facultad()
        facultad.nombre = 'Facultad de Ingenieria'
        facultad.abreviatura = 'FI'

        self.assertEqual(facultad.nombre, 'Facultad de Ingenieria')
        self.assertEqual(facultad.abreviatura, 'FI')


if __name__ == '__main__':
    unittest.main()