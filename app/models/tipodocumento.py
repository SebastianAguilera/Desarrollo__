from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class TipoDocumento:
  DNI: int
  libretacivica: str
  libretaenrolamiento: str
  pasaporte: str
