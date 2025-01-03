from flask import Flask
from flask_cors import CORS

from config import Config
from flask_sqlalchemy import SQLAlchemy
from database import db  # Importar el objeto db definido en database.py


# Funcion para crear instancia de la aplicación
def create_app(config_class = Config):
    # Crear instancia de la aplicacion Flask con el nombre de la aplicacion (__name__) y el contexto (__main__)
    app = Flask(__name__)
    # Configuracion de la aplicacion
    app.config.from_object(config_class)
    
    # Inicializacion de la bd con la app
    db.init_app(app)

    # Middleware
    # Cors
    CORS(app)

    # Importar Blueprintst de cada modulo 
    from modules.users.routes import users_bp
    
    # Registrar blueprints
    app.register_blueprint(users_bp, url_prefix='/api/users')
    
    # Lista de rutas registradas
    print(app.url_map)
    return app

# Observa que aquí no hay modelos ni nada que dependa directamente de un import de app. Esto evita conflictos y hace el código más limpio.  