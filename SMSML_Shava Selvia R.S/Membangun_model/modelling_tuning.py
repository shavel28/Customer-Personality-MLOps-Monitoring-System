import dagshub
import mlflow
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. Hubungkan ke DagsHub (Ganti sesuai username Anda jika berbeda)
dagshub.init(
    repo_owner="shavel28",
    repo_name="customer-mlops",
    mlflow=True
)

# 2. Load & Split Data
df = pd.read_csv("customer_preprocessed.csv")
X = df.drop("Target", axis=1)
y = df["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Hyperparameter Tuning
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10],
    "min_samples_split": [2, 5]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring="accuracy")
print("Sedang mencari hyperparameter terbaik...")
grid.fit(X_train, y_train)
best_model = grid.best_estimator_

# 4. Evaluasi & Hitung Metrik
y_pred = best_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# 5. Bikin Grafik Artefak 1: Confusion Matrix
plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

# 6. Bikin Grafik Artefak 2: Feature Importance
importance = pd.DataFrame({"Feature": X.columns, "Importance": best_model.feature_importances_})
importance = importance.sort_values(by="Importance", ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x="Importance", y="Feature", data=importance.head(10))
plt.title("Top 10 Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# 7. Simpan Model Berupa File Pickle
joblib.dump(best_model, "rf_model.pkl")

# 8. Kirim Data Eksperimen ke DagsHub (Manual Logging)
with mlflow.start_run(run_name="RF_Hyperparameter_Tuning"):
    mlflow.log_params(grid.best_params_)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", prec)
    mlflow.log_metric("recall", rec)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_artifact("feature_importance.png")
    mlflow.sklearn.log_model(best_model, "model")

print("Semua data berhasil dikirim ke Dashboard DagsHub!")
