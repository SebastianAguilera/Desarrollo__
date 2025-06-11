# from marshmallow import Schema, fields, post_load, validate 
# from app.models.universidad import Universidad

# class UniversidadMapping(Schema):
#     id = fields.Integer() #el dump_only=True es para obtener
#     nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) #max de la base de datos
#     sigla = fields.String(required=True, validate = validate.Length(min=1, max=10)) 

# @post_load

# def nueva_universidad(self, data, **kwargs):

#     return Universidad(**data)

# #json discriminan entre valores enteros y strings
# #**kwargs el tercero es tipo clave valor