from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the serialized model
model = joblib.load("superkart_model.joblib")

app = Flask(__name__)

# -----------------------------
# 1. ONLINE INFERENCE ENDPOINT
# -----------------------------
@app.post("/v1/predict")
def predict():
    data = request.get_json()
    df_input = pd.DataFrame([data])
    prediction = model.predict(df_input)[0]
    return jsonify({"predicted_sales": float(prediction)})

# -----------------------------
# 2. BATCH INFERENCE ENDPOINT
# -----------------------------
@app.post("/v1/predictbatch")
def predict_batch():
    file = request.files['file']
    df = pd.read_csv(file)
    preds = model.predict(df)
    return jsonify({i: float(p) for i, p in enumerate(preds)})

# -----------------------------
# Run the API
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
