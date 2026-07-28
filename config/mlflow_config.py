import mlflow

# SQLite Backend
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Experiment Name
mlflow.set_experiment("Customer Churn Prediction")