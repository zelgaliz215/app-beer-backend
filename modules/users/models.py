# Creacion del modelo SQLalchemy para usuarios

from database import db

class User(db.Model):
    # Nombre de la tabla
    __tablename__ = 'users'
    
    # Columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    # Metodo para imprimir el objeto
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }