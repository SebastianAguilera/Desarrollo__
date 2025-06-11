from app.models import Cargo
from app.repositories import CargoRepository

class CargoService:
    
    @staticmethod
    def crear_cargo(cargo: Cargo) -> Cargo:
        return CargoRepository.crearCargo(cargo)
    
    @staticmethod
    def buscar_cargo_por_id(id: int) -> Cargo | None:
        return CargoRepository.buscar_cargo_por_id(id)  
    
    @staticmethod
    def listar_cargos() -> list[Cargo]:
        return CargoRepository.listar_cargo()
    
    @staticmethod
    def actualizar_cargo(id: int, cargo: Cargo):
        cargo_existente = CargoRepository.buscar_cargo_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        cargo_actualizado = CargoRepository.guardar_cargo(cargo_existente)
        return cargo_actualizado
    
    @staticmethod
    def borrar_por_id(id: int) -> Cargo | None:
        return CargoRepository.borrar_por_id(id)
    