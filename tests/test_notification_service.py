import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.notification_service import NotificationService

def test_get_notifications_by_email_simple():
    """
    @summary: Prueba unitaria  para verificar que el método 
    'get_notifications_by_email' devuelve una lista de notificaciones válidas 
    para un correo existente.
    """
    email = 'giovanny329614@gmail.com'

    notifications = NotificationService.get_notifications_by_email(email)

    assert isinstance(notifications, list)

    if notifications:
        n = notifications[0]
        assert hasattr(n, 'sent_at')
        assert hasattr(n, 'latitude')
        assert hasattr(n, 'longitude')
        assert hasattr(n, 'condition')
        assert hasattr(n, 'code')

