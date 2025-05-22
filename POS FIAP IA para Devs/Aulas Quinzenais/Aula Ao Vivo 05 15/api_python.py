from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)  # <- permite requisições de qualquer origem (ou especifique o domínio)

model = joblib.load("loan_approval_model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"loan_approved": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
