from pathlib import Path
import pandas as pd

# -----------------------------
# Project paths
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CLEANED_FILE = PROJECT_ROOT / "data" / "Marketing_Campaign_Cleaned.csv"

# -----------------------------
# Load cleaned dataset
# -----------------------------

df = pd.read_csv(CLEANED_FILE)

# -----------------------------
# Audience by Target Age
# -----------------------------

age_performance = (
    df.groupby("Target_Age")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
)

age_performance["CTR"] = (
    age_performance["Clicks"] /
    age_performance["Impressions"]
)

age_performance["Conversion_Rate"] = (
    age_performance["Conversions"] /
    age_performance["Clicks"]
)

age_performance["CPA"] = (
    age_performance["Spend"] /
    age_performance["Conversions"]
)

age_performance["ROAS"] = (
    age_performance["Revenue"] /
    age_performance["Spend"]
)

print("\nAudience Performance by Age:")
print(age_performance.sort_values("ROAS", ascending=False))

# -----------------------------
# Audience by Target Gender
# -----------------------------

gender_performance = (
    df.groupby("Target_Gender")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
)

gender_performance["CTR"] = (
    gender_performance["Clicks"] /
    gender_performance["Impressions"]
)

gender_performance["Conversion_Rate"] = (
    gender_performance["Conversions"] /
    gender_performance["Clicks"]
)

gender_performance["CPA"] = (
    gender_performance["Spend"] /
    gender_performance["Conversions"]
)

gender_performance["ROAS"] = (
    gender_performance["Revenue"] /
    gender_performance["Spend"]
)

print("\nAudience Performance by Gender:")
print(gender_performance.sort_values("ROAS", ascending=False))

# -----------------------------
# Audience by Region
# -----------------------------

region_performance = (
    df.groupby("Region")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
)

region_performance["CTR"] = (
    region_performance["Clicks"] /
    region_performance["Impressions"]
)

region_performance["Conversion_Rate"] = (
    region_performance["Conversions"] /
    region_performance["Clicks"]
)

region_performance["CPA"] = (
    region_performance["Spend"] /
    region_performance["Conversions"]
)

region_performance["ROAS"] = (
    region_performance["Revenue"] /
    region_performance["Spend"]
)

print("\nAudience Performance by Region:")
print(region_performance.sort_values("ROAS", ascending=False))

# -----------------------------
# Age + Gender combinations
# -----------------------------

age_gender_performance = (
    df.groupby(["Target_Age", "Target_Gender"])
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum")
      )
)

age_gender_performance["CPA"] = (
    age_gender_performance["Spend"] /
    age_gender_performance["Conversions"]
)

age_gender_performance["ROAS"] = (
    age_gender_performance["Revenue"] /
    age_gender_performance["Spend"]
)

print("\nAge + Gender Performance:")
print(
    age_gender_performance
    .sort_values("ROAS", ascending=False)
    .head(10)
)

# -----------------------------
# Age + Gender + Region
# -----------------------------

best_audience_combinations = (
    df.groupby(["Target_Age", "Target_Gender", "Region"])
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum")
      )
)

best_audience_combinations["CPA"] = (
    best_audience_combinations["Spend"] /
    best_audience_combinations["Conversions"]
)

best_audience_combinations["ROAS"] = (
    best_audience_combinations["Revenue"] /
    best_audience_combinations["Spend"]
)

print("\nTop 10 Audience Combinations:")
print(
    best_audience_combinations
    .sort_values("ROAS", ascending=False)
    .head(10)
)

print("\nAudience analysis completed successfully.")