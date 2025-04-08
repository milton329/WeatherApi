class WeatherAPIException(Exception):
    """Excepción personalizada para errores relacionados con la API del clima."""
    def __init__(self, message="Error en la API del clima"):
        super().__init__(message)
