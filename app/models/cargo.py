from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):
    __tablename__ = 'cargos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre: str = db.Column(db.String(100), nullable=False)
    puntos: int = db.Column(db.Integer, nullable=False)
    categoria_cargo_id: int = db.Column(db.Integer, db.ForeignKey('categorias_cargo.id'), nullable=False)

    categoria = db.relationship('CategoriaCargo', back_populates='cargos', lazy='joined')
