import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn
import mlflow.models.signature

# Load the dataset
df = pd.read_csv("housing.csv")

# Separate X and y
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Encode the ocean_proximity column if it exists
if "ocean_proximity" in X.columns:
    X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model with RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and calculate metrics
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error du modèle :", mae)
print("Score R2 du modèle :", r2)

# Infer the model signature (input and output schema)
signature = mlflow.models.signature.infer_signature(X_train, model.predict(X_train))

# Log the model with MLflow
mlflow.set_tracking_uri("http://mlflow_container:5000")  # Ensure this matches your MLflow server URI
mlflow.set_experiment("Housing Model")
with mlflow.start_run() as run:
    mlflow.log_param("model", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2", r2)
    mlflow.sklearn.log_model(
        model,
        "model",
        input_example=X_train.head(1),
        signature=signature
    )
    run_id = run.info.run_id
    print("Modèle loggué avec le run ID :", run_id)

# Export the model to the 'model' directory
mlflow.sklearn.save_model(model, "model", signature=signature, input_example=X_train.head(1))
print("Modèle exporté dans le dossier 'model'")