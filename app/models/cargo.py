from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):
  __tablename__ = 'cargos'
  id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  nombre: str = db.Column(db.String(100), primary_key=True, nullable=False)
  puntos: int = db.Column(db.Integer, nullable=False)
