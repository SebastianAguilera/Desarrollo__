from app.models import Grado
from app.repositories.grado_repositorio import GradoRepository

class GradoService:
  @staticmethod
  def crear_grado(grado: Grado):
    GradoRepository.crear_grado(grado)
    return grado

  def buscar_grado(id: int):
    grado = GradoRepository.buscar_grado(id)
    return grado
    
  def actualizar_grado(grado: Grado, id: int):
    GradoRepository.actualizar_grado(grado, id)
    return grado
  
  def eliminar_grado(id: int):
    grado = GradoRepository.eliminar_grado(id)
    
    
    