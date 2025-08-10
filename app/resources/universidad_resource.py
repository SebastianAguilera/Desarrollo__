from flask import jsonify, Blueprint, request 
from app.mapping.universidad_mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService
from markupsafe import escape
universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()
#from app.validators import validate_with

"""
@universidad_bp.route('/universidad', methods=['GET'])
def buscar_todos():
    universidades = UniversidadService.buscar_universidad()

    return universidad_mapping.dump(universidades, many=True), 200

#dump convierte el objeto a un diccionario o json
"""


@universidad_bp.route('/universidad/<int:id>', methods=['GET']) #Funciona
def buscar_por_id(id):
    universidad = UniversidadService.buscar_universidad(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['GET'])
def listar_universidades():
    universidades = UniversidadService.listar_universidades()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad', methods=['POST']) #Funciona
def crear():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear_universidad(universidad)
    return jsonify("Universidad creada exitosamente"), 201 #201 significa creado exitosamente

@universidad_bp.route('/universidad/<int:id>', methods=['PUT']) #Funciona
#@validate_with(UniversidadMapping) #validar acciones con marshmallow, 
def actualizar(id):
    universidad = universidad_mapping.load(request.get_json()) #cada vez que se llama al load sanitiza
    UniversidadService.actualizar_universidad(universidad, id)
    return jsonify("Universidad actualizada exitosamente"), 200 

@universidad_bp.route('/universidad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    universidad = UniversidadService.eliminar_universidad(id)
    return jsonify("Universidad borrada exitosamente"), 200 #200 significa que se borro exitosamente



def sanitizar_universidad_entrada(request):
  universidad = universidad_mapping.load(request.get_json())
  universidad.nombre = escape(universidad.nombre)
  universidad.sigla = escape(universidad.sigla)
  universidad.tipo = escape(universidad.tipo) 
  return universidad






#crea un objeto json que se le va a devolver al usuario
#para ejecutar para probarlo desde el postman por ej, hay que crear las tablas y un migrate
#abrio el pgadmin para ver las tablas
#en consola:
#flask db migrate 
#hay que modificar las variables de flask context para que la base sea PROD
#flask db init
#migraciones en env.py:
#from app .models import *
#flask db upgrade
#flask app.py
