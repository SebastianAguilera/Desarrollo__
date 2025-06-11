from app.models import Plan
from app.repositories import PlanRepository
class PlanService:
  
  @staticmethod
  def crear_plan(plan : Plan) -> Plan:
    return PlanRepository.crear_plan(plan)
  
  @staticmethod
  def buscar_plan_por_id(id: int) -> Plan | None:
    return PlanRepository.buscar_plan_por_id(id)

  @staticmethod
  def listar_planes() -> list[Plan]:
    return PlanRepository.listar_planes()
  
  @staticmethod
  def actualizar_plan(id: int, plan: Plan) -> Plan | None:
    plan_existente = PlanRepository.buscar_plan_por_id(id)
    if not plan_existente:
      return None
    plan_existente.nombre = plan.nombre
    plan_existente.fechaInicio = plan.fechaInicio
    plan_existente.fechaFin = plan.fechaFin
    plan_existente.observacion = plan.observacion
    plan_actualizado = PlanRepository.guardar_plan(plan_existente)
    return plan_actualizado
  
  @staticmethod
  def borrar_por_id(id: int):
    return PlanRepository.borrar_por_id(id)