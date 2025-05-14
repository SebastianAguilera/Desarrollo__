from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Alumno():
    nombre : str
    apellido: str
    nroDocumento : str
    tipoDocumento : str
    fechaNacimiento : str
    sexo : str
    nroLegajo : int
    fechaIngreso : str
    carrera : str