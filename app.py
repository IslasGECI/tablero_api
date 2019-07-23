from flask import Flask, jsonify, render_template, request
from tablero.Dashboard import get_dashboard
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", tablero=get_dashboard())

@app.route('/api/v1/record', methods=['POST'])
def add_new_record():
    datafile = 'data/testmake.log.csv'
    repo = request.args['repo']
    objetivo = request.args['objetivo']
    revision = request.args['revision']
    id = request.args['id']
    phony = request.args['phony']
    analista = request.args['analista']
    maquina = request.args['maquina']
    timestamp = request.args['timestamp']
    es_make_exitoso = request.args['es_make_exitoso']
    es_phony = request.args['es_phony']
    existe_objetivo = request.args['existe_objetivo']
    with open(datafile, 'a') as archivo:
        archivo.write(f"{repo},{objetivo},{revision},{id},{phony},{analista},{maquina},{timestamp},{es_make_exitoso},{es_phony},{existe_objetivo}\n")
    archivo.close()
    return jsonify(request.args)

if __name__ == "__main__":
    tablero=get_dashboard()
    app.run(debug=True)
