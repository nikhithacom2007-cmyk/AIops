import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(csv_path):
    """
    Load, clean, encode, and split the dataset.
    """

    # -----------------------------
    # Step 1: Read Dataset
    # -----------------------------
    df = pd.read_csv(csv_path)

    # -----------------------------
    # Step 2: Remove Customer ID
    # -----------------------------
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # -----------------------------
    # Step 3: Convert TotalCharges
    # -----------------------------
    if "TotalCharges" in df.columns:

        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

    # -----------------------------
    # Step 4: Handle Missing Values
    # -----------------------------
    df = df.ffill()


    # -----------------------------
    # Step 5: Remove Duplicates
    # -----------------------------
    df = df.drop_duplicates()

    # -----------------------------
    # Step 6: Encode Categorical Data
    # -----------------------------
    encoders = {}

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(
            df[column]
        )

        encoders[column] = encoder

    # -----------------------------
    # Step 7: Split Features & Target
    # -----------------------------
    target_column = "Churn"

    X = df.drop(columns=[target_column])

    y = df[target_column]

    feature_names = list(X.columns)

    # -----------------------------
    # Step 8: Train/Test Split
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42,

        stratify=y

    )

    # -----------------------------
    # Step 9: Return Everything
    # -----------------------------
    return (

        X_train,

        X_test,

        y_train,

        y_test,

        encoders,

        feature_names

    )