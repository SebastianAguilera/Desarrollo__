from dataclasses import dataclass


@dataclass(init=False, repr=True, eq=True)
class Nota:
  alumno_id: int
  materia_id: int
  autoridad_id: int
  nota: float