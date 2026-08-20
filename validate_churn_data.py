import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

# 1. Load Dataset
csv_filename = "credit_card_customer_churn_dataset.csv"
df = pd.read_csv(csv_filename)

print("=" * 60)
print("1. DATASET OVERVIEW & SHAPE")
print("=" * 60)
print(f"Rows: {df.shape[0]:,}, Columns: {df.shape[1]}")
print(f"Missing Values: {df.isnull().sum().sum()}")

# Verify Column Count Assertion
if df.shape[1] != 40:
    print(f"⚠️ WARNING: Expected 40 columns, but found {df.shape[1]}. Check schema mapping.")
else:
    print("✅ Success: Dataset has expected 40 columns.")

# 2. Target Distribution
print("\n" + "=" * 60)
print("2. TARGET CLASS DISTRIBUTION (churned)")
print("=" * 60)
churn_counts = df["churned"].value_counts(normalize=True) * 100
print(f"Retained (0): {churn_counts.get(0, 0):.2f}%")
print(f"Churned  (1): {churn_counts.get(1, 0):.2f}%")

# 3. Key Risk Metrics by Churn Status
print("\n" + "=" * 60)
print("3. KEY RISK METRICS BY CHURN STATUS")
print("=" * 60)
risk_cols = [
    "financial_stress_score",
    "engagement_score",
    "complaints_count",
    "support_satisfaction",
    "payment_delay_count"
]
print(df.groupby("churned")[risk_cols].mean().round(2).T)

# 4. Quick Predictive Validation (Random Forest)
print("\n" + "=" * 60)
print("4. QUICK PREDICTIVE VALIDATION (Random Forest)")
print("=" * 60)

# Drop identifiers, raw string columns, and LEAKAGE features (churn_risk_score & churn_probability)
leakage_and_id_cols = ["customer_id", "churn_risk_score", "churn_probability", "churned"]
X = df.drop(columns=[c for c in leakage_and_id_cols if c in df.columns])
y = df["churned"]

# One-Hot Encode categorical features
X_encoded = pd.get_dummies(X, drop_first=True)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.20, random_state=42, stratify=y
)

# Train Baseline Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

# Predictions
y_preds = rf.predict(X_test)
y_probs = rf.predict_proba(X_test)[:, 1]

# Metrics Output
roc_auc = roc_auc_score(y_test, y_probs)
print(f"Validation ROC-AUC Score: {roc_auc:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_preds, digits=4))

# Top 5 Features
print("\nTop 5 Most Predictive Features:")
feat_importances = pd.Series(rf.feature_importances_, index=X_encoded.columns)
print(feat_importances.nlargest(5).round(4))
