import numpy as np
import pandas as pd

np.random.seed(42)
N = 100_000

# 1. Customer Profile (9)
customer_id = [f"CUST-{i:07d}" for i in range(1, N + 1)]
age = np.clip(np.random.normal(loc=44, scale=13, size=N), 18, 85).astype(int)
gender = np.random.choice(["Male", "Female", "Other"], size=N, p=[0.49, 0.49, 0.02])
marital_status = np.random.choice(["Single", "Married", "Divorced", "Widowed"], size=N, p=[0.35, 0.48, 0.12, 0.05])
education_level = np.random.choice(["High School", "Associate", "Bachelor", "Master", "Doctorate"], size=N, p=[0.25, 0.15, 0.40, 0.15, 0.05])
employment_status = np.random.choice(["Employed", "Self-Employed", "Unemployed", "Retired", "Student"], size=N, p=[0.62, 0.15, 0.08, 0.10, 0.05])

edu_multiplier = pd.Series(education_level).map({"High School": 1.0, "Associate": 1.15, "Bachelor": 1.45, "Master": 1.8, "Doctorate": 2.2}).values
base_income = np.random.lognormal(mean=10.6, sigma=0.55, size=N)
income = np.clip(base_income * edu_multiplier * (1 + (age - 18) / 100), 15000, 350000).round(2)
city = np.random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Other"], size=N, p=[0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.04, 0.04, 0.42])
credit_score = np.clip(np.random.normal(loc=690, scale=80, size=N), 300, 850).astype(int)

# 2. Account Information (8)
account_age_months = np.random.exponential(scale=42, size=N).astype(int) + 1
card_type = np.random.choice(["Standard", "Silver", "Gold", "Platinum"], size=N, p=[0.45, 0.30, 0.18, 0.07])
card_rank = pd.Series(card_type).map({"Standard": 1, "Silver": 2, "Gold": 3, "Platinum": 4}).values
credit_limit = np.clip((income * 0.15) * (card_rank * 0.8) + np.random.normal(0, 2000, N), 1000, 75000).round(-2)
annual_fee = pd.Series(card_type).map({"Standard": 0, "Silver": 50, "Gold": 150, "Platinum": 450}).values
interest_rate = np.clip(28.0 - (credit_score - 300) * (16.0 / 550) + np.random.normal(0, 1.5, N), 8.99, 29.99).round(2)
num_products = np.random.choice([1, 2, 3, 4], size=N, p=[0.45, 0.35, 0.15, 0.05])
has_loan = np.random.choice([0, 1], size=N, p=[0.65, 0.35])
has_savings_account = np.random.choice([0, 1], size=N, p=[0.40, 0.60])

# 3. Usage Behavior (9)
utilization_ratio = np.clip(np.random.beta(a=2, b=5, size=N) + (800 - credit_score) / 1200, 0.01, 0.99).round(3)
monthly_spending = np.clip(credit_limit * utilization_ratio * np.random.uniform(0.7, 1.1, N), 50, 60000).round(2)
monthly_transactions = np.clip((monthly_spending / np.random.uniform(25, 120, N)), 1, 150).astype(int)
avg_transaction_amount = (monthly_spending / np.maximum(monthly_transactions, 1)).round(2)
online_transactions = (monthly_transactions * np.random.uniform(0.2, 0.8, N)).astype(int)
international_transactions = (monthly_transactions * np.random.beta(0.5, 5, size=N)).astype(int)
cash_withdrawals = np.random.poisson(lam=1.2, size=N)
payment_delay_count = np.random.negative_binomial(n=1, p=0.7, size=N)
late_payment_amount = np.where(payment_delay_count > 0, np.clip(payment_delay_count * np.random.exponential(scale=45, size=N), 15, 500), 0.0).round(2)

