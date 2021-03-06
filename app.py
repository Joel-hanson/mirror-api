from flask import Flask
from flask import jsonify
import flask
import json
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if flask.request.method == 'POST':
        if flask.request.args.get("request_for") == "hook":
            return jsonify(json.dumps(flask.request.args.to_dict()))
        return jsonify(flask.request.get_json())
    else:
        return jsonify(flask.request.args.to_dict())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
