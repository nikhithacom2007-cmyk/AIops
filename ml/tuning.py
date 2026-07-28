from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except Exception:
    XGBOOST_AVAILABLE = False


def get_models():

    models = {

        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            random_state=42
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),

        "LightGBM": LGBMClassifier(
            random_state=42,
            verbose=-1
        ),

        "CatBoost": CatBoostClassifier(
            verbose=0,
            random_state=42
        )

    }

    if XGBOOST_AVAILABLE:

        models["XGBoost"] = XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        )

    return models