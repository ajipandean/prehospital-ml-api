from flask import Flask, request, jsonify
from operator import itemgetter
import pickle

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
port = 8080

@app.route("/predict", methods=["POST"])
def predict():
    req = request.get_json()["symtomps"]
    classes = model.classes_
    prediction = model.predict_proba([req])[0]

    # Merge 2 arrays into dictionary
    probability = [{
        "label": label,
        "value": value,
    } for label, value in zip(classes, prediction)]
    sorted_probability = sorted(probability, key=lambda l: l["value"], reverse=True)

    return jsonify(sorted_probability)

if __name__ == "__main__":
    model = pickle.load(open("models/model-v2.pkl", "rb"))
    app.run(port=port, debug = True)