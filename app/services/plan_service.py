from app.models import Plan
from app.repositories import PlanRepository
class PlanService:
  
  @staticmethod
  def crear_plan(plan : Plan) -> Plan:
    PlanRepository.crear_plan(plan)
    return plan
  
  @staticmethod
  def buscar_plan_por_id(id: int) -> Plan | None:
    plan = PlanRepository.buscar_plan_por_id(id)
    return plan

  @staticmethod
  def listar_planes() -> list[Plan]:
    planes = PlanRepository.listar_planes()
    return planes
  
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
  def borrar_por_id(id: int) -> Plan | None:
    eliminar_plan = PlanRepository.borrar_por_id(id)
    return eliminar_plan