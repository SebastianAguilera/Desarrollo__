import unittest
from flask import current_app
from app import create_app, db
from app.models import Autoridad
from app.services import AutoridadService

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  #crea tablas

    def tearDown(self):
        db.session.remove()
        db.drop_all()  #borra tablas despues de cada test
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
        
    def test_autoridad(self):
        autoridad = Autoridad()
        autoridad.nombre="Dra. Ana Prez"
        autoridad.cargo="Decana"
        autoridad.telefono="123456789"
        autoridad.email="ana.perezuniversidad.edu"
        
        self.assertEqual(autoridad.nombre, "Dra. Ana Prez")
        self.assertEqual(autoridad.cargo, "Decana")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "ana.perezuniversidad.edu")
    

if __name__ == '__main__':
    unittest.main()
