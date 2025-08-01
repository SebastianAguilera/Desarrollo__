from marshmallow import Schema, fields, post_load, validate 
from app.models.categoria_cargo import CategoriaCargo
from markupsafe import escape

class CategoriaCargoMapping(Schema):
    id = fields.Integer(dump_only=True)  # El dump_only=True es para obtener el ID al serializar
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) #max de la base de datos

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        if 'nombre' in data and isinstance(data['nombre'], str):
            data['nombre'] = escape(data['nombre'])
        return CategoriaCargo(**data)


#json discriminan entre valores enteros y strings
#**kwargs el tercero es tipo clave valor