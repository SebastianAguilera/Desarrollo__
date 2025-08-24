from marshmallow import fields, Schema, post_load, validate
from app.models.grado import Grado
from markupsafe import escape

class GradoMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))
    
    @post_load 
    
    def nuevo_grado(self, data, **kwargs):
        for key in ['nombre']:
            if key in data:
                data[key] = escape(data[key])
        return Grado(**data)