import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    #jwt.init_app(app)

    from app.resources import home, certificado_bp, universidad_bp, cargo_bp, categoria_cargo_bp, materia_bp, autoridad_bp
    
    app.register_blueprint(home, url_prefix="/api/v1")
    app.register_blueprint(certificado_bp, url_prefix="/api/v1")
    app.register_blueprint(universidad_bp, url_prefix="/api/v1")
    app.register_blueprint(cargo_bp, url_prefix="/api/v1")
    app.register_blueprint(categoria_cargo_bp, url_prefix="/api/v1")
    app.register_blueprint(autoridad_bp, url_prefix="/api/v1")
    app.register_blueprint(materia_bp, url_prefix="/api/v1")

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
