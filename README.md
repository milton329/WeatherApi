# 🌦️ Weather Alert Service
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

## ✨ Características

- Consulta la API de [WeatherAPI](https://www.weatherapi.com/) para obtener el clima.
- Detecta condiciones climáticas adversas como tormentas, nieve o niebla.
- Envía notificaciones por correo electrónico a los usuarios afectados.
- Registra las notificaciones en una base de datos SQLite.
- Seguridad mediante API Key.
- Documentación dinámica y visual usando Swagger (OpenAPI).
- Pruebas unitarias con Pytest para asegurar calidad y estabilidad.

## 🛠️ Tecnologías 

- Python 3.10+
- Flask
- Peewee (ORM)
- requests
- smtplib
- SQLite
- flasgger para generar documentación Swagger
- pytest para pruebas unitarias

## ⚙️ Configuración 

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

## 🚀 Instrucciones
### Instalar dependencias 
pip install -r requirements.txt

### Correr pruebas unitarias 
pytest tests -v

### Correr Aplicación 
python app.py

## 📑 Documentación de la API (Swagger)
Utilizamos Swagger a través de la librería flasgger para generar automáticamente la documentación de los endpoints, facilitando pruebas, visualización y entendimiento del API.

- Local: http://localhost:5000/apidocs/

- Producción (Render):
🔐 API Key: milton_1234
🌐 URL: https://weatherapi-x181.onrender.com/apidocs/


## ☁️ Despliegue en la nube
Este proyecto está desplegado en Render, una plataforma de Cloud Hosting similar a AWS, GCP o Heroku, que permite alojar y escalar aplicaciones fácilmente.

## 🔧 Mantenibilidad del Componente

### ✅ Alta mantenibilidad
Gracias al uso de código limpio y una arquitectura desacoplada, cualquier cambio en las fuentes de datos, lógica de alertas o medios de notificación puede realizarse de forma segura y controlada, sin afectar el resto del sistema.

### 🧱 Escalabilidad modular
- Se pueden agregar nuevos tipos de alertas fácilmente, como contaminación ambiental o actividad sísmica.
- Es posible integrar nuevos canales de notificación como correo electrónico, SMS o notificaciones push sin alterar la lógica central.

### 🧪 Testeo facilitado
- Las capas están organizadas y desacopladas para permitir pruebas unitarias e integración automatizadas.
- Se pueden simular distintos escenarios meteorológicos (normales o extremos) sin depender de servicios externos reales.


## 👨‍💻 Autor
Milton Jaramillo
Desarrollador Full Stack
