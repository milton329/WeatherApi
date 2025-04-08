"""
@author: Milton Jaramillo  
@since: 07-04-2025  
@summary: Este proyecto forma parte del reto técnico de MELI, y representa no solo un desafío profesional, sino también personal.  
          Es una API construida con Flask, que integra autenticación mediante API Key, uso de variables de entorno y enrutamiento modular.    
          Este reto es una oportunidad para demostrar no solo habilidades técnicas, sino también carácter, disciplina y amor por lo que hago.  
          ¡Vamos Milton! MELI es solo el comienzo :)
"""
from flask import Flask
from flasgger import Swagger
from routes import weather_router
from config import Config
from dotenv import load_dotenv
import os
from config import db
from models.notification import Notification

# Creo mi BD para poder registrar todas las notificaciones
with db:
    db.create_tables([Notification])

# Cargar variables de entorno
load_dotenv()

# Crear app Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar Swagger
swagger = Swagger(app)

# Registrar blueprint
app.register_blueprint(weather_router)

# Correr la app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
