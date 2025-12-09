
import json
import os

class HistorialRepository:
    def __init__(self, archivo: str):
        self.archivo = archivo

    # Guardar Consulta
    def guardar_consulta(self, cuidad: str, temperatura: float, clima: str) -> None:
        # Recuperar historial previo
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                historial = json.load(f) # Se carga el historial desde el archivo
        else:
            historial = [] # Se inicializa como lista vacía

        # Crear nuevo registro
        nuevo_registro = {
            "cuidad": cuidad,
            "temp": temperatura,
            "clima": clima
        }

        # Agregar nuevo registro al historial
        historial.append(nuevo_registro)

        # Guardar historial actualizado
        with open(self.archivo, "w") as f:
            json.dump(historial, f, indent=4)