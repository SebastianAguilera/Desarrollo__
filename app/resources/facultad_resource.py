from flask import jsonify, Blueprint, request 
from app.mapping.facultad_mapping import FacultadMapping
from app.services.facultad_service import FacultadService
from markupsafe import escape
facultad_bp = Blueprint('facultad', __name__)
facultad_mapping = FacultadMapping()
#from app.validators import validate_with

#<hashid:id>

@facultad_bp.route('/facultad/<hashid:id>', methods=['GET']) #Funciona
def buscar_por_id(id):
    facultad = FacultadService.buscar_facultad(id)
    return facultad_mapping.dump(facultad), 200

@facultad_bp.route('/facultad', methods=['GET'])
def listar_facultades():
    facultades = FacultadService.listar_facultades()
    return facultad_mapping.dump(facultades, many=True), 200

@facultad_bp.route('/facultad', methods=['POST']) #Funciona
def crear():
    facultad = facultad_mapping.load(request.get_json())
    FacultadService.crear_facultad(facultad)
    return jsonify("Facultad creada exitosamente"), 201 #201 significa creado exitosamente

@facultad_bp.route('/facultad/<hashid:id>', methods=['PUT']) #Funciona
#@validate_with(FacultadMapping) #validar acciones con marshmallow, 
def actualizar(id):
    facultad = facultad_mapping.load(request.get_json()) #cada vez que se llama al load sanitiza
    FacultadService.actualizar_facultad( facultad, id)
    return jsonify("Facultad actualizada exitosamente"), 200 

@facultad_bp.route('/facultad/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    facultad = FacultadService.eliminar_Facultad(id)
    return jsonify("Facultad borrada exitosamente"), 200 #200 significa que se borro exitosamente


def sanitizar_facultad_entrada(request):
  facultad= facultad_mapping.load(request.get_json())
  facultad.nombre = escape(facultad.nombre)
  facultad.sigla = escape(facultad.sigla)
  facultad.codigoPostal = escape(facultad.codigoPostal)
  facultad.abreviatura= escape(facultad.abreviatura)
  facultad.directorio= escape(facultad.directorio)
  facultad.ciudad= escape(facultad.ciudad)
  facultad.domicilio= escape(facultad.domicilio)
  facultad.telefono= escape(facultad.telefono)
  facultad.contacto= escape(facultad.contacto)
  facultad.email= escape(facultad.email)

  return facultad






