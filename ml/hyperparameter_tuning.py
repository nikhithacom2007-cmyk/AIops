from sklearn.model_selection import RandomizedSearchCV


def tune_model(
    model,
    param_grid,
    X_train,
    y_train
):

    search = RandomizedSearchCV(

        estimator=model,

        param_distributions=param_grid,

        n_iter=10,

        scoring="accuracy",

        cv=5,

        random_state=42,

        n_jobs=-1

    )

    search.fit(
        X_train,
        y_train
    )

    return (

        search.best_estimator_,

        search.best_params_,

        search.best_score_

    )