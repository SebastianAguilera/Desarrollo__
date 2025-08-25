import unittest
from flask import current_app
from app import create_app, db
from app.models import Autoridad
from app.services import AutoridadService
import os

class CartTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
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
    
    def test_crear_autoridad(self):
        autoridad = self.__nueva_autoridad()
        autoridad_guardada = AutoridadService.crear_autoridad(autoridad)
        
        self.assertIsNotNone(autoridad_guardada)
        self.assertIsNotNone(autoridad_guardada.id)
        self.assertGreaterEqual(autoridad_guardada.id,1)
        self.assertEqual(autoridad_guardada.nombre, autoridad.nombre)
        
    def test_buscar_autoridad_por_id(self):
        autoridad = self.__nueva_autoridad()
        AutoridadService.crear_autoridad(autoridad)
        resultado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Dra. Ana Perez")
    
    def test_actualizar_autoridad(self):
        autoridad = self.__nueva_autoridad()  
        AutoridadService.crear_autoridad(autoridad)

        autoridad_actualizada = Autoridad()
        autoridad_actualizada.nombre = "Dra. Belen"
        autoridad_actualizada.cargo = "Decana"
        autoridad_actualizada.email = "email"
        autoridad_actualizada.telefono = "2604567688"

        autoridad_modificada = AutoridadService.actualizar_autoridad(autoridad.id, autoridad_actualizada)

        autoridad_encontrada = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNotNone(autoridad_encontrada)
        self.assertIsNotNone(autoridad_encontrada.id)
        self.assertGreaterEqual(autoridad_encontrada.id, 1)
        self.assertEqual(autoridad_encontrada.nombre, autoridad_modificada.nombre)
        self.assertEqual(autoridad_encontrada.cargo, autoridad_modificada.cargo)
        self.assertEqual(autoridad_encontrada.email, autoridad_modificada.email)
        self.assertEqual(autoridad_encontrada.telefono, autoridad_modificada.telefono)

        
    def test_borrar_autoridad(self):
        autoridad = self.__nueva_autoridad()
        AutoridadService.crear_autoridad(autoridad)
        AutoridadService.borrar_autoridad(autoridad.id)
        autoridad_encontrada = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNone(autoridad_encontrada)

    def __nueva_autoridad(self):
        return Autoridad(
            nombre="Dra. Ana Perez",
            cargo="Decana",
            telefono="123456789",
            email="ana.perezuniversidad.edu"
        )

if __name__ == '__main__':
    unittest.main()
