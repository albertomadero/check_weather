import requests
from typing import Optional, Dict, Any

class ServicioClima:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def obtener_clima(self, ciudad: str) -> Optional[Dict[str, Any]]:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={self.api_key}"
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
        else:
            return None

        
        