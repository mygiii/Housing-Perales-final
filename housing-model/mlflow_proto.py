import os
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np


def main():
    # Charger le dataset nettoyé
    df = pd.read_csv("housing_clean.csv")

    # Séparer X, y
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    # Encoder la colonne ocean_proximity (elle doit exister)
    if "ocean_proximity" in X.columns:
        X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # **Start an MLflow run**
    mlflow.set_experiment("California_Housing_Model")

    with mlflow.start_run():
        # **Modèle**
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # **Évaluation**
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"MAE = {mae}")
        print(f"R^2 = {r2}")

        # **Log parameters and metrics**
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # **Exemple d'entrée**
        input_example = X_train.iloc[:1]  # Prend la première ligne sous forme de DataFrame

        # **Signature MLflow**
        signature = infer_signature(X_train, model.predict(X_train))

        # **Log the model**
        mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example)

        # **Sauvegarder le modèle**
        os.makedirs("model", exist_ok=True)
        joblib.dump(model, "model/model.joblib")
        print("Modèle sauvegardé dans model/model.joblib")

        # **Sauvegarder la liste ordonnée des colonnes**
        trained_columns = X_train.columns.tolist()
        joblib.dump(trained_columns, "model/trained_columns.joblib")
        print("Liste des colonnes entraînées sauvegardée dans model/trained_columns.joblib")


if __name__ == "__main__":
    main()
