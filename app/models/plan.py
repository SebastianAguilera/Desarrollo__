from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
  __tablename__ = 'planes'
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True , nullable=False)
  nombre: str = db.Column(db.String(100), nullable=False)
  fechaInicio: str = db.Column(db.String, nullable=False)
  fechaFin : str = db.Column(db.String, nullable=False)
  observacion: str = db.Column(db.String(100), nullable=False)

 



