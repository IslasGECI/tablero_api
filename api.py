from flask import Flask, Response, jsonify, request
import tablero

app = Flask(__name__)


@app.route("/api/v1/dashboard")
def get_dashboard():
    resp = Response(tablero.get_dashboard().to_json(orient="records"))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/api/v1/records", methods=["POST"])
def add_new_record():
    datafile = "data/testmake.log.csv"
    is_true_analista = request.args["analista"] != "inspector"
    if is_true_analista:
        with open(datafile, "a") as archivo:
            for indice, llave in enumerate(sorted(request.args.keys())):
                archivo.write(
                    "{}{}".format(request.args[llave], "," if indice + 1 < len(request.args) else "\n")
                )
    return jsonify(request.args)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
