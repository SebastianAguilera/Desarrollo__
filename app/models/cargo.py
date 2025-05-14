from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Cargo:
  nombre: str
  puntos: int
