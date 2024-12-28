#!/usr/bin/env bash

# File: install_dependecies.sh
# Description: This script installs necessary dependencies for running the application.
# Grant Permisos> chmod +x scripts/install_dependencies.sh
# Use: source scripts/install_dependencies.sh

# Define the necessary dependencies
dependencies=(
  "flask"
  "flask-cors"
  "flask_sqlalchemy"
  "python-dotenv"
  "mysqlclient"
)

# Funcion para crear el entorno virtual env

if [ ! -d "env" ]; then
  echo "Creating virtual environment..."
  python -m venv env
fi

# Activate the virtual environment

echo "Esperando 5 segundos para continuar..."
sleep 5

source env/Scripts/activate
echo "Virtual environment activated..."

echo "Instalando dependencias con pip..."
# Function to install dependencies
install_dependencies() {
  for dependency in "${dependencies[@]}"; do
    pip install $dependency
  done
}
install_dependencies
echo "Dependencias instaladas con éxito."

pip freeze > requirements.txt
echo "Archivo requirements.txt actualizado."



# Funcion para migrar la base de datos
#migrate_database() {
#  echo "Migrando la base de datos..."
#  flask db upgrade