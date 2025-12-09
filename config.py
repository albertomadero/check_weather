import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener la clave de manera segura
API_KEY = os.getenv("API_KEY")