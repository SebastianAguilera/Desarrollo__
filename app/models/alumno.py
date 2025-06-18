from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    apellido = db.Column(db.String(100), nullable=False, unique=True)
    nroDocumento = db.Column(db.String(20), nullable=False)
    tipoDocumento = db.Column(db.String(20), nullable=False)
    fechaNacimiento = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    nroLegajo = db.Column(db.Integer, nullable=False, unique=True)
    fechaIngreso = db.Column(db.String(20), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

    #relacion de alumno con notas
    notas = db.relationship("Nota")

