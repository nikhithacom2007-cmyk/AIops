import joblib
import pandas as pd


MODEL_PATH = "models/production/best_model.pkl"


def predict(data: dict):

    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    confidence = float(max(probability))

    label = (
        "Churn"
        if prediction == 1
        else "No Churn"
    )

    return {

        "prediction": int(prediction),

        "prediction_label": label,

        "confidence": round(confidence, 4)

    }