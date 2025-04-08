import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from services.weather_service import WeatherAlertService
from models.forecast import Forecast

class TestWeatherAlertService(unittest.TestCase):
    @patch('services.weather_service.WeatherAlertService._get_weather_forecast')
    @patch('services.weather_service.WeatherAlertService._send_email_alert')
    def test_bad_weather_triggers_email(self, mock_send_email, mock_get_forecast):
        """
        Objetivo de esta prueba:
        Verificar que el sistema **envíe un correo de alerta** cuando se detecta mal clima.

        ¿Qué se simula aquí?
        - Se finge que la API devuelve un clima severo (código 1276).
        - Se simula también el envío de correo para no hacer un envío real.

        ¿Qué se espera?
        - Que se haya enviado el correo (verificamos que el método fue llamado).
        - Que el mensaje de respuesta indique que hubo clima severo.
        """
        service = WeatherAlertService()

        mock_get_forecast.return_value = Forecast(
            code=1276,
            condition='Heavy Rain',
            date='2025-04-08'
        )

        response = service.process_forecast('10.0000', '-84.0000', 'usuario@correo.com')

        self.assertTrue(response['alert_sent'])
        self.assertIn('clima', response['message'])
        mock_send_email.assert_called_once()

    @patch('services.weather_service.WeatherAlertService._get_weather_forecast')
    def test_good_weather_no_email(self, mock_get_forecast):
        """
        Objetivo de esta prueba:
        Verificar que **no se envíe ninguna alerta** cuando el clima está bien.

        ¿Qué se simula aquí?
        - Se simula un clima soleado (código 1000).

        ¿Qué se espera?
        - Que no se haya enviado ninguna alerta.
        - Que el mensaje indique que no hay clima severo.
        """
        service = WeatherAlertService()

        mock_get_forecast.return_value = Forecast(
            code=1000,
            condition='Sunny',
            date='2025-04-08'
        )

        response = service.process_forecast('10.0000', '-84.0000', 'usuario@correo.com')

        self.assertFalse(response['alert_sent'])
        self.assertIn('No hay clima severo', response['message'])

if __name__ == '__main__':
    unittest.main()
