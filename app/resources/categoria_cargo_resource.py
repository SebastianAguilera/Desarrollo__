from flask import jsonify, Blueprint, request
from app.mapping.categoria_cargo_mapping import CategoriaCargoMapping
from app.services.categoria_cargo_service import CategoriaCargoService

categoria_cargo_bp = Blueprint('categoria_cargo', __name__)
categoria_cargo_mapping = CategoriaCargoMapping()

@categoria_cargo_bp.route('/categoria_cargo', methods=['GET'])
def buscar_todas():
    categorias = CategoriaCargoService.listar_categorias_cargo()
    return categoria_cargo_mapping.dump(categorias, many=True), 200

@categoria_cargo_bp.route('/categoria_cargo/<int:id>', methods=['GET'])
def buscar_por_id(id):
    categoria = CategoriaCargoService.buscar_categoria_cargo_por_id(id)
    return categoria_cargo_mapping.dump(categoria), 200

@categoria_cargo_bp.route('/categoria_cargo', methods=['POST'])
def crear():
    categoria = categoria_cargo_mapping.load(request.get_json())
    CategoriaCargoService.crear_categoria_cargo(categoria)
    return jsonify("Categoría creada exitosamente"), 201

@categoria_cargo_bp.route('/categoria_cargo/<int:id>', methods=['PUT'])
def actualizar(id):
    categoria = categoria_cargo_mapping.load(request.get_json())
    CategoriaCargoService.actualizar_categoria_cargo(id, categoria)
    return jsonify("Categoría actualizada exitosamente"), 200

@categoria_cargo_bp.route('/categoria_cargo/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    CategoriaCargoService.borrar_por_id(id)
    return jsonify("Categoría borrada exitosamente"), 200
