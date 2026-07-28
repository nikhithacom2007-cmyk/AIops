import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from ml.preprocessing import preprocess_data

csv_path = "datasets/sample/customer_churn.csv"

(
    X_train,
    X_test,
    y_train,
    y_test,
    encoders,
    feature_names
) = preprocess_data(csv_path)

print("=" * 60)
print("PREPROCESSING SUCCESSFUL")
print("=" * 60)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

print(f"\nNumber of Features : {len(feature_names)}")

print("\nFeature Names:")
print(feature_names)

print("\nEncoded Columns:")
print(list(encoders.keys()))

print("\nTraining Data Preview:")
print(X_train.head())