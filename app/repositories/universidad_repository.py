from app.models import Universidad
from app import db


class UniversidadRepository:

  @staticmethod
  def crear_facultad(Universidad: Universidad) -> Universidad:
    db.session.add(universidad)
    db.session.commit()
    return universidad
  
  @staticmethod
  def buscar_universidad(id: int) -> Universidad:
    return db.session.query(Universidad).filter(Universidad.id == id).one_or_none()
  
  @staticmethod
  def actualizar_universidad(universidad: Universidad, id: int) -> Universidad:
    entity = UniversidadRepository.buscar_universidad(id)
    entity.nombre = universidad.nombre

    entity.sigla = universidad.sigla
    entity.tipo = universidad.tipo
    entity.anioFundacion = universidad.anioFundacion
    entity.direccion = universidad.direccion
    entity.telefono = universidad.telefono  
    entity.email = universidad.email
  


    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_universidad(id: int) -> None:
    entity = UniversidadRepository.buscar_universidad(id)
    db.session.delete(entity)
    db.session.commit()