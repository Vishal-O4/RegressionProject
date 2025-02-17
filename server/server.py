from flask import Flask, jsonify, request
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)


@app.route("/get_location_names",  methods=['GET'])
def get_location_names():
    response = jsonify({
        "locations" : util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/get_area_types",  methods=['GET'])
def get_area_types():
    response = jsonify({
        "area_type": util.get_area_types()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    area = request.form["area_type"]
    print(total_sqft, location, bhk, bath)
    response = jsonify({
        "estimate_price": util.get_estimated_price(location, total_sqft, bhk, bath, area)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting python flask server for home prediction")
    util.load_saved_artifacts()
    app.run()
