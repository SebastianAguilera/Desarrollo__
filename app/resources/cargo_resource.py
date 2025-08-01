from flask import jsonify, Blueprint, request 
from app.mapping.cargo_mapping import CargoMapping
from app.services.cargo_service import CargoService
from markupsafe import escape

cargo_bp = Blueprint('cargo', __name__)
cargo_mapping = CargoMapping()

@cargo_bp.route('/cargo', methods=['GET'])
def buscar_todos():
    cargos = CargoService.listar_cargos()
    return cargo_mapping.dump(cargos, many=True), 200 


@cargo_bp.route('/cargo/<int:id>', methods=['GET']) 
def buscar_por_id(id):
    cargo = CargoService.buscar_cargo_por_id(id)
    return cargo_mapping.dump(cargo), 200

@cargo_bp.route('/cargo', methods=['POST']) 
def crear():
    cargo = cargo_mapping.load(request.get_json())
    CargoService.crear_cargo(cargo)
    return jsonify("Cargo creado exitosamente"), 201 

    
@cargo_bp.route('/cargo/<int:id>', methods=['PUT'])  
def actualizar(id):
    cargo = cargo_mapping.load(request.get_json())
    CargoService.actualizar_cargo(id, cargo)
    return jsonify("Cargo actualizado exitosamente"), 200

@cargo_bp.route('/cargo/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    cargo = CargoService.borrar_por_id(id)
    return jsonify("Cargo borrado exitosamente"), 200 

def sanitizar_cargo_entrada(request):
    cargo = cargo_mapping.load(request.get_json())
    cargo.nombre = escape(cargo.nombre)
    return cargo
