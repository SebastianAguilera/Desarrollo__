from marshmallow import Schema, fields, post_load, validate 
from app.models.alumno import Alumno



class AlumnoMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) #max de la base de datos
    apellido = fields.String(required=True, validate = validate.Length(min=1, max=100))
    nroDocumento = fields.String(required=True, validate= validate.Length(min=1, max=100))
    tipoDocumento = fields.String( required=True, validate= validate.Length(min=1, max=100))
    fechaNacimiento = fields.String(required= True, validate= validate.Length(min=1, max=100))
    sexo = fields.String(required= True, validate=validate.Length(min=1, max=100))
    nroLegajo = fields.Int(required=True)
    fechaIngreso = fields.String(required=True, validate=validate.Length(min=1,max=100))
    carrera = fields.String(required=True, validate=validate.Length(min=1,max=100))

    usuario_id = fields.Int(required=False, allow_none=True)
    universidad_id = fields.Int(required=False, allow_none=True)
    especialidad_id = fields.Int(required=False, allow_none=True)


    @post_load
    def nueva_alumno(self, data, **kwargs):
       return Alumno(**data)
    