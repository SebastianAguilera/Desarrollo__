import unittest
from flask import current_app
from app import create_app
from app.models import Facultad
from app.services import FacultadService

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_facultad(self):
        facultad= Facultad()
        facultad.nombre = 'Facultad de Ingenieria'
        facultad.abreviatura = 'FI'
        facultad.directorio = "directorio"
        facultad.sigla = "sigla"
        facultad.codigoPostal = "codigoPostal"
        facultad.ciudad = "ciudad"
        facultad.domicilio = "domicilio"
        facultad.telefono = "telefono"
        facultad.contacto = "contacto"
        facultad.email = "email"
        
        self.assertEqual(facultad.nombre, 'Facultad de Ingenieria')
        self.assertEqual(facultad.abreviatura, 'FI')
        self.assertEqual(facultad.directorio, "directorio")
        self.assertEqual(facultad.sigla, "sigla")
        self.assertEqual(facultad.codigoPostal, "codigoPostal")
        self.assertEqual(facultad.ciudad, "ciudad")
        self.assertEqual(facultad.domicilio, "domicilio")
        self.assertEqual(facultad.telefono, "telefono")
        self.assertEqual(facultad.contacto, "contacto")
        self.assertEqual(facultad.email, "email")
    def test_crear_facultad(self):
        facultad= Facultad()
        facultad.nombre = 'Facultad de Ingenieria'
        facultad.abreviatura = 'FI'
        facultad.directorio = "directorio"
        facultad.sigla = "sigla"
        facultad.codigoPostal = "codigoPostal"
        facultad.ciudad = "ciudad"
        facultad.domicilio = "domicilio"
        facultad.telefono = "telefono"
        facultad.contacto = "contacto"
        facultad.email = "email"
        FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, 'Facultad de Ingenieria')
        self.assertEqual(facultad.abreviatura, 'FI')
        self.assertEqual(facultad.directorio, "directorio")
        self.assertEqual(facultad.sigla, "sigla")
        self.assertEqual(facultad.codigoPostal, "codigoPostal")
        self.assertEqual(facultad.ciudad, "ciudad")
        self.assertEqual(facultad.domicilio, "domicilio")
        self.assertEqual(facultad.telefono, "telefono")
        self.assertEqual(facultad.contacto, "contacto")
        self.assertEqual(facultad.email, "email")
        




if __name__ == '__main__':
    unittest.main()