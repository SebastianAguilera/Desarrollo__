from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)

class Materia(db.Model):
    __tablename__ = "materias"
    
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre: str = db.Column(db.String(100), nullable = False)
    diseno_curricular: str = db.Column(db.String(100), nullable = False)
    #correlativas: list = db.Column(db.List(), nullable = False)
    horas_dictadas: str =  db.Column(db.String(), nullable = False)
    promocional: bool =  db.Column(db.Boolean(), nullable = False)
    nivel: str =  db.Column(db.String(), nullable = False)
    
    
    
    