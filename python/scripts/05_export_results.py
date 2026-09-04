from pathlib import Path
import pandas as pd

# -----------------------------
# Project paths
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CLEANED_FILE = (
    PROJECT_ROOT
    / "data"
    / "Marketing_Campaign_Cleaned.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "data"
    / "analysis_results"
)

# Create output folder if it does not exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load cleaned dataset
# -----------------------------

df = pd.read_csv(CLEANED_FILE)

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Create Month
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# -----------------------------
# 1. Platform Performance
# -----------------------------

platform_performance = (
    df.groupby("Platform")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
)

platform_performance["CTR"] = (
    platform_performance["Clicks"]
    / platform_performance["Impressions"]
)

platform_performance["Conversion_Rate"] = (
    platform_performance["Conversions"]
    / platform_performance["Clicks"]
)

platform_performance["CPA"] = (
    platform_performance["Spend"]
    / platform_performance["Conversions"]
)

platform_performance["ROAS"] = (
    platform_performance["Revenue"]
    / platform_performance["Spend"]
)

platform_performance = platform_performance.sort_values(
    "ROAS",
    ascending=False
)

# -----------------------------
# 2. Region Performance
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
    region_performance["Clicks"]
    / region_performance["Impressions"]
)

region_performance["Conversion_Rate"] = (
    region_performance["Conversions"]
    / region_performance["Clicks"]
)

region_performance["CPA"] = (
    region_performance["Spend"]
    / region_performance["Conversions"]
)

region_performance["ROAS"] = (
    region_performance["Revenue"]
    / region_performance["Spend"]
)

region_performance = region_performance.sort_values(
    "ROAS",
    ascending=False
)

# -----------------------------
# 3. Content Type Performance
# -----------------------------

content_performance = (
    df.groupby("Content_Type")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
)

content_performance["CTR"] = (
    content_performance["Clicks"]
    / content_performance["Impressions"]
)

content_performance["Conversion_Rate"] = (
    content_performance["Conversions"]
    / content_performance["Clicks"]
)

content_performance["CPA"] = (
    content_performance["Spend"]
    / content_performance["Conversions"]
)

content_performance["ROAS"] = (
    content_performance["Revenue"]
    / content_performance["Spend"]
)

content_performance = content_performance.sort_values(
    "ROAS",
    ascending=False
)

# -----------------------------
# 4. Top Campaigns by ROAS
# -----------------------------

campaign_summary = (
    df.groupby("Campaign_ID")
      .agg(
          Budget=("Budget", "sum"),
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Clicks=("Clicks", "sum"),
          Conversions=("Conversions", "sum"),
          Impressions=("Impressions", "sum")
      )
)

campaign_summary["CTR"] = (
    campaign_summary["Clicks"]
    / campaign_summary["Impressions"]
)

campaign_summary["Conversion_Rate"] = (
    campaign_summary["Conversions"]
    / campaign_summary["Clicks"]
)

campaign_summary["CPA"] = (
    campaign_summary["Spend"]
    / campaign_summary["Conversions"]
)

campaign_summary["ROAS"] = (
    campaign_summary["Revenue"]
    / campaign_summary["Spend"]
)

campaign_summary["Budget_Utilization"] = (
    campaign_summary["Spend"]
    / campaign_summary["Budget"]
)

top_campaigns_roas = (
    campaign_summary
    .sort_values("ROAS", ascending=False)
    .head(10)
)

# -----------------------------
# 5. Top Campaigns by Revenue
# -----------------------------

top_campaigns_revenue = (
    campaign_summary
    .sort_values("Revenue", ascending=False)
    .head(10)
)

# -----------------------------
# 6. Top Campaigns by Conversions
# -----------------------------

top_campaigns_conversions = (
    campaign_summary
    .sort_values("Conversions", ascending=False)
    .head(10)
)

# -----------------------------
# 7. Best Audience Combinations
# -----------------------------

best_audiences = (
    df.groupby(
        ["Target_Age", "Target_Gender", "Region"]
    )
    .agg(
        Spend=("Spend", "sum"),
        Revenue=("Revenue", "sum"),
        Conversions=("Conversions", "sum")
    )
)

best_audiences["CPA"] = (
    best_audiences["Spend"]
    / best_audiences["Conversions"]
)

best_audiences["ROAS"] = (
    best_audiences["Revenue"]
    / best_audiences["Spend"]
)

best_audiences = (
    best_audiences
    .sort_values("ROAS", ascending=False)
    .head(10)
)

# -----------------------------
# 8. Monthly Performance
# -----------------------------

monthly_performance = (
    df.groupby("Month")
      .agg(
          Spend=("Spend", "sum"),
          Revenue=("Revenue", "sum"),
          Conversions=("Conversions", "sum"),
          Clicks=("Clicks", "sum"),
          Impressions=("Impressions", "sum")
      )
      .sort_index()
)

monthly_performance["CTR"] = (
    monthly_performance["Clicks"]
    / monthly_performance["Impressions"]
)

monthly_performance["Conversion_Rate"] = (
    monthly_performance["Conversions"]
    / monthly_performance["Clicks"]
)

monthly_performance["CPA"] = (
    monthly_performance["Spend"]
    / monthly_performance["Conversions"]
)

monthly_performance["ROAS"] = (
    monthly_performance["Revenue"]
    / monthly_performance["Spend"]
)

# -----------------------------
# 9. Monthly ROAS and CPA
# -----------------------------

monthly_roas_cpa = monthly_performance[
    [
        "ROAS",
        "CPA",
        "Spend",
        "Revenue",
        "Conversions"
    ]
]

# -----------------------------
# Export results
# -----------------------------

