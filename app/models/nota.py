from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Nota(db.Model): 
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  alumno_id: int 
  materia_id: int 
  autoridad_id: int
  nota: float

  #materia_id : int = db.Column(db.Integer, db.ForeignKey('materias.id'))