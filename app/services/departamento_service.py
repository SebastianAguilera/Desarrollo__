from app.models import Departamento
from app.repositories.departamento_repositorio import DepartamentoRepository

class DepartamentoService:
  @staticmethod
  def crear_departamento(departamento: Departamento):
    DepartamentoRepository.crear_departamento(departamento)
    return departamento

  def buscar_departamento(id: int):
    departamento = DepartamentoRepository.buscar_departamento(id)
    return departamento
    
  def actualizar_departamento(departamento: Departamento, id: int):
    DepartamentoRepository.actualizar_departamento(departamento, id)
    return departamento
  
  def eliminar_departamento(id: int):
    departamento = DepartamentoRepository.eliminar_departamento(id)
    
  