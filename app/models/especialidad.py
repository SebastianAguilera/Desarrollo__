from dataclasses import dataclass
from app import db

class Especialidad(db.Model):
    __tablename__ = 'especialidades'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(100), nullable=False)
    observacion = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Especialidad {self.id}: {self.nombre}>"

