# Import de la clase que configura el app
from config import Config
# Import de la clase que crea la aplicacion
from app import create_app
# Import de la clase que crea la base de datos en SQlAlchemy
from database import db
# Import de de modelos necesarios para crear las tablas
from modules.users.models import User


# Crear instancia de la aplicacion con la configuracion de entorno
app = create_app(Config)

with app.app_context():
    db.drop_all()    
    # Crear las tablas en la base de datos
    db.create_all()
    # Crear un usuario de prueba
    print ("Tablas creadas exitosamente")

