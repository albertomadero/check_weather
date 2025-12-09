import config
from servicio_clima import ServicioClima
from repository import HistorialRepository

servicio = ServicioClima(config.API_KEY)
repo = HistorialRepository("historial_climas.json")

def mostrar_menu() -> None:
    print("\nMenú:")
    print("1. Mostrar clima de una ciudad")
    print("2. Mostrar historial de consultas")
    print("3. Salir")

def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ciudad = input("Introduce el nombre de la ciudad: ")
            clima = servicio.obtener_clima(ciudad)
            print("\n")

            if clima:
                weather = clima["weather"][0]["description"]
                temp = clima["main"]["temp"] - 273.15
                sensacion = clima["main"]["feels_like"] - 273.15
                humedad = clima["main"]["humidity"]
                print(f"En {ciudad} hay {temp:.2f}°C y {weather}, la humedad es de {humedad} y la sensación terminca es de {sensacion:.2f}°C")
                repo.guardar_consulta(ciudad, temp, weather)
            else:
                print("No se encontró información del clima para la ciudad especificada.")
              
        elif opcion == "2":
            historial = repo.obtener_historial()
            if len(historial) == 0:
                print("\nAún no se tiene un historial")
            else:
                print("\nHistorial de consultas:")
                for consulta in historial:
                    print(f"Ciudad: {consulta['ciudad']}")
                    print(f"Temperatura: {consulta['temp']:.2f}°C")
                    print(f"Clima: {consulta['clima']}")
                    print("-" * 20)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")
        
if __name__ == "__main__":
    main()