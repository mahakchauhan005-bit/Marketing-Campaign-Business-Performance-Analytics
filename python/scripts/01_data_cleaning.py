from pathlib import Path
import pandas as pd

# Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Location of the raw Excel file
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "ppc_campaign_performance_data.xlsx"

# Load the raw dataset
df = pd.read_excel(RAW_FILE)

# -----------------------------
# Initial inspection
# -----------------------------

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# -----------------------------
# Data types before cleaning
# -----------------------------

print("\nData types before cleaning:")
print(df.dtypes)

print("\nData info:")
df.info()

# -----------------------------
# Convert Date to datetime
# -----------------------------

print("\nDate data type before conversion:")
print(df["Date"].dtype)

df["Date"] = pd.to_datetime(df["Date"])

print("\nDate data type after conversion:")
print(df["Date"].dtype)

# -----------------------------
# Convert numeric columns
# -----------------------------

numeric_columns = [
    "Budget",
    "Clicks",
    "CTR",
    "CPC",
    "Conversions",
    "CPA",
    "Conversion_Rate",
    "Revenue",
    "Spend",
    "ROAS",
    "Impressions"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# -----------------------------
# Check final data types
# -----------------------------

print("\nData types after cleaning:")
print(df.dtypes)

OUTPUT_FILE = PROJECT_ROOT / "data" / "Marketing_Campaign_Cleaned.csv"

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)