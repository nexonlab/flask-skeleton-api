#!/bin/bash
echo "Instalando pacotes de requirements.txt necessarios a aplicacao {{cookiecutter.app_name}}..."
pip install -r requirements.txt
echo "Iniciando aplicacao..."
waitress-serve --call --listen=0.0.0.0:5000 app:create_app