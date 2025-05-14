import unittest
from flask import current_app
from app import create_app
from app.models import Materia

class MateriaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_materia(self):
        materia = Materia()
        materia.nombre = 'Algebra y geometria'
        materia.diseno_curricular = 'diseno curricular'
        materia.correlativas = []
        materia.horas_dictadas = '36'
        materia.promocional = True
        materia.nivel = '1'
          
        self.assertEqual(materia.nombre, 'Algebra y geometria')
        self.assertEqual(materia.diseno_curricular, 'diseno curricular')
        self.assertEqual(materia.correlativas, [])
        self.assertEqual(materia.horas_dictadas, '36')
        self.assertEqual(materia.promocional, True)
        self.assertEqual(materia.nivel, '1')

if __name__ == '__main__':
    unittest.main()