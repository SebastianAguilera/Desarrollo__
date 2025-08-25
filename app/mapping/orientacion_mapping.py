from marshmallow import fields, Schema, post_load, validate
from app.models.orientacion import Orientacion
from markupsafe import escape

class OrientacionMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nueva_orientacion(self, data, **kwargs):
        for key in ['nombre']:
            if key in data:
                data[key] = escape(data[key])
        return Orientacion(**data)
    
 