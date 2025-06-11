from app.models import Alumno
from app.repositories import AlumnoRepository
class AlumnoService:

  @staticmethod
  def crear_alumno(alumno: Alumno):
    AlumnoRepository.crear_alumno(alumno)
    return alumno

  def buscar_alumno(id: int):
    alumno = AlumnoRepository.buscar_alumno(id)
    return alumno
    
  def actualizar_alumno(alumno: Alumno, id: int):
    AlumnoRepository.actualizar_alumno(alumno, id)
    return alumno
  
  def eliminar_alumno(id: int):
    alumno = AlumnoRepository.eliminar_alumno(id)