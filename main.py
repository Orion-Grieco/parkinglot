import json
import pandas as pd
from flask import jsonify,Flask,render_template,redirect,session, request
from tabulate import tabulate
import os
template_dir = os.path.abspath("C:/Users/Orion/PycharmProjects/flaskTesting/templates")
app = Flask(__name__, template_folder=template_dir)
app.config["JSON_SORT_KEYS"] = False

my_files = r"C:/Users/Orion/PycharmProjects/flaskTesting/static/data/"
project_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = my_files
test_file_dir = r"C:/Users/Orion/Documents/parkingLot/"
file = file_dir + r"jsonContainer.json"
#file2 = file_dir + r"jsonContainer2.json"

@app.route("/")
def html_table():
    with open(file) as f:
        js_object = json.load((f))
        content = pd.read_json(json.dumps((js_object)))
    return render_template("index.html",data =content)

@app.route("/downloads")
def download_files():
    return render_template("template.html")

@app.route("/get_data", methods=["POST"])
def get_data_function():

    user = request.form["user"]

    if user == "three":
        file = file_dir + r"jsonContainer2.json"

        with open(file) as f:
            js_object = json.load(f)
            return jsonify(js_object)

    elif user == "two":
        file = file_dir + r"jsonContainer1.json"

        with open(file) as f:
            js_object = json.load(f)
            return jsonify(js_object)

    if user == "one":
        file = file_dir + r"jsonContainer.json"

        with open(file) as f:
            js_object = json.load(f)
            return jsonify(js_object)

    else:
        file = test_file_dir + r"ParkingDataset.json"
        with open(file) as f:
            js_object = json.load(f)
            return jsonify(js_object)


if __name__ == "__main__":
    app.run(debug=True)
