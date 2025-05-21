from app import db
from app.models import Autoridad


#a parte del CRUD tiene consultas a la base de datos

class AutoridadRepository:
    def crear(autoridad: db.Model):
        "crea una nnueva autoridad en la base de datos"
        
        db.session.add(autoridad)
        db.session.commit()
        
        