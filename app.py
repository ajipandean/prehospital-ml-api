from flask import Flask, request, jsonify
from operator import itemgetter
import pickle
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
port = 8081

@app.route("/predict", methods=["POST"])
def predict():
    req = request.get_json()
    req = [i[1] for i in req.items()]
    classes = model.classes_
    prediction = model.predict_proba([req])[0]

    probability = [{
        "label": label,
        "value": value,
    } for label, value in zip(classes, prediction)]
    sorted_probability = sorted(probability, key=lambda l: l["value"], reverse=True)

    return jsonify(sorted_probability)

if __name__ == "__main__":
    model = pickle.load(open("models/model-v3.pkl", "rb"))
    app.run(host="0.0.0.0", port=port, debug = True)
