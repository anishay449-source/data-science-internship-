import pandas as pd

# Load dataset
df = pd.read_csv("input/dataset.csv")

print("Original Dataset Shape:", df.shape)

# Remove unnecessary column
if "customerID" in df.columns:
    df.drop(columns=["customerID"], inplace=True)

# Convert TotalCharges to numeric
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

# Create customer value category
if "MonthlyCharges" in df.columns:
    df["Customer_Value"] = pd.cut(
        df["MonthlyCharges"],
        bins=[0, 50, 100, float("inf")],
        labels=["Low", "Medium", "High"]
    )

# Business rule
if "tenure" in df.columns:
    df["Customer_Segment"] = df["tenure"].apply(
        lambda x: "New Customer"
        if x < 12
        else "Existing Customer"
    )

# Generate summary
summary = df.groupby("Customer_Segment").size().reset_index(
    name="Customer_Count"
)

print("\nCustomer Segment Summary:")
print(summary)

# Save processed data
df.to_csv("output/processed_data.csv", index=False)

print("\nProcessed dataset saved successfully.")
