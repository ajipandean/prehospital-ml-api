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
    probability = {key: value for key, value in zip(classes, prediction)}
    sorted_probability = {}
    for key in sorted(probability, key=probability.get, reverse=True):
        sorted_probability[key] = probability[key]

    return jsonify(sorted_probability)

if __name__ == "__main__":
    model = pickle.load(open("models/diseases.pkl", "rb"))
    app.run(port=port, debug = True)