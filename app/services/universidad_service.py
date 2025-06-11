from app.models import Universidad
from app.repositories import UniversidadRepository
class UniversidadService:

  @staticmethod
  def crear_universidad(universidad: Universidad):
    UniversidadRepository.crear_universidad(universidad)
    return universidad

  def buscar_universidad(id: int):
    universidad = UniversidadRepository.buscar_universidad(id)
    return universidad
    
  def actualizar_universidad(universidad: Universidad, id: int):
    UniversidadRepository.actualizar_universidad(universidad, id)
    return universidad
  
  def eliminar_universidad(id: int):
    universidad= UniversidadRepository.eliminar_universidad(id)