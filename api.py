from flask import Flask, Response, jsonify, request
from functools import wraps
import tablero
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("TABLERO_API_SECRET_KEY")


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"]

        if not token:
            return jsonify({"message": "a valid token is missing"})

        if token == app.config["SECRET_KEY"]:
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "token is invalid"})

    return decorator


@app.route("/api/v1/dashboard")
@token_required
def get_dashboard():
    resp = Response(tablero.get_dashboard().to_json(orient="records"))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/api/v1/records", methods=["POST"])
@token_required
def add_new_record():
    datafile = "data/testmake.log.csv"
    is_valid_request = tablero.validate_request(request)
    if is_valid_request:
        with open(datafile, "a") as archivo:
            for indice, llave in enumerate(sorted(request.args.keys())):
                archivo.write(
                    "{}{}".format(
                        request.args[llave], "," if indice + 1 < len(request.args) else "\n"
                    )
                )
    return jsonify(request.args)


if __name__ == "__main__":  # pragma: no mutate
    app.run(host="0.0.0.0", debug=True)
