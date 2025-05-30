from dataclasses import dataclass
from app import db
from datetime import date;

@dataclass(init=False, repr=True, eq=True)
class Plan:
  __tablename__ = 'planes'
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True , nullable=False)
  nombre: str = db.Column(db.String(100), nullable=False)
  fechaInicio: date = db.Column(db.Date, nullable=False)
  fechaFin : date = db.Column(db.Date, nullable=False)
  observacion: str = db.Column(db.String(100), nullable=False)
