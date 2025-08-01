from marshmallow import Schema, fields, post_load, validate 
from app.models.cargo import Cargo
from markupsafe import escape

class CargoMapping(Schema):
    id = fields.Integer(dump_only=True) 
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))  
    puntos = fields.Integer(required=True, validate=validate.Range(min=0))
    categoria_cargo_id = fields.Integer(required=True, load_only=True)  # Este campo es para la relación con CategoriaCargo
    categoria = fields.Nested('CategoriaCargoMapping', only=('id', 'nombre'), dump_only=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        if 'nombre' in data and isinstance(data['nombre'], str):
            data['nombre'] = escape(data['nombre'])
        return Cargo(**data)