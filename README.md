#  Credit Card Customer Churn & Retention Dataset (100K) Generator

A Python-based synthetic data generator that creates a realistic retail credit card customer dataset containing **100,000 records** and **40 features** for churn prediction, classification benchmarks, and customer retention analytics.

---

##  Dataset Overview

* **Rows:** 100,000
* **Columns:** 40 (Demographic, Usage, Account, Support, Risk Scores, and Target)
* **Target Class Ratio:** ~19.5% Churned (`1`) vs. ~80.5% Retained (`0`)
* **Format:** CSV (`credit_card_customer_churn_dataset.csv`)

---

##  Quick Start

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/MobeenFatimaa/Credit-Card-Customer-Churn-Retention-Dataset-100K-Generator.git
cd Credit-Card-Customer-Churn-Retention-Dataset-100K-Generator
pip install -r requirements.txt
```

### 2. Generate Dataset

```bash
python generate_churn_data.py
```

---

##  Repository Structure

```text
generate_churn_data.py  - Core generation script incorporating calibrated logit logic and stochastic noise.
requirements.txt        - Required dependencies (pandas, numpy, etc.).
LICENSE                 - MIT License.
```

---

##  Modeling Note (Data Leakage)

When building machine learning models, exclude `customer_id`, `churn_risk_score`, and `churn_probability` from your feature matrix `X` to prevent target leakage:

```python
X = df.drop(columns=[
    "customer_id",
    "churn_risk_score",
    "churn_probability",
    "churned"
])

y = df["churned"]
```

---

##  License

Distributed under the MIT License.
