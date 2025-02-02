import os
import pandas as pd
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def main():
    # Charger le dataset nettoyé
    df = pd.read_csv("data/housing_clean.csv")

    # Séparer X, y
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    # Encoder la colonne ocean_proximity
    if "ocean_proximity" in X.columns:
        X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # **Start an MLflow run**
    mlflow.set_tracking_uri("http://mlflow_server:5000")  # Connect to MLflow container
    mlflow.set_experiment("California_Housing_Model")

    with mlflow.start_run():
        # **Train Model**
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # **Evaluate**
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"MAE = {mae}")
        print(f"R^2 = {r2}")

        # **Log Parameters and Metrics**
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # **Register Model in MLflow**
        input_example = X_train.iloc[:1]
        signature = infer_signature(X_train, model.predict(X_train))
        mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example, registered_model_name="California_Housing_Model")

    print("Model registered in MLflow!")

if __name__ == "__main__":
    main()
