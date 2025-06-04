from app import db
from app.models import Cargo

class CargoRepository:
  @staticmethod
  def crearCargo(cargo: Cargo) -> Cargo:
    db.session.add(cargo)
    db.session.commit()
    return cargo

  @staticmethod
  def buscar_cargo_por_id(id: int) -> Cargo | None:
    return db.session.query(Cargo).filter_by(id=id).one_or_none()
    
  @staticmethod
  def listar_cargo() -> list[Cargo]:
    return db.session.query(Cargo).all()
    
  @staticmethod
  def guardar_cargo(cargo: Cargo) -> Cargo:
    cargo_existente = db.session.merge(cargo)
    db.session.commit()
    return cargo_existente
  
  @staticmethod
  def borrar_por_id(id: int) -> Cargo | None:
    cargo = db.session.query(Cargo).filter_by(id=id).first()
    if not cargo:
      return None
    db.session.delete(cargo)
    db.session.commit()
    return cargo
