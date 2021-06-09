from flask import Flask, request, jsonify
import pickle
import urllib

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
port = 8080

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
    url = "https://storage.googleapis.com/g-one-bucket/ml-models/model-v3.pkl"
    file = urllib.request.urlopen(url)
    model = pickle.load(file)
    app.run(host="0.0.0.0", port=port)
