# Proyecto Clima (Híbrido) 🌤️

Una aplicación completa para consultar el clima en tiempo real, desarrollada en **Python**.
Ahora cuenta con **dos modos de uso**: Consola (CLI) y Web (Flask).

## 🚀 Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/TU_USUARIO/ProyectoNuevo.git
    cd ProyectoNuevo
    ```

2.  **Configurar Entorno Virtual:**
    ```bash
    python -m venv climaenv
    source climaenv/bin/activate  # En Windows: climaenv\Scripts\activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar API Key:**
    *   Crea un archivo `.env` en la raíz.
    *   Agrega tu clave de OpenWeatherMap:
        ```text
        API_KEY=tu_clave_secreta_aqui
        ```

---

## 💻 Modos de Uso

### Opción A: Modo Consola (CLI)
Ideal para consultas rápidas y ver tu historial detallado.
```bash
python main.py
```
*   ✅ Consultar clima por ciudad.
*   ✅ Ver historial de búsquedas.
*   ✅ Ver estadísticas (Temp. Máxima, Mínima y Promedio).

### Opción B: Modo Web (Flask)
Una interfaz visual amigable accesible desde el navegador.
```bash
python app.py
```
*   Abre tu navegador en: `http://127.0.0.1:5000`
*   ✅ Interfaz gráfica con formularios.
*   ✅ Visualización limpia de los resultados.

---

## 🛠️ Tecnologías
*   **Python 3.x**
*   **Flask** (Web Framework)
*   **Requests** (Consumo de APIs)
*   **Dotenv** (Seguridad)
*   **JSON** (Persistencia de datos)

## 📂 Estructura
*   `main.py`: Punto de entrada para la CLI.
*   `app.py`: Punto de entrada para la Web.
*   `servicio_clima.py`: Lógica de conexión con la API (Reutilizable).
*   `repository.py`: Manejo de base de datos JSON (Reutilizable).
