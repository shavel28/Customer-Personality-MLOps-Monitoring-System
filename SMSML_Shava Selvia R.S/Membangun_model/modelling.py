import pandas as pd
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("customer_preprocessed.csv")
X = df.drop("Target", axis=1)
y = df["Target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mengaktifkan autolog MLflow lokal
mlflow.autolog()

with mlflow.start_run():
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

print("Training Basic Selesai!")
