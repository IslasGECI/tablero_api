from flask import Flask, jsonify, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    peticion = requests.get(url="http://localhost:500/api/v1/dashboard")
    return render_template("index.html", tablero=peticion.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
