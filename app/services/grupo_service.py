from app.models import Grupo
from app.repositories import GrupoRepository

class GrupoService:

    @staticmethod
    def crear_grupo(grupo: Grupo):
        GrupoRepository.crear_grupo(grupo)
        return grupo

    def buscar_grupo(id: int):
        grupo = GrupoRepository.buscar_grupo(id)
        return grupo

    def actualizar_grupo(grupo: Grupo, id: int):
        GrupoRepository.actualizar_grupo(grupo, id)
        return grupo

    def eliminar_grupo(id: int):
        return GrupoRepository.eliminar_grupo(id)


