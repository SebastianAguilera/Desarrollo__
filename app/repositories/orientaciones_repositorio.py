from app.models import Orientacion
from app import db

class OrientacionRepository:

  @staticmethod
  def crear_facultad(orientacion: Orientacion):
    db.session.add(orientacion)
    db.session.commit()
    return orientacion
  
  @staticmethod
  def buscar_orientacion(id: int) -> Orientacion:
    return db.session.query(Orientacion).filter(Orientacion.id == id).one_or_none()
  
  @staticmethod
  def actualizar_orientacion(orientacion: Orientacion, id: int) -> Orientacion:
    entity = OrientacionRepository.buscar_orientacion(id)
    entity.nombre = orientacion.nombre
    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_facultad(id: int) -> None:
    entity = OrientacionRepository.buscar_orientacion(id)
    db.session.delete(entity)
    db.session.commit()