platform_performance.to_csv(
    OUTPUT_DIR / "platform_performance.csv"
)

region_performance.to_csv(
    OUTPUT_DIR / "region_performance.csv"
)

content_performance.to_csv(
    OUTPUT_DIR / "content_performance.csv"
)

top_campaigns_roas.to_csv(
    OUTPUT_DIR / "top_campaigns_roas.csv"
)

top_campaigns_revenue.to_csv(
    OUTPUT_DIR / "top_campaigns_revenue.csv"
)

top_campaigns_conversions.to_csv(
    OUTPUT_DIR / "top_campaigns_conversions.csv"
)

best_audiences.to_csv(
    OUTPUT_DIR / "best_audience_combinations.csv"
)

monthly_performance.to_csv(
    OUTPUT_DIR / "monthly_performance.csv"
)

monthly_roas_cpa.to_csv(
    OUTPUT_DIR / "monthly_roas_cpa.csv"
)

print("All analysis results exported successfully.")
print(f"Output folder: {OUTPUT_DIR}")

# =========================================================
# FACT AND DIMENSION TABLE EXPORTS
# =========================================================

FACT_DIR = PROJECT_ROOT / "data" / "processed" / "fact"
DIMENSION_DIR = PROJECT_ROOT / "data" / "processed" / "dimension"

# Create folders if they do not exist
FACT_DIR.mkdir(parents=True, exist_ok=True)
DIMENSION_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# Dimension tables
# ---------------------------------------------------------

# DimAge
dim_age = (
    df[["Target_Age"]]
    .drop_duplicates()
    .sort_values("Target_Age")
    .reset_index(drop=True)
)

dim_age.insert(0, "Age_ID", range(1, len(dim_age) + 1))

dim_age.to_csv(
    DIMENSION_DIR / "DimAge.csv",
    index=False
)

# DimContent
dim_content = (
    df[["Content_Type"]]
    .drop_duplicates()
    .sort_values("Content_Type")
    .reset_index(drop=True)
)

dim_content.insert(0, "Content_ID", range(1, len(dim_content) + 1))

dim_content.to_csv(
    DIMENSION_DIR / "DimContent.csv",
    index=False
)

# DimGender
dim_gender = (
    df[["Target_Gender"]]
    .drop_duplicates()
    .sort_values("Target_Gender")
    .reset_index(drop=True)
)

dim_gender.insert(0, "Gender_ID", range(1, len(dim_gender) + 1))

dim_gender.to_csv(
    DIMENSION_DIR / "DimGender.csv",
    index=False
)

# DimPlatform
dim_platform = (
    df[["Platform"]]
    .drop_duplicates()
    .sort_values("Platform")
    .reset_index(drop=True)
)

dim_platform.insert(0, "Platform_ID", range(1, len(dim_platform) + 1))

dim_platform.to_csv(
    DIMENSION_DIR / "DimPlatform.csv",
    index=False
)

# DimRegion
dim_region = (
    df[["Region"]]
    .drop_duplicates()
    .sort_values("Region")
    .reset_index(drop=True)
)

dim_region.insert(0, "Region_ID", range(1, len(dim_region) + 1))

dim_region.to_csv(
    DIMENSION_DIR / "DimRegion.csv",
    index=False
)

# ---------------------------------------------------------
# DimDate
# ---------------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

dim_date = (
    df[["Date"]]
    .drop_duplicates()
    .sort_values("Date")
    .reset_index(drop=True)
)

dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Month_Number"] = dim_date["Date"].dt.month
dim_date["Month_Name"] = dim_date["Date"].dt.month_name()
dim_date["Quarter"] = "Q" + dim_date["Date"].dt.quarter.astype(str)

dim_date.insert(0, "Date_ID", range(1, len(dim_date) + 1))

dim_date.to_csv(
    DIMENSION_DIR / "DimDate.csv",
    index=False
)

# ---------------------------------------------------------
# Fact table
# ---------------------------------------------------------

fact = df.copy()

# Create lookup dictionaries from dimensions
age_lookup = dict(zip(dim_age["Target_Age"], dim_age["Age_ID"]))
content_lookup = dict(zip(dim_content["Content_Type"], dim_content["Content_ID"]))
gender_lookup = dict(zip(dim_gender["Target_Gender"], dim_gender["Gender_ID"]))
platform_lookup = dict(zip(dim_platform["Platform"], dim_platform["Platform_ID"]))
region_lookup = dict(zip(dim_region["Region"], dim_region["Region_ID"]))
date_lookup = dict(zip(dim_date["Date"], dim_date["Date_ID"]))

# Add foreign keys
fact["Age_ID"] = fact["Target_Age"].map(age_lookup)
fact["Content_ID"] = fact["Content_Type"].map(content_lookup)
fact["Gender_ID"] = fact["Target_Gender"].map(gender_lookup)
fact["Platform_ID"] = fact["Platform"].map(platform_lookup)
fact["Region_ID"] = fact["Region"].map(region_lookup)
fact["Date_ID"] = fact["Date"].map(date_lookup)

# Select fact table columns
fact = fact[
    [
        "Campaign_ID",
        "Age_ID",
        "Content_ID",
        "Gender_ID",
        "Platform_ID",
        "Region_ID",
        "Date_ID",
        "Budget",
        "Clicks",
        "CTR",
        "CPC",
        "Conversions",
        "CPA",
        "Conversion_Rate",
        "Duration",
        "Revenue",
        "Spend",
        "ROAS",
        "Impressions"
    ]
]

fact.to_csv(
    FACT_DIR / "FactMarketingPerformance.csv",
    index=False
)

print("\nFact and dimension tables exported successfully.")