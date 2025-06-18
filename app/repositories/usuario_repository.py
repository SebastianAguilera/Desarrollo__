from app.models import Usuario
from app import db 

class UsuarioRepository():
  @staticmethod
  def guardar_usuario(usuario: Usuario):
    db.session.add(usuario)
    db.session.commit()
    return usuario