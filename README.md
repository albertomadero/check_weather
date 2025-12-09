# 🌤️ Consultor de Clima

Una aplicación de línea de comandos (CLI) moderna y robusta en Python para consultar el clima en tiempo real.

## 🚀 Características

*   **Consulta en Tiempo Real**: Conexión directa a la API de OpenWeatherMap.
*   **Arquitectura Profesional**:
    *   **Controlador**: Orquestación de lógica (`main.py`).
    *   **Servicios**: Lógica de negocio encapsulada (`servicio_clima.py`).
    *   **Repositorio**: Persistencia de datos desacoplada (`repository.py`).
*   **Persistencia**: Historial de búsquedas guardado automáticamente en JSON.
*   **Seguridad**: Manejo seguro de credenciales mediante variables de entorno (`.env`).
*   **Código Limpio**: Uso de Type Hinting (tipado estático) y PEP 8.

## 🛠️ Requisitos

*   Python 3.8 o superior.
*   Una API Key de [OpenWeatherMap](https://openweathermap.org/) (Gratuita).

## 📦 Instalación

1.  **Clonar el repositorio** (o descargar los archivos):
    ```bash
    git clone <tu-repositorio>
    cd ProyectoNuevo
    ```

2.  **Crear y activar un entorno virtual** (Recomendado):
    ```bash
    python -m venv climaenv
    # En Windows:
    # climaenv\Scripts\activate
    # En Linux/Mac:
    source climaenv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración**:
    Crea un archivo llamado `.env` en la raíz del proyecto y agrega tu clave:
    ```env
    API_KEY=tu_clave_api_aqui_sin_comillas
    ```

## ▶️ Uso

Ejecuta el punto de entrada principal:

```bash
python main.py
```

Sigue las instrucciones en pantalla para consultar el clima de cualquier ciudad del mundo.

## 📂 Estructura del Proyecto

```text
.
├── config.py           # Gestión de configuración y credenciales
├── main.py             # Punto de entrada (Controller)
├── repository.py       # Capa de acceso a datos (Repository Pattern)
├── servicio_clima.py   # Lógica de negocio (Service Layer)
├── requirements.txt    # Dependencias del proyecto
├── .env                # Variables de entorno (NO subir a Git)
└── historial_climas.json # Base de datos local (generada automáticamente)
```
