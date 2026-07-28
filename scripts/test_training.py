import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from ml.train import train_models


csv_path = "datasets/sample/customer_churn.csv"

results = train_models(csv_path)

print("=" * 60)
print("TRAINING COMPLETED")
print("=" * 60)

print()

print(f"Best Model : {results['best_model']}")

print(f"Accuracy   : {results['accuracy']:.4f}")

print()

print("All Models")

print("-" * 60)

for model, score in results["all_models"].items():

    print(f"{model:<25} {score:.4f}")

print()

print("Features Used")

print("-" * 60)

for feature in results["feature_names"]:

    print(feature)

print()

print("Model saved successfully.")