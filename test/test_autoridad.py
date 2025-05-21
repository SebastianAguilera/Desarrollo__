import unittest
from flask import current_app
from app import create_app, db
from app.models import Autoridad
from app.services import AutoridadService

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
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
        autoridad.nombre="Dra. Ana Pérez"
        autoridad.cargo="Decana"
        autoridad.telefono="123456789"
        autoridad.email="ana.perez@universidad.edu"
        
        self.assertEqual(autoridad.nombre, "Dra. Ana Pérez")
        self.assertEqual(autoridad.cargo, "Decana")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "ana.perez@universidad.edu")
    
    def test_crear_autoridad(self):
        
        autoridad = self.__nuevaautoridad()  
        
        AutoridadService.crear_autoridad(autoridad)
        
        self.assertIsNotNone(autoridad)
        self.assertIsNotNone(autoridad.id)
        self.assertGreaterEqual(autoridad.id,1)
        self.assertEqual(autoridad.nombre,"Dra. Ana Pérez")
        
    def __nuevaautoridad(autoridad):
        autoridad = Autoridad()
        autoridad.nombre="Dra. Ana Pérez"
        autoridad.cargo="Decana"
        autoridad.telefono="123456789"
        autoridad.email="ana.perez@universidad.edu" 
        return autoridad
    
    def test_actualizar_autoridad(autoridad):
        autoridad = self.__nuevaautoridad()  
        AutoridadService.crear_autoridad(autoridad)
        autoridad.nombre = ""
        autoridad_actualizada= AutoridadService.test_actualizar_autoridad(autoridad.nombre,autoridad.cargo,)
        
    
    def test_buscar_autoridad():
        autoridad = self.__nuevaautoridad()  
        AutoridadService.crear_autoridad(autoridad)
        
    
    def test_borrar_autoridad():
        autoridad = self.__nuevaautoridad()  
        AutoridadService.crear_autoridad(autoridad)
        
if __name__ == '__main__':
    unittest.main()
