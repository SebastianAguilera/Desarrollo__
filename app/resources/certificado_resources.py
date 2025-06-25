from flask import Blueprint
from services import AlumnoService

certificado_bp=Blueprint('certificado', __name__)
@certificado_bp.route('certificado/<int:id>/pdf')
def reporte_pdf(id:int):
    return AlumnoService.generar_certificado_alumno_regular(id)




