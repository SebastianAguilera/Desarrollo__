from dataclasses import dataclass
from app import db

@dataclass
class Autoridad(db.Model):
    __tablename__ = "autoridades"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    cargo: str = db.Column(db.String(100), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(100), nullable=False)

  #muchas autoridades tienen un cargo