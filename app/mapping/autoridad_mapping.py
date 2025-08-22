from marshmallow import Schema, fields, post_load, validate 
from app.models.autoridad import Autoridad
from markupsafe import escape

class AutoridadMapping(Schema):
    id = fields.Integer(dump_only=True) 
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))
    cargo = fields.String(required=True, validate = validate.Length(min=1, max=50))
    telefono = fields.String(required=True, validate = validate.Length(min=7, max=20))
    email = fields.Email(required=True, validate = validate.Length(max=100))

    @post_load
    def nueva_autoridad(self, data, **kwargs):
        for key in ['nombre', 'cargo', 'telefono', 'email']:
            if key in data:
                data[key] = escape(data[key])
        return Autoridad(**data)


