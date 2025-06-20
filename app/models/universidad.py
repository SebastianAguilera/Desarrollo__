from dataclasses import dataclass
from sqlalchemy.orm import relationship
from app import db

@dataclass(init=False, repr=True, eq=True)
class Universidad(db.Model):
    __tablename__ = 'universidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    sigla = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False)

    facultades = relationship("Facultad", back_populates="universidad")

    