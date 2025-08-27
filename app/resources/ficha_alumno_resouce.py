from flask import Blueprint, send_file
from app.services import AlumnoService

ficha_bp=Blueprint('ficha', __name__)

@ficha_bp.route('/ficha/<int:id>/pdf', methods=['GET'])
def ficha_en_pdf(id: int):
    pdf_io = AlumnoService.generar_ficha_alumno(id, 'pdf')
    return send_file(pdf_io, mimetype='application/pdf', as_attachment=False)