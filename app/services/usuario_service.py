from app.models import Usuario
from app.repositories import UsuarioRepository

class UsuarioService:
  @staticmethod
  def guardar_usuario(usuario):
    usuario_guardado = UsuarioRepository.guardar_usuario(usuario)
    return usuario_guardado