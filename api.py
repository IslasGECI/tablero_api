from flask import Flask, jsonify, render_template, request
import tablero
app = Flask(__name__)

@app.route('/api/v1/dashboard')
def get_dashboard():
    return tablero.get_dashboard().to_json(orient='records')

@app.route('/api/v1/records', methods=['POST'])
def add_new_record():
    datafile = 'data/testmake.log.csv'
    with open(datafile, 'a') as archivo:
        for indice, llave in enumerate(sorted(request.args.keys())):
            archivo.write("{}{}".format(request.args[llave], "," if indice+1 < len(request.args) else "\n"))
    return jsonify(request.args)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
