import unittest
import os
from app import db
from app import create_app
from app.models import Nota


class NotaTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_nota(self):
        notaa = Nota()
        
        notaa.alumno_id = 1
        notaa.materia_id = 1
        notaa.autoridad_id = 1
        notaa.nota = 10

