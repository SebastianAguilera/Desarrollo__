from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
  @staticmethod
  def crear_orientacion(orientacion: Orientacion):
    OrientacionRepository.crear_orientacion(orientacion)
    return orientacion

  def buscar_orientacion(id: int):
    orientacion = OrientacionRepository.buscar_orientacion(id)
    return orientacion
    
  def actualizar_orientacion(orientacion: Orientacion, id: int):
    OrientacionRepository.actualizar_orientacion(orientacion, id)
    return orientacion
  
  def eliminar_orientacion(id: int):
    orientacion = OrientacionRepository.eliminar_orientacion(id)
    
  