import os
import joblib

import mlflow
import mlflow.sklearn

from config.mlflow_config import *

from sklearn.metrics import accuracy_score

from ml.preprocessing import preprocess_data
from ml.evaluate import evaluate_model
from ml.tuning import get_models
from ml.registry import register_model


def train_models(csv_path, model_dir="models/production"):
    """
    Train multiple machine learning models,
    evaluate them,
    log everything to MLflow,
    save the best model,
    and register model versions.
    """

    # ----------------------------------
    # Start MLflow Experiment
    # ----------------------------------
    with mlflow.start_run():

        # ----------------------------------
        # Load Dataset
        # ----------------------------------
        (
            X_train,
            X_test,
            y_train,
            y_test,
            encoders,
            feature_names
        ) = preprocess_data(csv_path)

        # ----------------------------------
        # Candidate Models
        # ----------------------------------
        models = get_models()

        results = {}

        best_model = None
        best_accuracy = 0

        best_name = ""

        # ----------------------------------
        # Train Every Model
        # ----------------------------------
        for name, model in models.items():

            print("\n" + "-" * 60)
            print(f"Training {name}")
            print("-" * 60)

            model.fit(
                X_train,
                y_train
            )

            predictions = model.predict(
                X_test
            )

            accuracy = accuracy_score(
                y_test,
                predictions
            )

            results[name] = round(
                accuracy,
                4
            )

            print(
                f"{name} Accuracy : {accuracy:.4f}"
            )

            if accuracy > best_accuracy:

                best_accuracy = accuracy

                best_model = model

                best_name = name

        # ----------------------------------
        # Evaluate Best Model
        # ----------------------------------
        evaluation = evaluate_model(

            best_model,

            X_test,

            y_test

        )

        # ----------------------------------
        # Log Parameters
        # ----------------------------------
        mlflow.log_param(

            "algorithm",

            best_name

        )

        mlflow.log_param(

            "training_samples",

            len(X_train)

        )

        mlflow.log_param(

            "testing_samples",

            len(X_test)

        )

        mlflow.log_param(

            "features",

            len(feature_names)

        )

        # ----------------------------------
        # Log Metrics
        # ----------------------------------
        mlflow.log_metric(

            "accuracy",

            evaluation["accuracy"]

        )

        mlflow.log_metric(

            "precision",

            evaluation["precision"]

        )

        mlflow.log_metric(

            "recall",

            evaluation["recall"]

        )

        mlflow.log_metric(

            "f1_score",

            evaluation["f1_score"]

        )

        mlflow.log_metric(

            "roc_auc",

            evaluation["roc_auc"]

        )

        # ----------------------------------
        # Save in MLflow
        # ----------------------------------
        mlflow.sklearn.log_model(

            sk_model=best_model,

            name="best_model"

        )

        # ----------------------------------
        # Create Production Folder
        # ----------------------------------
        os.makedirs(

            model_dir,

            exist_ok=True

        )

        # ----------------------------------
        # Save Production Model
        # ----------------------------------
        model_path = os.path.join(

            model_dir,

            "best_model.pkl"

        )

        joblib.dump(

            best_model,

            model_path

        )

        # ----------------------------------
        # Save Label Encoders
        # ----------------------------------
        joblib.dump(

            encoders,

            os.path.join(

                model_dir,

                "encoders.pkl"

            )

        )
                # ----------------------------------
        # Register Model Version
        # ----------------------------------
        version = register_model(

            model_path,

            evaluation

        )

        # ----------------------------------
        # Console Summary
        # ----------------------------------
        print("\n")
        print("=" * 60)
        print("TRAINING COMPLETED")
        print("=" * 60)

        print(f"Best Model      : {best_name}")
        print(f"Model Version   : {version}")
        print(f"Accuracy        : {best_accuracy:.4f}")

        print("\nEvaluation Metrics")
        print("-" * 60)

        print(
            f"Accuracy  : {evaluation['accuracy']:.4f}"
        )

        print(
            f"Precision : {evaluation['precision']:.4f}"
        )

        print(
            f"Recall    : {evaluation['recall']:.4f}"
        )

        print(
            f"F1 Score  : {evaluation['f1_score']:.4f}"
        )

        print(
            f"ROC AUC   : {evaluation['roc_auc']:.4f}"
        )

        print("\nFeatures Used")
        print("-" * 60)

        for feature in feature_names:

            print(feature)

        print("\n")
        print("=" * 60)
        print("Production Model Saved Successfully")
        print("=" * 60)

        # ----------------------------------
        # API Response
        # ----------------------------------
        return {

            "model_version": version,

            "best_model": best_name,

            "accuracy": round(
                best_accuracy,
                4
            ),

            "all_models": results,

            "feature_names": feature_names,

            "evaluation": evaluation

        }