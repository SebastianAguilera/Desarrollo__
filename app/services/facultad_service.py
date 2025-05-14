from app.models import Facultad
from app.repositories import FacultadRepository
class FacultadService:

  @staticmethod
  def crear_facultad(facultad: Facultad):
    FacultadRepository.crear_facultad(facultad)
    
    