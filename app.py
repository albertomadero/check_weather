from flask import Flask, render_template, request
import config
from servicio_clima import ServicioClima

app = Flask(__name__)
servicio = ServicioClima(config.API_KEY)

@app.route('/', methods=['GET', 'POST'])
def home():
    datos_clima = None
    if request.method == 'POST':
        ciudad_usuario = request.form.get('ciudad')
        datos_clima = servicio.obtener_clima(ciudad_usuario)
    return render_template('index.html', clima=datos_clima)

if __name__ == '__main__':
    app.run(debug=True)
