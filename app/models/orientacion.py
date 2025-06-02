from dataclasses import dataclass
from app import db  

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
  __tablename__ = 'orientaciones'
  id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  nombre: str = db.Column(db.String(100), nullable=False)