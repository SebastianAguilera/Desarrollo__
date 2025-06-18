from flask import render_template
from app.models import Alumno
from app.services import FacultadService, EspecialidadService
from app.repositories import AlumnoRepository
from datetime import datetime

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

  def generar_certificado_alumno_regular(id: int): 
    alumno = AlumnoRepository.buscar_alumno(id)
    #TODO: relacionar alumno con facultad y especialidad 
    facultad = FacultadService.buscar_facultad(19)
    fecha = datetime.now()
    especialidad = EspecialidadService.buscar_especialidad(5)
    return render_template("certificado/certificado.html", alumno=alumno, facultad=facultad, fecha=fecha, especialidad=especialidad)


