#!/usr/bin/env bash
# File: install_requirements.sh
# Grant Permisos> chmod +x scripts/install_requirements.sh
# Use: source scripts/install_requirements.sh

# 1) Crear el entorno virtual (si no existe).
if [ ! -d "env" ]; then
    echo "Creando entorno virtual (env)..."
    python -m venv env
fi

# 2) Activar el entorno virtual.
#    En Windows, la carpeta de scripts se llama 'Scripts' en lugar de 'bin'.
#    Para Git Bash, usa la barra normal '/' en lugar de '\'.
echo "Activando el entorno virtual..."
source env/Scripts/activate
echo "Virtual environment activated..."

# 3) Instalar las dependencias desde requirements.txt.
echo "Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Dependencias instaladas con éxito."