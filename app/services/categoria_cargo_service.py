from app.models import CategoriaCargo
from app.repositories import CategoriaCargoRepository

class CategoriaCargoService:
    @staticmethod
    def crear_categoria_cargo(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        return CategoriaCargoRepository.crear_categoria_cargo(categoria_cargo)

    @staticmethod
    def buscar_categoria_cargo_por_id(id: int) -> CategoriaCargo | None:
        return CategoriaCargoRepository.buscar_categoria_cargo_por_id(id)

    @staticmethod
    def listar_categorias_cargo() -> list[CategoriaCargo]:
        return CategoriaCargoRepository.listar_categorias_cargo()

    @staticmethod
    def actualizar_categoria_cargo(id: int, categoria_cargo: CategoriaCargo) -> CategoriaCargo | None:
        categoria_existente = CategoriaCargoRepository.buscar_categoria_cargo_por_id(id)
        if not categoria_existente:
            return None
        categoria_existente.nombre = categoria_cargo.nombre
        categoria_actualizada = CategoriaCargoRepository.guardar_categoria_cargo(categoria_existente)
        return categoria_actualizada

    @staticmethod
    def borrar_por_id(id: int): 
        return CategoriaCargoRepository.borrar_por_id(id)