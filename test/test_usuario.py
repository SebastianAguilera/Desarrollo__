import unittest
from flask import current_app
from app import create_app
from app.models import Usuario
from app.services import UsuarioService
from app import db
import os

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_usuario(self):
        usuario = Usuario()
        usuario.nombredeusuario = 'alguien'
        usuario.password = 'alguien.123'
        usuario.actividad = True

    def test_crear_usuario(self):
        usuario = Usuario()
        usuario.nombredeusuario = 'alguien'
        usuario.password = 'alguien.123'
        usuario.actividad = True
        usuario_guardado = UsuarioService.guardar_usuario(usuario)
        self.assertIsNotNone(usuario_guardado)
        
    