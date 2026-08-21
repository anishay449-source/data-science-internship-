Project 2 — Python-Based Data Processing

Objective
The objective of this project is to use Python to process customer data, apply business rules, perform data transformations, and generate meaningful business-oriented outputs.
This project uses the Telco Customer Churn dataset to create customer segments, charge categories, estimated annual revenue, and churn-risk categories.

Dataset
Dataset: Telco Customer Churn

Source: Kaggle
https://www.kaggle.com/blastchar/telco-customer-churn

The dataset contains customer information such as:
- Customer ID
- Tenure
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Churn status

Processing Tasks
The Python script performs the following operations:
1. Loads the raw CSV dataset using Pandas.
2. Converts "TotalCharges" into a numeric data type.
3. Creates customer segments based on tenure.
4. Categorizes customers based on monthly charges.
5. Calculates estimated annual revenue.
6. Applies business rules to classify customers into churn-risk categories.
7. Generates a processed dataset.
8. Saves the processed data as a new CSV file.

Business Rules
Customer Segmentation
Customers are classified based on their tenure:

Tenure| Segment
0–12 months| New Customer
13–48 months| Established Customer
More than 48 months| Long-Term Customer

##Monthly Charge Classification
Customers are categorized according to monthly charges:
Monthly Charges| Category
Less than 40| Low Charge
40–69.99| Medium Charge
70 or more| High Charge

Estimated Annual Revenue
Estimated annual revenue is calculated using:
"Estimated Annual Revenue = Monthly Charges × 12"

Churn Risk Classification
A simple rule-based risk score is created using factors such as:
- Month-to-month contract
- Short tenure
- High monthly charges
- Electronic check payment method

Customers are then classified as:
- Low Risk
- Medium Risk
- High Risk

Python Libraries Used
- Python
- Pandas

Learning Outcomes
Through this project, I learned how to:
- Read and process CSV data using Pandas
- Apply conditional business logic
- Create new features from existing data
- Transform raw data into meaningful categories
- Generate business-oriented outputs
- Save processed data for further analysis

Conclusion

This project demonstrates how Python can be used to transform raw customer data into structured and meaningful information that can support business analysis and customer-retention strategies.
