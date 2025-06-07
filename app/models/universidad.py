from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Universidad():
    __tablename__ = 'universidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    sigla = db.Column(db.String(10), nullable=False, unique=True)
    