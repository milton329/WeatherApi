"""
@author: Milton Jaramillo
@since: 07-04-2025
@summary: Modelo de base de datos para almacenar las notificaciones enviadas por la API.
"""

from peewee import Model, CharField, FloatField, IntegerField, DateTimeField
from config import db
import datetime

class Notification(Model):
    email = CharField()                 # Correo del buyer
    latitude = FloatField()             # Latitud de la ubicación consultada
    longitude = FloatField()            # Longitud de la ubicación consultada
    condition = CharField()             # Condición climática (ej: Heavy Rain)
    code = IntegerField()               # Código del clima
    sent_at = DateTimeField(default=datetime.datetime.now)  # Fecha/hora de la notificación

    class Meta:
        database = db                  # Conecta con la base de datos declarada en config.py
