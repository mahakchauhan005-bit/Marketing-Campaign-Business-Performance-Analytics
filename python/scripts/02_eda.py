from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Location of the cleaned CSV file
CLEANED_FILE = PROJECT_ROOT / "data" / "Marketing_Campaign_Cleaned.csv"

# Load the cleaned dataset
df = pd.read_csv(CLEANED_FILE)

# -----------------------------
# Initial inspection
# -----------------------------

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

df.describe()
df["Platform"].unique()
df.groupby("Platform")["ROAS"].mean()
df.groupby("Platform")["Revenue"].mean()

print("\nBusiness Summary:")

print("Total Budget:", df["Budget"].sum())
print("Total Spend:", df["Spend"].sum())
print("Total Revenue:", df["Revenue"].sum())
print("Total Clicks:", df["Clicks"].sum())
print("Total Conversions:", df["Conversions"].sum())

print("Average CTR:", df["CTR"].mean())
print("Average Conversion Rate:", df["Conversion_Rate"].mean())
print("Average CPA:", df["CPA"].mean())
print("Average ROAS:", df["ROAS"].mean())

print("\nPlatform Performance:")

platform_performance = (
    df.groupby("Platform")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CTR": "mean",
          "Conversion_Rate": "mean",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(platform_performance)

print("\nRegion Performance:")

region_performance = (
    df.groupby("Region")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CTR": "mean",
          "Conversion_Rate": "mean",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(region_performance)

print("\nContent Type Performance:")

content_performance = (
    df.groupby("Content_Type")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CTR": "mean",
          "Conversion_Rate": "mean",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(content_performance)

print("\nTarget Age Performance:")

age_performance = (
    df.groupby("Target_Age")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CTR": "mean",
          "Conversion_Rate": "mean",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(age_performance)

print("\nTarget Gender Performance:")

gender_performance = (
    df.groupby("Target_Gender")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CTR": "mean",
          "Conversion_Rate": "mean",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(gender_performance)

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("\nMonthly Performance:")

monthly_performance = (
    df.groupby("Month")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "Clicks": "sum",
          "Impressions": "sum"
      })
      .sort_index()
)

print(monthly_performance)

print("\nTop 10 Campaigns by ROAS:")

top_campaigns_roas = (
    df.groupby("Campaign_ID")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
      .head(10)
)

print(top_campaigns_roas)

print("\nTop 10 Campaigns by Revenue:")

top_campaigns_revenue = (
    df.groupby("Campaign_ID")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "ROAS": "mean"
      })
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print(top_campaigns_revenue)

print("\nTop 10 Campaigns by Conversions:")

top_campaigns_conversions = (
    df.groupby("Campaign_ID")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("Conversions", ascending=False)
      .head(10)
)

print(top_campaigns_conversions)

print("\nAudience Combination Performance:")

audience_performance = (
    df.groupby(["Target_Age", "Target_Gender", "Region"])
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(audience_performance.head(10))

print("\nInvalid Value Checks:")

print("Negative Budget:", (df["Budget"] < 0).sum())
print("Negative Spend:", (df["Spend"] < 0).sum())
print("Negative Revenue:", (df["Revenue"] < 0).sum())
print("Negative Clicks:", (df["Clicks"] < 0).sum())
print("Negative Conversions:", (df["Conversions"] < 0).sum())
print("Negative Impressions:", (df["Impressions"] < 0).sum())
print("Negative ROAS:", (df["ROAS"] < 0).sum())

print("CTR outside 0-1:", ((df["CTR"] < 0) | (df["CTR"] > 1)).sum())
print(
    "Conversion Rate outside 0-1:",
    ((df["Conversion_Rate"] < 0) | (df["Conversion_Rate"] > 1)).sum()
)


print("\nKey Metric Summary:")

print(
    df[
        [
            "Budget",
            "Spend",
            "Revenue",
            "Clicks",
            "Conversions",
            "CTR",
            "Conversion_Rate",
            "CPA",
            "ROAS"
        ]
    ].describe()
)

print("\nCorrelation Matrix:")

correlation_matrix = df[
    [
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
].corr()

print(correlation_matrix)

print("\nCorrelation with Revenue:")

revenue_correlations = (
    correlation_matrix["Revenue"]
    .sort_values(ascending=False)
)

print(revenue_correlations)

print("\nInvalid CTR Records:")

invalid_ctr = df[
    (df["CTR"] < 0) | (df["CTR"] > 1)
]

print(
    invalid_ctr[
        ["Campaign_ID", "CTR", "Clicks", "Impressions", "Platform"]
    ]
)

print("\nCalculated CTR Comparison:")

df["Calculated_CTR"] = df["Clicks"] / df["Impressions"]

df["CTR_Difference"] = df["CTR"] - df["Calculated_CTR"]

print(
    df[
        ["Campaign_ID", "CTR", "Calculated_CTR", "CTR_Difference"]
    ].head(10)
)

print("\nLargest CTR Differences:")

largest_ctr_difference = (
    df[
        [
            "Campaign_ID",
            "CTR",
            "Calculated_CTR",
            "CTR_Difference"
        ]
    ]
    .assign(
        Absolute_Difference=lambda x: x["CTR_Difference"].abs()
    )
    .sort_values("Absolute_Difference", ascending=False)
    .head(10)
)

print(largest_ctr_difference)

print("\nCampaign Summary:")

campaign_summary = (
    df.groupby("Campaign_ID")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(campaign_summary)

print("\nBottom 10 Campaigns by ROAS:")

bottom_10_roas = (
    campaign_summary
    .sort_values("ROAS", ascending=True)
    .head(10)
)

print(bottom_10_roas)

print("\nTop 10 Campaigns by CPA:")

top_10_cpa = (
    campaign_summary
    .sort_values("CPA", ascending=False)
    .head(10)
)

print(top_10_cpa)

print("\nCampaign Efficiency:")

df["Efficiency_Flag"] = df["ROAS"].apply(
    lambda x: "High ROAS" if x >= 15
    else "Moderate ROAS" if x >= 8
    else "Low ROAS"
)

print(df["Efficiency_Flag"].value_counts())

print("\nROAS Category Counts:")

roas_categories = pd.cut(
    df["ROAS"],
    bins=[-float("inf"), 8, 15, float("inf")],
    labels=["Low ROAS", "Moderate ROAS", "High ROAS"]
)

print(roas_categories.value_counts())

print("\nAge and Gender Performance:")

age_gender_performance = (
    df.groupby(["Target_Age", "Target_Gender"])
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(age_gender_performance)

print("\nRegion and Platform Performance:")

region_platform_performance = (
    df.groupby(["Region", "Platform"])
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(region_platform_performance)

print("\nBest Audience Combinations:")

best_audiences = (
    df.groupby(["Target_Age", "Target_Gender", "Region"])
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
      .head(10)
)

print(best_audiences)

print("\nCampaigns Where Spend Exceeds Budget:")

overspent_campaigns = df[df["Spend"] > df["Budget"]]

print(
    overspent_campaigns[
        ["Campaign_ID", "Budget", "Spend", "Revenue", "ROAS"]
    ].sort_values("Spend", ascending=False)
)


print("\nBudget Utilization:")

df["Budget_Utilization"] = df["Spend"] / df["Budget"]

print(
    df[
        ["Campaign_ID", "Budget", "Spend", "Budget_Utilization"]
    ].head(10)
)

print("\nTop 10 Campaigns by Budget Utilization:")

top_10_budget_utilization = (
    df[
        [
            "Campaign_ID",
            "Budget",
            "Spend",
            "Revenue",
            "ROAS",
            "Budget_Utilization"
        ]
    ]
    .sort_values("Budget_Utilization", ascending=False)
    .head(10)
)

print(top_10_budget_utilization)


print("\nDuration vs Campaign Performance:")

duration_performance = (
    df.groupby("Duration")
      .agg({
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum",
          "CPA": "mean",
          "ROAS": "mean"
      })
      .sort_values("ROAS", ascending=False)
)

print(duration_performance)


print("\nDuration Correlation with Key Metrics:")

duration_correlation = df[
    [
        "Duration",
        "Spend",
        "Revenue",
        "Conversions",
        "ROAS"
    ]
].corr()["Duration"].sort_values(ascending=False)

print(duration_correlation)

print("\nMonthly ROAS and CPA Trends:")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_roas_cpa = (
    df.groupby("Month")
      .agg({
          "ROAS": "mean",
          "CPA": "mean",
          "Spend": "sum",
          "Revenue": "sum",
          "Conversions": "sum"
      })
      .sort_index()
)

print(monthly_roas_cpa)

platform_revenue = (
    df.groupby("Platform")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

platform_revenue.plot(kind="bar", title="Revenue by Platform")

plt.xlabel("Platform")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

platform_roas = (
    df.groupby("Platform")["ROAS"]
      .mean()
      .sort_values(ascending=False)
)

platform_roas.plot(kind="bar", title="ROAS by Platform")

plt.xlabel("Platform")
plt.ylabel("ROAS")
plt.tight_layout()
plt.show()

region_revenue = (
    df.groupby("Region")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

region_revenue.plot(kind="bar", title="Revenue by Region")

plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

monthly_revenue = (
    df.groupby("Month")["Revenue"]
      .sum()
      .sort_index()
)

monthly_revenue.plot(kind="line", marker="o", title="Monthly Revenue")

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

content_roas = (
    df.groupby("Content_Type")["ROAS"]
      .mean()
      .sort_values(ascending=False)
)

content_roas.plot(kind="bar", title="ROAS by Content Type")

plt.xlabel("Content Type")
plt.ylabel("ROAS")
plt.tight_layout()
plt.show()

OUTPUT_DIR = PROJECT_ROOT / "data" / "analysis_results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

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

print("\nAnalysis results exported successfully.")

print("\nEDA completed successfully.")
print("Rows analyzed:", len(df))
print("Columns analyzed:", len(df.columns))
