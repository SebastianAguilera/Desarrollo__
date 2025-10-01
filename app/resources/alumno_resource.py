from flask import jsonify, Blueprint, request 
from app.mapping.alumno_mapping import AlumnoMapping
from app.services.alumno_service import AlumnoService
from markupsafe import escape
from app.validators import validate_with
import logging 

logging.basicConfig(level=logging.DEBUG)

alumno_bp = Blueprint('alumno', __name__)
alumno_mapping = AlumnoMapping()

@alumno_bp.route('/alumno/<int:id>', methods=['GET'])
def buscar_por_id(id):
    alumno = AlumnoService.buscar_alumno(id)
    return alumno_mapping.dump(alumno), 200
@alumno_bp.route('/alumno', methods=['GET'])
def listar_alumnos():
    alumnos = AlumnoService.listar_alumnos()
    return alumno_mapping.dump(alumnos, many=True), 200

@alumno_bp.route('/alumno', methods=['POST']) 
def crear():
    alumno = alumno_mapping.load(request.get_json())
    AlumnoService.crear_alumno(alumno)
    return jsonify("Alumno creado exitosamente"), 201

@alumno_bp.route('/alumno/<int:id>', methods=['PUT'])
def actualizar(id):
    alumno = alumno_mapping.load(request.get_json())
    AlumnoService.actualizar_alumno(alumno, id)
    return jsonify("Alumno actualizado exitosamente"), 200

@alumno_bp.route('/alumno/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    alumno = AlumnoService.eliminar_alumno(id)
    return jsonify("Alumno borrado exitosamente"), 200


def sanitizar_alumno_entrada(request):
    alumno = alumno_mapping.load(request.get_json())
    alumno.nombre = escape(alumno.nombre)
    alumno.apellido = escape(alumno.apellido)
    alumno.nroDocumento = escape(alumno.nroDocumento)
    alumno.fechaNacimiento = escape(alumno.fechaNacimiento)
    alumno.tipoDocumento = escape(alumno.tipoDocumento)
    alumno.sexo = escape(alumno.sexo)
    alumno.nroLegajo = escape(alumno.nroLegajo)
    alumno.fechaIngreso = escape(alumno.fechaIngreso)
    alumno.carrera = escape(alumno.carrera)
    alumno.usuario_id = escape(alumno.usuario_id)
    alumno.especialidad_id = escape(alumno.especialidad_id)
    alumno.universidad_id = escape(alumno.universidad_id)
    

    return alumno


