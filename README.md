# Weather Alert Service ---------------------------------

Este proyecto es un servicio REST desarrollado con Flask que consulta el pronóstico del clima para una ubicación específica y envía alertas por correo electrónico si se detectan condiciones meteorológicas adversas.

## Características --------------------------------------

- Consulta la API de [WeatherAPI](https://www.weatherapi.com/) para obtener el clima.
- Detecta condiciones climáticas adversas como tormentas, nieve o niebla.
- Envía notificaciones por correo electrónico a los usuarios afectados.
- Registra las notificaciones en una base de datos SQLite.
- Seguridad mediante API Key.

## Tecnologías ------------------------------------------

- Python 3.10+
- Flask
- Peewee (ORM)
- requests
- smtplib
- SQLite

## Configuración ----------------------------------------

## Variables de entorno (`.env`)
Debes crear un archivo `.env` con las siguientes variables:
API_KEY=milton_1234
WEATHER_API_KEY=83b7c8c1fa89489fa81224129240506
WEATHER_API_URL=http://api.weatherapi.com/v1/forecast.json
WEATHER_DAYS=2
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=Correo para el envio de notificaciones
MAIL_PASSWORD=Clave de la aplicación de GMail.
MAIL_USE_TLS=True

## Instalar dependencias ---------------------------------
pip install -r requirements.txt

## Correr pruebas unitarias ------------------------------
pytest tests -v

## Correr Aplicación -------------------------------------
python app.py

## Documentación Swagger (Aquí esta todo para saber como funcionan los endpoint)
http://localhost:5000/apidocs/

