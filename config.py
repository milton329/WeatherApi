import os
from peewee import SqliteDatabase
# Conexión global a la base de datos SQLite
db = SqliteDatabase('weather_alerts.db')

class Config:
    # Seguridad para nuestra Api
    API_KEY = os.getenv("API_KEY")

    # Whater Api
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    WEATHER_API_URL = os.getenv('WEATHER_API_URL', 'https://api.weatherapi.com/v1/forecast.json')
    WEATHER_DAYS = int(os.getenv('WEATHER_DAYS', 2))

    # Email
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
