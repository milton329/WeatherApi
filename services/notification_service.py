"""
@author: Milton Jaramillo  
@since: 07-04-2025  
@summary: Servicio para consultar las notificaciones enviadas a los usuarios. 
"""
from models.notification import Notification

class NotificationService:
    @staticmethod
    def get_notifications_by_email(email: str):
        """
        Consulta las notificaciones previas enviadas a un correo específico.
        :param email: Correo electrónico del usuario (buyer).
        :return: Lista de objetos Notification.
        """
        return list(Notification.select().where(Notification.email == email))