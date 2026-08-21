# Project 3 — Data Cleaning & Preparation

## Objective

The objective of this project is to prepare a raw customer churn dataset for analysis by inspecting its structure, identifying data-quality issues, handling missing values, removing duplicate records, correcting data types, and creating a clean, analysis-ready dataset.

## Dataset

**Dataset:** Telco Customer Churn

**Source:** Kaggle
https://www.kaggle.com/blastchar/telco-customer-churn

The dataset contains customer information including:

* Customer ID
* Gender
* Senior Citizen status
* Partner and Dependents
* Tenure
* Phone and Internet services
* Contract type
* Payment method
* Monthly charges
* Total charges
* Churn status

## Data Cleaning Tasks

The following data preparation steps were performed:

### 1. Dataset Inspection

The dataset was inspected to understand:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Duplicate records
* Basic numerical information

### 2. Duplicate Detection

Duplicate rows were identified using Pandas and removed to prevent duplicate customer records from affecting the analysis.

### 3. Data Type Correction

The `TotalCharges` column requires numeric analysis. It was converted from a string/object representation to a numeric data type.

Non-numeric values were converted to missing values during the conversion process.

### 4. Missing Value Handling

Missing values were identified after converting `TotalCharges`.

Missing `TotalCharges` values were handled using median imputation.

### 5. Categorical Data Standardization

Leading and trailing spaces were removed from selected categorical columns to maintain consistent category values.

### 6. Numerical Validation

Numerical columns such as:
* `tenure`
* `MonthlyCharges`
* `TotalCharges`
were checked for invalid negative values.

### 7. Clean Dataset Creation

After completing the cleaning process, the cleaned dataset was saved as:
dataset/cleaned_telco_churn.csv

## Python Libraries Used
* Python
* Pandas
* NumPy

## Project Structure
Project-3-Data-Cleaning-Preparation/
│
├── README.md
└── data_cleaning.py

## Input
dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv

## Output
dataset/cleaned_telco_churn.csv

## Data Quality Checks
The script checks:
* Dataset shape
* Data types
* Missing values
* Duplicate records
* Invalid numerical values
* Final dataset structure

## Learning Outcomes

Through this project, I learned how to:
* Inspect a raw dataset
* Identify data-quality problems
* Detect duplicate records
* Handle missing values
* Convert incorrect data types
* Standardize categorical values
* Validate numerical data
* Create an analysis-ready dataset

## Conclusion
Data cleaning is an important step before performing exploratory analysis or statistical analysis. The cleaned Telco Customer Churn dataset can now be used for further analysis, visualization, and statistical testing.

