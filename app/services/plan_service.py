from app.models import Plan
from app.repositories import PlanRepository
class PlanService:
  
  @staticmethod
  def crear(plan : Plan) -> Plan:
    return PlanRepository.crear(plan)
  
  @staticmethod
  def buscar_por_id(id: int) -> Plan | None:
    return PlanRepository.buscar_por_id(id)

  @staticmethod
  def buscar_todos() -> list[Plan]:
    return PlanRepository.buscar_todos()
  
  @staticmethod
  def actualizar(id: int, plan: Plan) -> Plan | None:
    plan_existente = PlanRepository.buscar_por_id(id)
    if not plan_existente:
      return None
    plan_existente.nombre = plan.nombre
    plan_existente.fechaInicio = plan.fechaInicio
    plan_existente.fechaFin = plan.fechaFin
    plan_existente.observacion = plan.observacion
    return plan_existente
  
  @staticmethod
  def borrar_por_id(id: int):
    return PlanRepository.borrar_por_id(id)