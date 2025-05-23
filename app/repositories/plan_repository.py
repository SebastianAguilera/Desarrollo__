from app import db
from app.models import Plan

class PlanRepository:
    @staticmethod
    def crear(plan: Plan):
      db.session.add(plan)
      db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):
      return db.session.query(Plan).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
      return db.session.query(Plan).all()
    
    @staticmethod
    def actualizar_Plan(Plan) -> Plan:
      Plan_existente = db.session.merge(Plan)
      if not Plan_existente:
          return None
      return Plan_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Plan:
      Plan = db.session.query(Plan).filter_by(id=id).first()
      if not Plan:
        return None
      db.session.delete(Plan)
      db.session.commit()
      return Plan
