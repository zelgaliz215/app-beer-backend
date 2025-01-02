# Modulo de configuracion de la aplicacion
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Clase de configuracion de la aplicacion
class Config:
    # Configuracion de la aplicacion
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    
    # Configuracion de la base de datos por defecto
    DB_TYPE = os.getenv('DB_TYPE', 'sqlite')
    
    if DB_TYPE == 'mysql':
        # Configuracion de la base de datos MySQL para produccion
        MYSQL_USER = os.getenv('MYSQL_USER', 'root')
        MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'daniel')
        MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
        MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'beer_db')
        # Conexion de SQLAlchem
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
        
    else:
        # Configuracion de la base de datos SQLite
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        # Conexion de SQLAlchem
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'beer_dev.db')}"

    # Opciones de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False