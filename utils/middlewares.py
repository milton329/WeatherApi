from flask import request, jsonify, current_app
from functools import wraps

def require_api_key(f):
    """
    @author: Milton Jaramillo  
    @since: 07-04-2025  
    @summary:Verifica que la solicitud tenga una API key válida en el header 'x-api-key'.
    Devuelve error 401 si no se envía la clave.
    Devuelve error 403 si la clave es incorrecta.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key:
            return jsonify({"error": "API key requerida"}), 401
        if api_key != current_app.config['API_KEY']:
            return jsonify({"error": "API key inválida"}), 403
        return f(*args, **kwargs)
    return decorated

