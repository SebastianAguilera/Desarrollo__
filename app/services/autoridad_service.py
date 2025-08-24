from app.models import Autoridad
from app.repositories import AutoridadRepository

class AutoridadService:
    
    @staticmethod
    def crear_autoridad(autoridad: Autoridad):
        "crea una nueva autoridad en la base de datos."
        AutoridadRepository.crear_autoridad(autoridad)
        return autoridad
    
    @staticmethod
    def buscar_por_id(id: int):
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todas():
        return AutoridadRepository.buscar_todas()
    
    @staticmethod
    def actualizar_autoridad( id: int,autoridad: Autoridad):
        return AutoridadRepository.actualizar_autoridad(id,autoridad)
    
    @staticmethod
    def borrar_autoridad(id: int):
        return AutoridadRepository.borrar_autoridad(id)