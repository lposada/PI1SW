from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.mediciones import Medicion

app = Flask(__name__)
CORS(app)

@app.route('/Mediciones', methods=['GET'])
def getAll():
    return (Medicion.list())

@app.route("/Mediciones", methods=['POST'])
def postOne():
    body = request.json
    return (Medicion.create(body))

app.run(port=4000, debug=True)