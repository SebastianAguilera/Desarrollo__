from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Materia:
    nombre: str
    diseno_curricular: str
    correlativas: list
    horas_dictadas: str
    promocional: bool
    nivel: str
    
    
    
    