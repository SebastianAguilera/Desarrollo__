from app.models import Grupo
from app import db

class GrupoRepository:

    @staticmethod
    def crear_grupo(grupo: Grupo):
        db.session.add(grupo)
        db.session.commit()
        return grupo
    
    @staticmethod
    def buscar_grupo(id: int) ->Grupo:
        return db.session.query(Grupo).filter(Grupo.id ==id).one_or_none()
    
    @staticmethod
    def actualizar_grupo(grupo: Grupo, id: int) ->Grupo:
        entity= GrupoRepository.buscar_grupo(id)
        entity.nombre = grupo.nombre
        db.session.commit()
        return entity
    
    @staticmethod
    def eliminar_grupo(id: int) -> None:
        entity = GrupoRepository.buscar_grupo(id)
        db.session.delete(entity)
        db.session.commit()
        


