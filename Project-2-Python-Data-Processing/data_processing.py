import pandas as pd

# Load dataset
file_path = "../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# -----------------------------
# Business Rule 1: Customer Age
# -----------------------------

def customer_segment(tenure):
    if tenure <= 12:
        return "New Customer"
    elif tenure <= 48:
        return "Established Customer"
    else:
        return "Long-Term Customer"


df["CustomerSegment"] = df["tenure"].apply(customer_segment)

# --------------------------------
# Business Rule 2: Monthly Charges
# --------------------------------

def charge_category(charge):
    if charge >= 70:
        return "High Charge"
    elif charge >= 40:
        return "Medium Charge"
    else:
        return "Low Charge"


df["ChargeCategory"] = df["MonthlyCharges"].apply(charge_category)

# -----------------------------
# Business Rule 3: Revenue
# -----------------------------

df["EstimatedAnnualRevenue"] = df["MonthlyCharges"] * 12

# -----------------------------
# Business Rule 4: Churn Risk
# -----------------------------

def churn_risk(row):

    score = 0

    if row["Contract"] == "Month-to-month":
        score += 1

    if row["tenure"] <= 12:
        score += 1

    if row["MonthlyCharges"] >= 70:
        score += 1

    if row["PaymentMethod"] == "Electronic check":
        score += 1

    if score >= 3:
        return "High Risk"
    elif score == 2:
        return "Medium Risk"
    else:
        return "Low Risk"


df["RiskCategory"] = df.apply(churn_risk, axis=1)

# -----------------------------
# Generate output
# -----------------------------

output_columns = [
    "customerID",
    "tenure",
    "MonthlyCharges",
    "CustomerSegment",
    "ChargeCategory",
    "EstimatedAnnualRevenue",
    "RiskCategory",
    "Churn"
]

processed_data = df[output_columns]

processed_data.to_csv(
    "../dataset/processed_customer_data.csv",
    index=False
)

print("Processing completed successfully.")

print("\nCustomer Segment:")
print(df["CustomerSegment"].value_counts())

print("\nRisk Category:")
print(df["RiskCategory"].value_counts())

print("\nProcessed Data:")
print(processed_data.head())
