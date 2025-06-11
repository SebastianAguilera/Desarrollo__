import unittest
from flask import current_app
from app import create_app
from app.models import Universidad
from app.services import UniversidadService
from app import db

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_Universidad(self):
        universidad= self.__crear_universidad()
        self.assertEqual(universidad.nombre, 'Universidad Tecnologica Nacional')
        self.assertEqual(universidad.sigla, "UTN")
        self.assertEqual(universidad.tipo, "publica")
        self.assertEqual(universidad.anioFundacion, "1948")        
        self.assertEqual(universidad.direccion, "direccion")
        self.assertEqual(universidad.telefono, "telefono")
        self.assertEqual(universidad.email, "email")

    def test_crear_universidad(self):
        universidad= self.__crear_universidad()
        universidad_guardada =UniversidadService.crear_Universidad(Universidad)
        self.assertIsNotNone(universidad_guardada)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad_guardada.id, 1)
        self.assertEqual(universidad_guardada.nombre, universidad.nombre) 
        self.assertEqual(universidad_guardada.sigla, universidad.sigla)
        self.assertEqual(universidad_guardada.tipo, universidad.tipo)
        self.assertEqual(universidad_guardada.anioFundacion, universidad.anioFundacion)
        self.assertEqual(universidad_guardada.direccion, universidad.direccion) 
        self.assertEqual(universidad_guardada.telefono, universidad.telefono)   
        self.assertEqual(universidad_guardada.email, universidad.email) 
    

    def test_buscar_universidad(self):
        
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)

        universidad_encontrada= UniversidadService.buscar_universidad(1)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, universidad_encontrada.nombre)
        self.assertEqual(universidad.sigla, universidad_encontrada.sigla)
        self.assertEqual(universidad.tipo, universidad_encontrada.tipo)
        self.assertEqual(universidad.anioFundacion, universidad_encontrada.anioFundacion)
        self.assertEqual(universidad.direccion, universidad_encontrada.direccion)
        self.assertEqual(universidad.telefono, universidad_encontrada.telefono)
        self.assertEqual(universidad.email, universidad_encontrada.email)

    def test_actualizar_universidad(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)
        nuevosdatosuniversidad=Universidad()
        nuevosdatosuniversidad.nombre = 'Universidad Tecnologica Nacional Modificada'
        nuevosdatosuniversidad.sigla = 'UTN Modificada'
        nuevosdatosuniversidad.tipo = 'privada'
        nuevosdatosuniversidad.anioFundacion = '1950'
        nuevosdatosuniversidad.direccion = 'Nueva Direccion'
        nuevosdatosuniversidad.telefono = 'Nuevo Telefono'
        nuevosdatosuniversidad.email = 'email'
    
        universidadmodificada = UniversidadService.actualizar_universidad(nuevosdatosuniversidad, universidad.id)
        universidadencontrada = UniversidadService.buscar_universidad(universidad.id)
        self.assertIsNotNone(universidadencontrada)
        self.assertIsNotNone(universidadencontrada.id)
        self.assertGreaterEqual(universidadencontrada.id, 1)
        self.assertEqual(universidadencontrada.nombre, universidadmodificada.nombre)
        self.assertEqual(universidadencontrada.sigla, universidadmodificada.sigla)  
        self.assertEqual(universidadencontrada.tipo, universidadmodificada.tipo)    
        self.assertEqual(universidadencontrada.anioFundacion, universidadmodificada.anioFundacion)  
        self.assertEqual(universidadencontrada.direccion, universidadmodificada.direccion)  
        self.assertEqual(universidadencontrada.telefono, universidadmodificada.telefono)
        self.assertEqual(universidadencontrada.email, universidadmodificada.email)

    

    def test_eliminar_universidad(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)
        UniversidadService.eliminar_universidad(universidad.id)
        universidad_encontrada = UniversidadService.buscar_universidad(universidad.id)
        self.assertIsNone(universidad_encontrada)

    def __crear_universidad(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
        universidad.anioFundacion = "1948"
        universidad.direccion = "direccion"
        universidad.telefono = "telefono"
        universidad.email = "email"
    
     
        return universidad
    
if __name__ == '__main__':
    unittest.main()