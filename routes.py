from flask import Blueprint, request, jsonify
from services.weather_service import WeatherAlertService
from services.notification_service import NotificationService
from utils.exceptions import WeatherAPIException
from flasgger.utils import swag_from
from utils.middlewares import require_api_key

weather_router = Blueprint('weather', __name__)
alert_service = WeatherAlertService()

@weather_router.route('/check_weather', methods=['POST'])
@swag_from({
    'tags': ['Weather'],
    'description': """
        Este endpoint recibe una ubicación geográfica (latitud y longitud) y una dirección de correo electrónico.  
        Consulta el clima actual y si se detecta mal tiempo (lluvia fuerte, tormentas, etc.), se enviará una alerta al correo proporcionado.  
        Ideal para prevenir riesgos y estar preparado.  
        ¡Milton está construyendo una API de clima con corazón!
    """,
    'parameters': [
        {
            'name': 'x-api-key',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Clave API de autenticación'
        },
        {
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'latitude': {
                    'type': 'number',
                    'example': 5.07,
                    'description': 'Latitud del lugar a consultar'
                },
                'longitude': {
                    'type': 'number',
                    'example': -75.52,
                    'description': 'Longitud del lugar a consultar'
                },
                'email': {
                    'type': 'string',
                    'example': 'correo@correo.com',
                    'description': 'Correo para recibir alertas'
                }
            },
            'required': ['latitude', 'longitude', 'email']
        }
    }
    ],
    'responses': {
        200: {
            'description': 'Pronóstico exitoso',
            'schema': {
                'type': 'object',
                'properties': {
                    'forecast': {
                        'type': 'string',
                        'example': 'Soleado con 25°C'
                    }
                }
            }
        },
        401: {
            'description': 'Falta la API key',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'API key requerida'
                    }
                }
            }
        }
    }
})
@require_api_key
def check_weather():
    try:
        data = request.get_json()
        lat = data.get('latitude')
        lon = data.get('longitude')
        email = data.get('email')

        if not lat or not lon or not email:
            return jsonify({'error': 'latitude, longitude y email son requeridos'}), 400

        result = alert_service.process_forecast(lat, lon, email)
        return jsonify(result), 200

    except WeatherAPIException as e:
        return jsonify({'error': str(e)}), 502
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500


@weather_router.route('/notifications', methods=['GET'])
@swag_from({
    'tags': ['Weather'],
    'description': """
        Consulta las notificaciones climáticas enviadas previamente a un correo electrónico.  
        Retorna el historial de alertas con información sobre la fecha, condición climática, código de condición y ubicación.  
        Ideal para visualizar el historial de alertas relacionadas al clima que ha recibido un usuario.
    """,
    'parameters': [
        {
            'name': 'x-api-key',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Clave API de autenticación'
        },
        {
            'name': 'email',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Correo electrónico del usuario que recibió las notificaciones'
        }
    ],
    'responses': {
        200: {
            'description': 'Historial de notificaciones encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'notifications': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'sent_at': {'type': 'string', 'example': '2025-04-07 10:00:00'},
                                'latitude': {'type': 'number', 'example': 5.07},
                                'longitude': {'type': 'number', 'example': -75.52},
                                'condition': {'type': 'string', 'example': 'Heavy Rain'},
                                'code': {'type': 'integer', 'example': 1195}
                            }
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Falta el parámetro email',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'El parámetro email es requerido'}
                }
            }
        },
        401: {
            'description': 'Falta la API key',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'API key requerida'}
                }
            }
        },
        404: {
            'description': 'No se encontraron notificaciones',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'No se encontraron notificaciones para correo@ejemplo.com'}
                }
            }
        }
    }
})
@require_api_key
def get_notifications():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'El parámetro email es requerido'}), 400

    notifications = NotificationService.get_notifications_by_email(email)

    if not notifications:
        return jsonify({'message': f'No se encontraron notificaciones para {email}'}), 404

    data = []
    for n in notifications:
        data.append({
            'sent_at': n.sent_at.strftime('%Y-%m-%d %H:%M:%S'),
            'latitude': n.latitude,
            'longitude': n.longitude,
            'condition': n.condition,
            'code': n.code
        })

    return jsonify({'notifications': data}), 200


