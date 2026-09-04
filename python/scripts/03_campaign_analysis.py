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

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Campaign summary
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

# -----------------------------
# Calculate campaign KPIs
# -----------------------------

campaign_summary["CTR"] = (
    campaign_summary["Clicks"] /
    campaign_summary["Impressions"]
)

campaign_summary["Conversion_Rate"] = (
    campaign_summary["Conversions"] /
    campaign_summary["Clicks"]
)

campaign_summary["CPA"] = (
    campaign_summary["Spend"] /
    campaign_summary["Conversions"]
)

campaign_summary["ROAS"] = (
    campaign_summary["Revenue"] /
    campaign_summary["Spend"]
)

campaign_summary["Budget_Utilization"] = (
    campaign_summary["Spend"] /
    campaign_summary["Budget"]
)

# -----------------------------
# Display campaign analysis
# -----------------------------

print("\nCampaign Summary:")
print(campaign_summary.head(10))

print("\nTop 10 Campaigns by ROAS:")
print(
    campaign_summary
    .sort_values("ROAS", ascending=False)
    .head(10)
)

print("\nTop 10 Campaigns by Revenue:")
print(
    campaign_summary
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\nTop 10 Campaigns by Conversions:")
print(
    campaign_summary
    .sort_values("Conversions", ascending=False)
    .head(10)
)

print("\nBottom 10 Campaigns by ROAS:")
print(
    campaign_summary
    .sort_values("ROAS", ascending=True)
    .head(10)
)

print("\nTop 10 Campaigns by CPA:")
print(
    campaign_summary
    .sort_values("CPA", ascending=False)
    .head(10)
)

print("\nTop 10 Campaigns by Budget Utilization:")
print(
    campaign_summary
    .sort_values("Budget_Utilization", ascending=False)
    .head(10)
)

# -----------------------------
# Campaign efficiency
# -----------------------------

campaign_summary["Efficiency_Flag"] = campaign_summary["ROAS"].apply(
    lambda x:
        "High ROAS" if x >= 15
        else "Moderate ROAS" if x >= 8
        else "Low ROAS"
)

print("\nCampaign Efficiency:")
print(
    campaign_summary["Efficiency_Flag"]
    .value_counts()
)

print("\nCampaign analysis completed successfully.")