from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Plan:
  nombre: str
  fechaInicio: str
  fechaFin : str
  observacion: str
