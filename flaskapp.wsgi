import sys
import os

# Asegura que tu app esté en el path
sys.path.insert(0, '/var/www/html/sti-p')

# Importa la app de Flask
from flaskapp import app as application

# Opcional
application.secret_key = 'stip'