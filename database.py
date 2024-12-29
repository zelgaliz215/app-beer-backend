# backend/database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Si tuvieras otras extensiones, podrías declararlas aquí, por ejemplo:
# migrate = Migrate()
# login_manager = LoginManager()
# etc.


# > No se hace `db = SQLAlchemy(app)` directamente, para evitar dependencias con la aplicación. Así evitamos imports circulares.