

from sklearn.model_selection import train_test_split
import pandas as pd

from src.data_preprocessing import (
    load_data, clean_data, encode_data,
    split_features_target, scale_data
)

from src.model_training import get_models, train_model
from src.evaluation import evaluate_model


def main():


    df = load_data("data/Automobile_data.csv")
    df = clean_data(df)
    df = encode_data(df)


    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)


    models = get_models()
    results = []

    for name, model in models.items():

        # Use scaled data for linear models
        if name in ["Linear Regression", "Ridge", "Lasso"]:
            trained_model = train_model(model, X_train_scaled, y_train)
            r2, rmse = evaluate_model(trained_model, X_test_scaled, y_test)
        else:
            trained_model = train_model(model, X_train, y_train)
            r2, rmse = evaluate_model(trained_model, X_test, y_test)

        results.append([name, r2, rmse])


    results_df = pd.DataFrame(results, columns=["Model", "R2 Score", "RMSE"])
    results_df = results_df.sort_values(by="R2 Score", ascending=False)

    print("Model Comparison:")
    print(results_df)

    print(" Best Model:", results_df.iloc[0]["Model"])


if __name__ == "__main__":
    main()