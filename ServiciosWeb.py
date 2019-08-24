from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import statistics

app = Flask(__name__)
CORS(app)

tipo_medicion = {'unidades': ''}

mediciones = [
    {'fecha': '2019-08-20 11:23:22', **tipo_medicion, 'valor': 60},
    {'fecha': '2019-08-21 20:00:00', **tipo_medicion, 'valor': 52},
    {'fecha': '2019-08-22 20:45:27', **tipo_medicion, 'valor': 68},
    {'fecha': '2019-08-22 20:50:55', **tipo_medicion, 'valor': 70},
    {'fecha': '2019-08-22 21:05:10', **tipo_medicion, 'valor': 70},
    {'fecha': '2019-08-22 21:30:05', **tipo_medicion, 'valor': 65},
    {'fecha': '2019-08-22 22:01:33', **tipo_medicion, 'valor': 80}
]

valores = [x['valor'] for x in mediciones]

@app.route("/obtener", methods=['GET'])
def getAll():
    return jsonify({'mediciones' : mediciones})
    
@app.route("/obtenermoda", methods=['GET'])
def getModa():
    moda = statistics.mode(valores)

    return jsonify(moda)

app.run(port=8000, debug=True)
