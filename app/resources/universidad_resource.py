from flask import jsonify, Blueprint 
from app.mapping.universidad_mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidad', methods=['GET'])
def buscar_todos():
    universidades = UniversidadService.buscar_todos()

    return universidad_mapping.dump(universidades, many=True), 200

#dump convierte el objeto a un diccionario o json

@universidad_bp.route('/universidad/<int: id>', methods=['GET'])
def buscar_por_id(id):
    universidad = UniversidadService.buscar_por_id(id)

    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['POST'])
def crear():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear(universidad)

    return jsonify("Universidad creada exitosamente"), 201 #201 significa creado exitosamente

@universidad_bp.route('/universidad/<int: id>', methods=['DELETE'])

def borrar_por_id(id):
    universidad = UniversidadService.borrar_por_id(id)

    return jsonify("Universidad borrada exitosamente"), 200 #200 significa que se borro exitosamente

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
