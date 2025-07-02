import unittest
import os
from app import db
from app import create_app
from app.models import Nota, Alumno, Universidad, Especialidad
from app.services import AlumnoService, NotaService, UniversidadService, EspecialidadService


class NotaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_nota(self):
        nota = self.__crear_nota()
        self.assertEqual(nota.alumno_id, 1)
        self.assertEqual(nota.materia_id, 1)
        self.assertEqual(nota.autoridad_id, 1)
        self.assertEqual(nota.nota, 10)

    def test_guardar_nota(self):
        nota = self.__crear_nota()
        nota_guardada = NotaService.guardar_nota(nota)
        alumno = AlumnoService.buscar_alumno(1)
        self.assertIsNotNone(nota_guardada)
        self.assertIsNotNone(nota_guardada.id)
        self.assertGreaterEqual(nota_guardada.id, 1)
        self.assertEqual(nota_guardada.alumno_id, alumno.id)
        self.assertEqual(nota_guardada.materia_id, 1)
        self.assertEqual(nota_guardada.autoridad_id, 1)
        self.assertEqual(nota_guardada.nota, 10)

    def test_buscar_nota(self):
        nota = self.__crear_nota()
        alumno = AlumnoService.buscar_alumno(1)
        nota_guardada = NotaService.guardar_nota(nota)
        nota_encontrada = NotaService.buscar_nota(alumno.id)
        self.assertIsNotNone(nota_encontrada)
        self.assertIsNotNone(nota_encontrada.id)
        self.assertGreaterEqual(nota_encontrada.id, 1)
        self.assertEqual(nota_encontrada.alumno_id, alumno.id)
        self.assertEqual(nota_encontrada.materia_id, 1)
        self.assertEqual(nota_encontrada.autoridad_id, 1)
        self.assertEqual(nota_encontrada.nota, 10)

    def __crear_nota(self):
        alumno = self.__crear_alumno()
        alumno_guardado = AlumnoService.crear_alumno(alumno)
        nota = Nota()
        nota.alumno_id = alumno_guardado.id
        nota.materia_id = 1
        nota.autoridad_id = 1
        nota.nota = 10
        return nota

    def __crear_alumno (self):
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
        UniversidadService.crear_universidad(universidad)

        especialidad = Especialidad()
        especialidad.nombre = "Ingenieria en Sistemas"
        especialidad.letra = "IS"
        especialidad.observacion = "Ingenieria en Sistemas"
        EspecialidadService.crear_especialidad(especialidad)
        
        
        alumno = Alumno()
        alumno.nombre = "Agostina"
        alumno.apellido = "Gualpa"
        alumno.nroDocumento = "12345678"
        alumno.fechaNacimiento = "2005-03-30"
        alumno.tipoDocumento = "DNI"
        alumno.sexo = "F"
        alumno.nroLegajo = 10066
        alumno.fechaIngreso = "2020-01-01"
        alumno.carrera = "Ingenieria en Sistemas"
        alumno.universidad_id = universidad.id
        alumno.especialidad_id = especialidad.id  
        return alumno




if __name__ == '__main__':
    unittest.main()

