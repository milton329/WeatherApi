# Weather Alert Service 

Este proyecto es un servicio REST desarrollado con Flask que consulta el pronóstico del clima para una ubicación específica y envía alertas por correo electrónico si se detectan condiciones meteorológicas adversas.

## 🗂️ Estructura del Proyecto

- app.py
- config.py
- routes.py
- weather_alerts.db
- requirements.txt
- .env
- .gitignore
- README.md
- models/
- -  forecast.py
- -  notification.py
-  services/
- -  weather_service.py
- -  notification_service.py
-  utils/
- -  exceptions.py
- -  middlewares.py
- tests/
- -  test_weather_service.py
- -  test_notification_service.py

## Características 

- Consulta la API de [WeatherAPI](https://www.weatherapi.com/) para obtener el clima.
- Detecta condiciones climáticas adversas como tormentas, nieve o niebla.
- Envía notificaciones por correo electrónico a los usuarios afectados.
- Registra las notificaciones en una base de datos SQLite.
- Seguridad mediante API Key.

## Tecnologías 

- Python 3.10+
- Flask
- Peewee (ORM)
- requests
- smtplib
- SQLite

## Configuración 

### Variables de entorno (`.env`)
Debes crear un archivo `.env` con las siguientes variables:
- API_KEY=milton_1234
- WEATHER_API_KEY=83b7c8c1fa89489fa81224129240506
- WEATHER_API_URL=http://api.weatherapi.com/v1/forecast.json
- WEATHER_DAYS=2
- MAIL_SERVER=smtp.gmail.com
- MAIL_PORT=587
- MAIL_USERNAME=Correo_para_el_envio_de_notificaciones
- MAIL_PASSWORD=Clave_de_la_aplicacion_de_GMail
- MAIL_USE_TLS=True

## Instalar dependencias 
pip install -r requirements.txt

## Correr pruebas unitarias 
pytest tests -v

## Correr Aplicación 
python app.py

## Documentación local Swagger (Aquí esta todo para saber como funcionan los endpoint)
http://localhost:5000/apidocs/

## Aplicación en AWS funcional Producción
API_KEY=milton_1234 << -- Con esta clave el endpoint de producción te funcionara

- Servicio desplegado en Render:
Render es una plataforma de Cloud Hosting (alojamiento en la nube) como AWS, GCP, o Heroku.

- Api 
https://weatherapi-x181.onrender.com/apidocs/


## 👨‍💻 Autor
Milton Jaramillo
Desarrollador Full Stack
