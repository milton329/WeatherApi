"""
@author: Milton Jaramillo
@since: 07-04-2025
@summary: Servicio principal encargado de procesar las alertas meteorológicas. 
Consulta el pronóstico del clima para una ubicación dada y, si se detectan condiciones 
climáticas adversas, envía una notificación por correo electrónico al comprador 
y registra la alerta en la base de datos. Este servicio es el corazón del reto de Meli, 
donde combinamos APIs, lógica de negocio y persistencia para cuidar la experiencia del cliente.
"""

import requests
import smtplib
from email.mime.text import MIMEText
from config import Config
from utils.exceptions import WeatherAPIException
from models.forecast import Forecast
from models.notification import Notification
from datetime import datetime
from utils.weather_translations import translate_condition_by_code


class WeatherAlertService:
    """
    Servicio encargado de procesar alertas meteorológicas y enviar notificaciones al comprador.

    BAD_WEATHER_CODES: conjunto de códigos de WeatherAPI que representan condiciones climáticas adversas
    como tormentas eléctricas, lluvias intensas, nieve, niebla espesa, entre otros. 
    Estos códigos se utilizan para determinar cuándo debe enviarse una alerta.

    Códigos incluidos más comunes:
    1063	Posible lluvia
    1066	Nieve ligera
    1069	Lluvia con aguanieve ligera
    1072	Llovizna helada ligera
    1087	Tormenta eléctrica aislada
    1114	Blowing snow (nieve ventosa)
    1117	Tormenta de nieve severa
    1135	Niebla
    1147	Niebla congelante
    1180-1246	Lluvias de distintas intensidades y tormentas eléctricas
    1255-1282	Nieve, granizo, ventiscas y otras formas severas

    Fuente: https://www.weatherapi.com/docs/
    """

    BAD_WEATHER_CODES = {1063, 1066, 1069, 1072, 1087, 1114, 1117, 1135, 1147, 1150,
                         1153, 1168, 1171, 1180, 1183, 1186, 1189, 1192, 1195, 1198,
                         1201, 1204, 1207, 1210, 1213, 1216, 1219, 1222, 1225, 1237,
                         1240, 1243, 1246, 1249, 1252, 1255, 1258, 1261, 1264, 1273,
                         1276, 1279, 1282}

    def process_forecast(self, lat, lon, email):
        forecast = self._get_weather_forecast(lat, lon)

        if forecast.code in self.BAD_WEATHER_CODES:
            self._send_email_alert(email, forecast)
            
            # Guardar notificación en BD
            Notification.create(
                email=email,
                latitude=lat,
                longitude=lon,
                condition=forecast.condition,
                code=forecast.code
            )

            return {
                "alert_sent": True,
                "message": f"Alerta enviada: clima {forecast.condition} en camino.",
                "forecast": forecast.to_dict()
            }
        else:
            return {
                "alert_sent": False,
                "message": "No hay clima severo en la zona.",
                "forecast": forecast.to_dict()
            }

    def _get_weather_forecast(self, lat, lon):
        params = {
            'key': Config.WEATHER_API_KEY,
            'q': f"{lat},{lon}",
            'days': Config.WEATHER_DAYS
        }

        response = requests.get(Config.WEATHER_API_URL, params=params)

        if response.status_code != 200:
            raise WeatherAPIException("Error consultando el clima")

        data = response.json()
        forecast_day = data["forecast"]["forecastday"][0]["day"]
        condition = forecast_day["condition"]

        return Forecast(
            code=condition["code"],
            condition=condition["text"],
            date=data["forecast"]["forecastday"][1]["date"]
        )

    def _send_email_alert(self, to_email, forecast):
        condition_es = translate_condition_by_code(forecast.code)
        msg = MIMEText(
            f"Hola!\n\nTenemos programada la entrega de tu paquete para mañana, "
            f"y se espera un clima con {condition_es} en tu ubicación. "
            "Es posible que tengamos retrasos. Haremos todo lo posible para cumplir con tu entrega.\n\n"
            f"Fecha del clima: {forecast.date}"
        )
        msg['Subject'] = '⚠️ Posible retraso en tu entrega por condiciones climáticas'
        msg['From'] = Config.MAIL_USERNAME
        msg['To'] = to_email

        try:
            server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
            if Config.MAIL_USE_TLS:
                server.starttls()
            server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            server.sendmail(Config.MAIL_USERNAME, to_email, msg.as_string())
            server.quit()
        except Exception as e:
            raise WeatherAPIException(f"Error enviando el correo: {e}")
