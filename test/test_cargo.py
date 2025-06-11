import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import Cargo
from app.services import CargoService

class CargoTestCase(unittest.TestCase):

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

    def test_cargo_creation(self):
        cargo = self._nuevoCargo()
        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, 'Decano')
        self.assertEqual(cargo.puntos, 2)

    def test_crear_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear_cargo(cargo)
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.id)
        self.assertGreaterEqual(cargo.id, 1)
        self.assertEqual(cargo.nombre, 'Decano')
        self.assertEqual(cargo.puntos, 2)

    def test_buscar_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear_cargo(cargo)
        cargo_encontrado = CargoService.buscar_cargo_por_id(cargo.id)
        self.assertIsNotNone(cargo_encontrado)
        self.assertEqual(cargo_encontrado.nombre, 'Decano')
        self.assertEqual(cargo_encontrado.puntos, 2)

    def test_listar_cargos(self):
        cargo1 = self._nuevoCargo()
        cargo2 = self._nuevoCargo()
        cargo2.nombre = 'Profesor'
        cargo2.puntos = 1
        CargoService.crear_cargo(cargo1)
        CargoService.crear_cargo(cargo2)
        cargos = CargoService.listar_cargos()
        self.assertEqual(len(cargos), 2)
        self.assertIn(cargo1, cargos)
        self.assertIn(cargo2, cargos)

    def test_actualizar_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear_cargo(cargo)
        cargo.nombre = 'Decano Actualizado'
        cargo.puntos = 3
        cargo_actualizado = CargoService.actualizar_cargo(cargo.id, cargo)
        self.assertIsNotNone(cargo_actualizado)
        self.assertEqual(cargo_actualizado.nombre, 'Decano Actualizado')
        self.assertEqual(cargo_actualizado.puntos, 3)

    def test_borrar_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear_cargo(cargo)
        cargo_borrado = CargoService.borrar_por_id(cargo.id)
        self.assertIsNotNone(cargo_borrado)
        self.assertEqual(cargo_borrado.nombre, 'Decano')
        self.assertEqual(cargo_borrado.puntos, 2)
        cargo_buscado = CargoService.buscar_cargo_por_id(cargo.id)
        self.assertIsNone(cargo_buscado)

    def _nuevoCargo(self):
        cargo = Cargo()
        cargo.nombre = 'Decano'
        cargo.puntos = 2
        return cargo

if __name__ == '__main__':
    unittest.main()

