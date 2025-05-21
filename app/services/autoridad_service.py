from app.models import Autoridad
from app import db
from app.repositories import AutoridadRepository

#encargada de la logica de servicios, que me haga reportes etc

class AutoridadService:
    
    @staticmethod
    def crear_autoridad(autoridad: Autoridad):
        "crea una nueva autoridad en la base de datos."
        
        AutoridadRepository.crear(autoridad)
        
    @staticmethod
    def buscar_por_id():
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def actualizar_autoridad():
        return AutoridadRepository.actualizar_autoridad(id)