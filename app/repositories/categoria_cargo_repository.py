from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    
  @staticmethod
  def crear_categoria_cargo(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
    db.session.add(categoria_cargo)
    db.session.commit()
    return categoria_cargo
  
  @staticmethod
  def buscar_categoria_cargo_por_id(id: int) -> CategoriaCargo | None:
    return db.session.query(CategoriaCargo).filter_by(id=id).one_or_none()
    
  @staticmethod
  def listar_categorias_cargo() -> list[CategoriaCargo]:
    return db.session.query(CategoriaCargo).all()
  
  @staticmethod
  def guardar_categoria_cargo(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
    categoria_existente = db.session.merge(categoria_cargo)
    db.session.commit()
    return categoria_existente
  
  @staticmethod
  def borrar_por_id(id: int):
    categoria = db.session.query(CategoriaCargo).filter_by(id=id).first()
    if not categoria:
      return None
    db.session.delete(categoria)
    db.session.commit()
    return categoria