# 4. Customer Engagement (8)
app_logins_monthly = np.random.poisson(lam=12, size=N)
website_visits_monthly = np.random.poisson(lam=6, size=N)
customer_service_calls = np.random.negative_binomial(n=1, p=0.4, size=N)
complaints_count = np.where(customer_service_calls > 0, np.random.binomial(n=customer_service_calls, p=0.4), 0)
support_satisfaction = np.clip(np.random.normal(4.0, 0.6, N) - (complaints_count * 0.7) - (payment_delay_count * 0.3), 1.0, 5.0).round(1)
reward_points = (monthly_spending * np.random.uniform(0.8, 1.5, N)).astype(int)
offers_received = np.random.poisson(lam=3, size=N)
offers_redeemed = np.minimum(offers_received, np.random.binomial(n=np.maximum(offers_received, 1), p=0.35))

# 5. Derived & Risk Metrics (5)
financial_stress_score = np.clip((utilization_ratio * 40) + (payment_delay_count * 15) + ((850 - credit_score) / 850 * 35) + np.random.normal(0, 5, N), 0, 100).round(2)
engagement_score = np.clip((app_logins_monthly * 2.5) + (website_visits_monthly * 1.5) + (offers_redeemed * 8) + (num_products * 10) + np.random.normal(0, 5, N), 0, 100).round(2)
customer_value_score = np.clip((monthly_spending / 500) + (card_rank * 15) + (account_age_months / 12 * 3) + np.random.normal(0, 5, N), 0, 100).round(2)

# Calibrated Logit Equation
logit = (
    + 0.85
    + 0.050 * financial_stress_score
    - 0.040 * engagement_score
    - 0.350 * support_satisfaction
    + 0.500 * complaints_count
    + 0.350 * payment_delay_count
    - 0.020 * (account_age_months / 12)
    - 0.350 * num_products
    + np.where(monthly_spending < 300, 0.6, -0.2)
    + np.random.normal(0, 0.55, N)
)

churn_probability = 1 / (1 + np.exp(-logit))
churn_risk_score = (churn_probability * 100).round(2)
churned = (churn_probability > np.random.uniform(0, 1, N)).astype(int)

# EXACTLY 40 COLUMNS DICTIONARY
df = pd.DataFrame({
    # Profile (9)
    "customer_id": customer_id,
    "age": age,
    "gender": gender,
    "marital_status": marital_status,
    "education_level": education_level,
    "employment_status": employment_status,
    "income": income,
    "city": city,
    "credit_score": credit_score,
    # Account (8)
    "account_age_months": account_age_months,
    "card_type": card_type,
    "credit_limit": credit_limit,
    "annual_fee": annual_fee,
    "interest_rate": interest_rate,
    "num_products": num_products,
    "has_loan": has_loan,
    "has_savings_account": has_savings_account,
    # Usage (9)
    "monthly_spending": monthly_spending,
    "avg_transaction_amount": avg_transaction_amount,
    "monthly_transactions": monthly_transactions,
    "online_transactions": online_transactions,
    "international_transactions": international_transactions,
    "cash_withdrawals": cash_withdrawals,
    "utilization_ratio": utilization_ratio,
    "payment_delay_count": payment_delay_count,
    "late_payment_amount": late_payment_amount,
    # Engagement (8)
    "app_logins_monthly": app_logins_monthly,
    "website_visits_monthly": website_visits_monthly,
    "customer_service_calls": customer_service_calls,
    "complaints_count": complaints_count,
    "support_satisfaction": support_satisfaction,
    "reward_points": reward_points,
    "offers_received": offers_received,
    "offers_redeemed": offers_redeemed,
    # Derived & Target (6)
    "financial_stress_score": financial_stress_score,
    "engagement_score": engagement_score,
    "customer_value_score": customer_value_score,
    "churn_risk_score": churn_risk_score,
    "churn_probability": churn_probability.round(4),
    "churned": churned
})

df.to_csv("credit_card_customer_churn_dataset.csv", index=False)
print(f"Dataset generated successfully with shape {df.shape} and saved to 'credit_card_customer_churn_dataset.csv'.")
