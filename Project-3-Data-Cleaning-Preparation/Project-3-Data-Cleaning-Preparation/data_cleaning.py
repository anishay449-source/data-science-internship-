import pandas as pd
import numpy as np

# ============================================================
# PROJECT 3: DATA CLEANING & PREPARATION
# ============================================================

# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

input_path = "../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
output_path = "../dataset/cleaned_telco_churn.csv"

df = pd.read_csv(input_path)

print("=" * 60)
print("DATA CLEANING & PREPARATION")
print("=" * 60)

# ------------------------------------------------------------
# 2. Inspect Dataset Structure
# ------------------------------------------------------------

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

# ------------------------------------------------------------
# 3. Check Missing Values Before Cleaning
# ------------------------------------------------------------

print("\n--- Missing Values Before Cleaning ---")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

# ------------------------------------------------------------
# 4. Check Duplicate Records
# ------------------------------------------------------------

print("\n--- Duplicate Records ---")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

# Remove duplicate rows
df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# ------------------------------------------------------------
# 5. Convert TotalCharges to Numeric
# ------------------------------------------------------------

print("\n--- Converting TotalCharges ---")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("TotalCharges data type:", df["TotalCharges"].dtype)

# ------------------------------------------------------------
# 6. Check Missing Values Created After Conversion
# ------------------------------------------------------------

print("\n--- Missing Values After Conversion ---")

missing_after_conversion = df.isnull().sum()

print(
    missing_after_conversion[
        missing_after_conversion > 0
    ]
)

# ------------------------------------------------------------
# 7. Handle Missing TotalCharges
# ------------------------------------------------------------

median_total_charges = df["TotalCharges"].median()

df["TotalCharges"] = df["TotalCharges"].fillna(
    median_total_charges
)

print(
    "\nMissing TotalCharges after imputation:",
    df["TotalCharges"].isnull().sum()
)

# ------------------------------------------------------------
# 8. Standardize Categorical Columns
# ------------------------------------------------------------

categorical_columns = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "Churn"
]

for column in categorical_columns:

    if column in df.columns:
        df[column] = df[column].astype(str).str.strip()

print("\nCategorical values standardized.")

# ------------------------------------------------------------
# 9. Check Numerical Columns
# ------------------------------------------------------------

numeric_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

print("\n--- Numerical Column Validation ---")

for column in numeric_columns:

    negative_values = (df[column] < 0).sum()

    print(
        f"{column}: {negative_values} negative values"
    )

# ------------------------------------------------------------
# 10. Check Customer ID Duplicates
# ------------------------------------------------------------

print("\n--- Customer ID Check ---")

customer_id_duplicates = df["customerID"].duplicated().sum()

print(
    "Duplicate customer IDs:",
    customer_id_duplicates
)

# ------------------------------------------------------------
# 11. Final Missing Value Check
# ------------------------------------------------------------

print("\n--- Final Missing Values ---")

final_missing = df.isnull().sum()

print(
    final_missing[
        final_missing > 0
    ]
)

# ------------------------------------------------------------
# 12. Final Dataset Information
# ------------------------------------------------------------

print("\n--- Final Dataset Information ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFinal Data Types:")
print(df.dtypes)

# ------------------------------------------------------------
# 13. Save Clean Dataset
# ------------------------------------------------------------

df.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(
    f"Cleaned dataset saved to: {output_path}"
)
