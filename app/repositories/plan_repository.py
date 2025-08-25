from app import db
from app.models import Plan

class PlanRepository:
  @staticmethod
  def crear(plan: Plan) -> Plan:
    db.session.add(plan)
    db.session.commit()
    return plan

  @staticmethod
  def buscar_por_id(id: int) -> Plan | None:
    return db.session.query(Plan).filter_by(id=id).one_or_none()
    
  @staticmethod
  def buscar_todos() -> list[Plan]:
    return db.session.query(Plan).all()
    
  @staticmethod
  def guardar(plan: Plan) -> Plan:
    db.session.commit()
    return plan
  
  @staticmethod
  def borrar_por_id(id: int):
    plan = db.session.query(Plan).filter_by(id=id).first()
    if not plan:
      return None
    db.session.delete(plan)
    db.session.commit()
    return plan
