from app import db
from app.models import Plan

class PlanRepository:
  @staticmethod
  def crear_plan(plan: Plan) -> Plan:
    db.session.add(plan)
    db.session.commit()
    return plan

  @staticmethod
  def buscar_plan_por_id(id: int) -> Plan | None:
    return db.session.query(Plan).filter_by(id=id).one_or_none()
    
  @staticmethod
  def listar_planes() -> list[Plan]:
    return db.session.query(Plan).all()
    
  @staticmethod
  def guardar_plan(plan: Plan) -> Plan:
    plan_existente = db.session.merge(plan)
    db.session.commit()
    return plan_existente
  
  @staticmethod
  def borrar_por_id(id: int):
    plan = db.session.query(Plan).filter_by(id=id).first()
    if not plan:
      return None
    db.session.delete(plan)
    db.session.commit()
    return plan
