# Data Dictionary: Credit Card Customer Churn & Retention Dataset

**Dataset Size:** 100,000 Rows × 40 Columns  
**Target Variable:** `churned` (0 = Retained, 1 = Churned)

---

## 1. Demographic & Customer Profile (9 Columns)

| Column Name | Data Type | Range / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `customer_id` | String | `CUST-0000001` – `CUST-0100000` | Unique customer identifier. |
| `age` | Integer | 18 – 85 | Customer age in years. |
| `gender` | Categorical | `Male`, `Female`, `Other` | Self-reported customer gender. |
| `marital_status` | Categorical | `Single`, `Married`, `Divorced`, `Widowed` | Customer marital status. |
| `education_level` | Categorical | `High School`, `Associate`, `Bachelor`, `Master`, `Doctorate` | Highest education level achieved. |
| `employment_status` | Categorical | `Employed`, `Self-Employed`, `Unemployed`, `Retired`, `Student` | Current employment status. |
| `income` | Float | $15,000.00 – $350,000.00 | Estimated gross annual income (USD). |
| `city` | Categorical | Top 9 US Metro Cities + `Other` | Customer's primary city of residence. |
| `credit_score` | Integer | 300 – 850 | FICO-equivalent credit score. |

---

## 2. Account Information (8 Columns)

| Column Name | Data Type | Range / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `account_age_months` | Integer | 1 – 240+ | Tenure with the bank in months. |
| `card_type` | Categorical | `Standard`, `Silver`, `Gold`, `Platinum` | Credit card tier level. |
| `credit_limit` | Float | $1,000.00 – $75,000.00 | Maximum revolving credit limit assigned (USD). |
| `annual_fee` | Float | $0.00, $50.00, $150.00, $450.00 | Annual card membership fee (USD). |
| `interest_rate` | Float | 8.99% – 29.99% | Annual Percentage Rate (APR %). |
| `num_products` | Integer | 1 – 4 | Total number of financial products held with the institution. |
| `has_loan` | Binary | `0` (No), `1` (Yes) | Active loan status with the bank. |
| `has_savings_account` | Binary | `0` (No), `1` (Yes) | Active savings account status with the bank. |

---

## 3. Usage & Transaction Behavior (9 Columns)

| Column Name | Data Type | Range / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `monthly_spending` | Float | $50.00 – $60,000.00 | Total monthly card spending volume (USD). |
| `avg_transaction_amount` | Float | $5.00 – $1,500.00 | Average dollar amount per transaction (USD). |
| `monthly_transactions` | Integer | 1 – 150 | Total transaction count per month. |
| `online_transactions` | Integer | 0 – 120 | Monthly e-commerce / online purchase count. |
| `international_transactions` | Integer | 0 – 30 | Monthly cross-border / international purchase count. |
| `cash_withdrawals` | Integer | 0 – 15 | Monthly cash advance / ATM withdrawal count. |
| `utilization_ratio` | Float | 0.010 – 0.990 | Ratio of revolving balance to credit limit. |
| `payment_delay_count` | Integer | 0 – 10+ | Late / missed payment count in the past 12 months. |
| `late_payment_amount` | Float | $0.00 – $500.00+ | Total late payment fees accrued (USD). |

---

## 4. Engagement & Support (8 Columns)

| Column Name | Data Type | Range / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `app_logins_monthly` | Integer | 0 – 40+ | Monthly mobile app login frequency. |
| `website_visits_monthly` | Integer | 0 – 25+ | Monthly web portal login frequency. |
| `customer_service_calls` | Integer | 0 – 15+ | Support interactions in the past 12 months. |
| `complaints_count` | Integer | 0 – 8+ | Number of formal customer complaints filed. |
| `support_satisfaction` | Float | 1.0 – 5.0 | Post-support satisfaction rating (1 = Poor, 5 = Excellent). |
| `reward_points` | Integer | 0 – 100,000+ | Total active reward points balance. |
| `offers_received` | Integer | 0 – 12+ | Promotional / retention offers extended. |
| `offers_redeemed` | Integer | 0 – 12+ | Extended offers accepted by customer. |

---

## 5. Derived Risk Metrics & Target Variables (6 Columns)

| Column Name | Data Type | Range / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `financial_stress_score` | Float | 0.00 – 100.00 | Composite financial distress index (Utilization + Delays + Credit Rating). |
| `engagement_score` | Float | 0.00 – 100.00 | Composite digital & product engagement index. |
| `customer_value_score` | Float | 0.00 – 100.00 | Estimated profitability / Customer Lifetime Value (LTV) score. |
| `churn_risk_score` | Float | 0.00 – 100.00 | Percentile risk calculation *(Target leakage: Exclude from modeling)*. |
| `churn_probability` | Float | 0.0000 – 1.0000 | Exact logistic probability *(Target leakage: Exclude from modeling)*. |
| **`churned`** | Binary | `0` (Retained), `1` (Churned) | **Primary Target Variable**: Customer attrition status (~19.5% positive rate). |
