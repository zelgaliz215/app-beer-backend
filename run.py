# Punto de entrada de la app
from app import create_app
from config import Config

#Instancia de la app y configuracion
app = create_app(Config)

# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)