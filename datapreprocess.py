# ---------------------------------------------
# TOURISM DATA PREPROCESSING (WITHOUT OUTLIERS REMOVAL)
# ---------------------------------------------

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\polka\OneDrive\Desktop\Tourist influx prediction\Tourism dataset.csv")   # Change path if needed

print("Original Shape:", df.shape)

# ---------------------------------------------
# 1️⃣ BASIC INFORMATION
# ---------------------------------------------
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# ---------------------------------------------
# 2️⃣ REMOVE DUPLICATES
# ---------------------------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#remane columns
df.rename(columns={'2014 4th quarter (Oct-Dec))':
                   '2014 4th quarter (Oct-Dec)'}, inplace=True)
# ---------------------------------------------
# 3️⃣ HANDLE MISSING VALUES
# ---------------------------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.median()))

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ---------------------------------------------
# 4️⃣ CLEAN COLUMN NAMES
# ---------------------------------------------
df.columns = df.columns.str.strip()

# ---------------------------------------------
# 5️⃣ CONVERT QUARTER COLUMNS TO NUMERIC
# ---------------------------------------------
for col in df.columns:
    if "quarter" in col.lower():
        df[col] = pd.to_numeric(df[col], errors='coerce')

# ---------------------------------------------
# 6️⃣ CREATE TOTAL INFLOW COLUMN
# ---------------------------------------------
tourism_cols = [col for col in df.columns if "quarter" in col.lower()]

if tourism_cols:
    df["Total_Inflow"] = df[tourism_cols].sum(axis=1)

# ---------------------------------------------
# 7️⃣ FINAL CHECK
# ---------------------------------------------
print("\nFinal Shape:", df.shape)
print("\nFinal Missing Values:")
print(df.isnull().sum())

# ---------------------------------------------
# 8️⃣ SAVE CLEANED DATASET
# ---------------------------------------------
df.to_csv("Preprocessed_Tourism_Dataset.csv", index=False)

print("\nPreprocessing Completed Successfully!")