# 📊 Marketing Campaign Business Performance Analytics

> 🚀 An end-to-end Data Analytics and Business Intelligence project that transforms raw marketing campaign data into actionable business insights using Python, Excel, SQL Server, Advanced SQL, and Power BI.

---

## 📌 Project Overview

Marketing campaigns generate large amounts of data across different platforms, regions, audiences, content types, budgets, and performance metrics.

This project analyzes marketing campaign data to understand campaign effectiveness, customer engagement, conversion performance, revenue generation, advertising efficiency, and Return on Advertising Spend (ROAS).

The project follows a complete analytics workflow:

```text
📁 Raw Marketing Data
        ↓
🐍 Python Data Cleaning
        ↓
🔍 Exploratory Data Analysis
        ↓
📊 Business Analysis
        ↓
📁 Processed Fact & Dimension Data
        ↓
🗄️ SQL Server Database
        ↓
📈 SQL Business Analysis
        ↓
🚀 Advanced SQL Analytics
        ↓
📊 Power BI Dashboard
        ↓
💡 Business Insights
        ↓
🎯 Business Recommendations
```

---

# 🎯 Business Objectives

The main objectives of this project are:

- 🧹 Clean and validate marketing campaign data
- 🔍 Perform exploratory data analysis
- 📊 Calculate important marketing KPIs
- 💰 Analyze revenue and advertising spend
- 📈 Evaluate Return on Advertising Spend (ROAS)
- 🎯 Analyze conversion performance
- 📢 Compare marketing platforms
- 🌍 Analyze regional performance
- 👥 Analyze customer and audience segments
- 🎨 Evaluate content-type performance
- 📅 Analyze monthly campaign trends
- 🏆 Identify top-performing campaigns
- 💸 Identify overspending campaigns
- 🗄️ Build a structured SQL Server database
- ⭐ Implement a Star Schema
- 🚀 Perform advanced SQL analytics
- 📊 Build an interactive Power BI dashboard
- 💡 Generate actionable business recommendations

---

# 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Data cleaning, EDA, and analysis |
| 🐼 Pandas | Data manipulation and transformation |
| 📊 Matplotlib | Data visualization |
| 📗 Excel | Business analysis and reporting |
| 🗄️ SQL Server | Database management and analytics |
| 💻 SQL | Business analysis |
| 🚀 Advanced SQL | Window functions and advanced analytics |
| 📈 Power BI | Interactive dashboard and reporting |
| 🔢 DAX | KPI and calculated measures |
| 🔄 Power Query | Data transformation |
| ⭐ Star Schema | Data warehouse modeling |
| 🐙 GitHub | Project management and portfolio |

---

# 📂 Project Structure

```text
Marketing Campaign Business Performance Analytics/
│
├── 📁 data/
│   ├── 📁 raw/
│   │   └── Raw marketing campaign dataset
│   │
│   ├── 📁 processed/
│   │   ├── 📁 fact/
│   │   │   └── FactMarketingPerformance.csv
│   │   │
│   │   └── 📁 dimension/
│   │       ├── DimAge.csv
│   │       ├── DimContent.csv
│   │       ├── DimDate.csv
│   │       ├── DimGender.csv
│   │       ├── DimPlatform.csv
│   │       └── DimRegion.csv
│   │
│   ├── 📁 analysis_results/
│   │   └── Python analysis outputs
│   │
│   └── 📄 Marketing_Campaign_Cleaned.csv
│
├── 📁 python/
│   ├── 📁 notebooks/
│   │   ├── 01_Data_Cleaning.ipynb
│   │   ├── 02_EDA.ipynb
│   │   ├── 03_Business_Analysis.ipynb
│   │   └── 04_Advanced_Analytics.ipynb
│   │
│   └── 📁 scripts/
│       ├── 01_data_cleaning.py
│       ├── 02_eda.py
│       ├── 03_business_analysis.py
│       ├── 04_advanced_analysis.py
│       └── 05_export_results.py
│
├── 📁 excel/
│   └── 📊 Marketing_Campaign_Analysis.xlsx
│
├── 📁 sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── load.sql
│   ├── Business Analysis.sql
│   └── Advanced Analytics.sql
│
├── 📁 powerbi/
│   └── 📊 Marketing_Campaign_Business_Performance.pbix
│
├── 📁 images/
│   ├── Marketing Executive Overview.png
│   ├── Customer & Audience Analysis.png
│   ├── Campaign & Channel Performance.png
│   ├── Campaign Detail.png
│   └── Campaign Tooltip.png
│
└── 📄 README.md
```

---

# 📊 Dataset

The project contains **1,000 marketing campaign performance records**.

## Dataset Columns

```text
Campaign_ID
Budget
Clicks
CTR
CPC
Conversions
CPA
Conversion_Rate
Duration
Platform
Content_Type
Target_Age
Target_Gender
Region
Revenue
Spend
ROAS
Date
Impressions
```

---

# 🧹 Data Cleaning with Python

Python was used to clean, validate, transform, and prepare the marketing campaign dataset.

## 🔧 Data Cleaning Activities

- 🔍 Missing-value inspection
- 🧾 Data-type validation
- 🔢 Duplicate checks
- 🚫 Negative-value checks
- 📈 CTR validation
- 💰 Revenue validation
- 💸 Spend validation
- 🎯 Conversion validation
- 📅 Date formatting
- 🆔 Campaign ID validation
- 📐 KPI validation
- 📤 Clean dataset export

The final cleaned dataset is:

```text
data/Marketing_Campaign_Cleaned.csv
```

---

# 🔍 Exploratory Data Analysis

Python EDA was performed to identify patterns, trends, relationships, and anomalies in marketing campaign performance.

## 📌 EDA Areas

- 📊 Overall campaign performance
- 📢 Platform performance
- 🌍 Regional performance
- 🎨 Content performance
- 👥 Age-group performance
- ⚥ Gender performance
- 📅 Monthly performance
- 🏆 Top campaigns
- 🔗 Audience combinations
- ⚠️ Data-quality analysis
- 📈 Correlation analysis

---

# 💰 Key Business Metrics

| KPI | Value |
|---|---:|
| 💰 Total Budget | 5,961,990 |
| 💸 Total Spend | 5,956,167.80 |
| 💵 Total Revenue | 59,886,710 |
| 🖱️ Total Clicks | 1,013,229 |
| 🎯 Total Conversions | 505,672 |
| 📈 Average CTR | 25.84% |
| 🔄 Average Conversion Rate | 50.83% |
| 💵 Average CPA | 40.97 |
| 🚀 Average ROAS | 11.69 |

---

# 📢 Platform Performance

| Rank | Platform | ROAS |
|---|---|---:|
| 🥇 | Facebook | 13.04 |
| 🥈 | LinkedIn | 11.85 |
| 🥉 | Google | 11.58 |
| 4️⃣ | YouTube | 11.14 |
| 5️⃣ | Instagram | 10.81 |

### 💡 Insight

Facebook achieved the highest ROAS among the analyzed platforms, indicating strong advertising efficiency.

---

# 🌍 Regional Performance

| Region | ROAS |
|---|---:|
| 🌎 North America | 12.47 |
| 🇪🇺 Europe | 12.39 |
| 🌎 South America | 12.35 |
| 🌏 Asia | 12.24 |
| 🌍 Africa | 9.11 |

### 💡 Insight

North America generated the strongest regional ROAS, while Africa showed comparatively lower campaign efficiency.

---

# 🎨 Content Type Performance

| Content Type | ROAS |
|---|---:|
| 🎥 Video | 12.86 |
| 🎠 Carousel | 11.96 |
| 🖼️ Image | 11.69 |
| 📝 Text | 10.26 |

### 💡 Insight

Video content generated the highest ROAS among the analyzed content types.

---

# 👥 Customer & Audience Analysis

## 🎂 Age Group Performance

| Age Group | ROAS |
|---|---:|
| 🥇 25-34 | 12.39 |
| 🥈 55+ | 12.01 |
| 🥉 45-54 | 11.93 |
| 35-44 | 11.14 |
| 18-24 | 10.96 |

### 💡 Insight

The **25-34 age group** produced the highest ROAS among the analyzed age groups.

---

## ⚥ Gender Performance

| Gender | ROAS |
|---|---:|
| Other | 12.82 |
| Male | 11.53 |
| Female | 10.61 |

---

# 🔗 Revenue Correlation Analysis

The project analyzed the relationship between important marketing metrics and revenue.

| Metric | Correlation with Revenue |
|---|---:|
| 🎯 Conversions | 0.838 |
| 🚀 ROAS | 0.810 |
| 🔄 Conversion Rate | 0.551 |
| 🖱️ Clicks | 0.515 |
| 📈 CTR | 0.300 |
| 💸 Spend | 0.096 |
| 💰 Budget | 0.095 |
| 👁️ Impressions | -0.009 |
| 💵 CPC | -0.319 |
| 💸 CPA | -0.379 |

### 💡 Key Insight

Conversions showed the strongest positive relationship with revenue.

This suggests that conversion performance is an important factor when evaluating revenue generation.

> ⚠️ Correlation does not imply causation.

---

# ⚠️ Data Quality Analysis

The project includes automated data-quality checks.

### Findings

- ❌ Invalid CTR records: **26**
- ✅ Negative Budget values: **0**
- ✅ Negative Spend values: **0**
- ✅ Negative Revenue values: **0**
- ✅ Negative Clicks: **0**
- ✅ Negative Conversions: **0**
- ✅ Negative Impressions: **0**

These checks help identify potential data-quality problems before the data is used for business decision-making.

---

# 🗄️ SQL Server Database

A relational SQL Server database was created for structured storage and analysis.

## Database

```text
MarketingCampaignAnalytics
```

---

# ⭐ Star Schema

The database follows a Star Schema architecture.

```text
                         📅 DimDate
                            │
                            │
                            ▼
👤 DimAge ──────────► 📊 FactMarketingPerformance ◄──────── 📢 DimPlatform
                            ▲
                            │
🎨 DimContent ──────────────┤
                            │
⚥ DimGender ────────────────┤
                            │
🌍 DimRegion ───────────────┘
```

---

# 📦 Database Tables

## Dimension Tables

- 👤 `DimAge`
- 🎨 `DimContent`
- 📅 `DimDate`
- ⚥ `DimGender`
- 📢 `DimPlatform`
- 🌍 `DimRegion`

## Fact Table

- 📊 `FactMarketingPerformance`

The fact table contains measurable campaign performance data, while the dimension tables provide descriptive business context.

---

# 🔐 Database Design

The SQL Server database includes:

- 🔑 Primary keys
- 🔗 Foreign keys
- ⭐ Star Schema
- 🧩 Fact and dimension relationships
- 🆔 Identity-based `Fact_ID`
- 📊 One-to-many relationships
- 🔍 Referential integrity checks
- 🧹 Data-quality checks

Because `Campaign_ID` can occur across multiple records, `Fact_ID` is used as the primary key of the fact table.

---

# 📈 SQL Business Analysis

The `Business Analysis.sql` file contains business-focused SQL analysis.

## Analysis Includes

1. 📊 Overall marketing performance
2. 💰 Key marketing metrics
3. 📢 Platform performance
4. 🌍 Region performance
5. 🎨 Content type performance
6. 🎂 Age-group performance
7. ⚥ Gender performance
8. 📅 Monthly performance
9. 🏆 Top 10 campaigns by ROAS
10. 💵 Top 10 campaigns by revenue
11. 🎯 Top 10 campaigns by conversions
12. 🔗 Best audience combinations
13. 💸 Overspent campaigns
14. 📊 Budget utilization
15. 🧹 Data-quality checks
16. 🔐 Foreign-key integrity checks
17. ⚡ Campaign efficiency classification
18. 🌍 Platform + region performance
19. 📋 Final business summary

---

# 🚀 Advanced SQL Analytics

The `Advanced Analytics.sql` file extends the business analysis using advanced SQL techniques.

## 🧠 Advanced SQL Concepts

- 🔹 Common Table Expressions (`CTE`)
- 🔹 `LAG()`
- 🔹 `SUM() OVER()`
- 🔹 `RANK()`
- 🔹 `DENSE_RANK()`
- 🔹 `PARTITION BY`
- 🔹 Window functions
- 🔹 `CASE`
- 🔹 Running totals
- 🔹 Revenue contribution analysis
- 🔹 Month-over-month growth
- 🔹 Campaign ranking
- 🔹 Efficiency classification
- 🔹 Platform-region ranking

## 📌 Advanced Analyses

```text
📅 Month-over-month revenue growth
📈 Cumulative revenue
📢 Platform revenue contribution
🏆 Platform performance ranking
🎯 Campaign performance ranking
⚡ Campaign efficiency classification
💰 Revenue-to-spend efficiency
🌍 Platform + region ranking
📋 Advanced executive summary
🧹 Advanced data-quality summary
```

---

# 📊 Power BI Dashboard

Power BI was used to transform the analyzed marketing campaign data into an interactive Business Intelligence dashboard.

## 📌 Dashboard Pages

### 📊 1. Marketing Executive Overview

Provides a high-level view of marketing performance through key KPIs, revenue, spend, conversions, ROAS, and campaign trends.

### 👥 2. Customer & Audience Analysis

Analyzes marketing performance across age groups, gender, regions, and audience segments.

### 📢 3. Campaign & Channel Performance

Analyzes campaign performance across platforms, channels, content types, and campaign-level metrics.

### 🔎 4. Campaign Detail

Provides detailed information about individual campaigns and their performance metrics.

### 💬 5. Campaign Tooltip

Provides additional contextual campaign information through interactive Power BI tooltip functionality.

---

# 🎛️ Power BI Features

The dashboard includes:

- 💳 KPI Cards
- 📊 Bar Charts
- 🍩 Donut Charts
- 📈 Trend Analysis
- 🎛️ Interactive Slicers
- 🔍 Filters
- 📢 Platform Analysis
- 🌍 Regional Analysis
- 👥 Audience Analysis
- 🎨 Content Analysis
- 🏆 Campaign Performance
- 🔎 Campaign Details
- 💬 Interactive Tooltips
- 📅 Time-based Analysis

---

# 🖼️ Power BI Dashboard Preview

## 📊 Marketing Executive Overview

![Marketing Executive Overview](YOUR_IMAGE_LINK_HERE)

---

## 👥 Customer & Audience Analysis

![Customer & Audience Analysis](YOUR_IMAGE_LINK_HERE)

---

## 📢 Campaign & Channel Performance

![Campaign & Channel Performance](YOUR_IMAGE_LINK_HERE)

---

## 🔎 Campaign Detail

![Campaign Detail](YOUR_IMAGE_LINK_HERE)

---

## 💬 Campaign Tooltip

![Campaign Tooltip](YOUR_IMAGE_LINK_HERE)

---

# 💡 Key Business Insights

## 🥇 Facebook Has Strong Advertising Efficiency

Facebook achieved the highest ROAS among the analyzed platforms.

➡️ High-performing Facebook campaigns can be evaluated for additional investment.

---

## 🎥 Video Content Performs Strongly

Video campaigns generated the highest ROAS among the analyzed content types.

➡️ Increasing experimentation with high-quality video content may improve campaign efficiency.

---

## 👥 25-34 Is a Strong Audience Segment

The 25-34 age group generated the highest ROAS among the analyzed age groups.

➡️ This segment can be considered for targeted marketing campaigns.

---

## 🌎 North America Shows Strong Performance

North America achieved the highest regional ROAS.

➡️ Strong-performing campaigns in this region can be evaluated for expansion opportunities.

---

## 🎯 Conversions Are Strongly Related to Revenue

Conversions showed the strongest positive correlation with revenue.

➡️ Campaign optimization should focus on improving conversion quality, not only clicks and impressions.

---

## 💸 CPA Requires Monitoring

CPA showed a negative relationship with revenue in this dataset.

➡️ High-CPA campaigns should be reviewed to identify opportunities for cost optimization.

---

## ⚠️ Data Quality Requires Attention

The dataset contains **26 invalid CTR records**.

➡️ These records should be investigated and corrected before operational use.

---

# 🎯 Business Recommendations

### 📢 Platform Optimization

Prioritize high-performing platforms while continuing controlled testing of other channels.

### 🎥 Content Strategy

Increase experimentation with video and carousel campaigns.

### 👥 Audience Targeting

Focus on high-performing audience segments and use personalized targeting.

### 🌍 Regional Strategy

Evaluate additional investment in high-performing regions.

### 💸 Budget Optimization

Monitor campaigns where advertising spend exceeds allocated budgets.

### 🎯 Conversion Optimization

Improve conversion rates while reducing acquisition costs.

### 🧪 Continuous Experimentation

Use A/B testing to compare:

- 📢 Platforms
- 🎨 Content types
- 👥 Age groups
- ⚥ Gender
- 🌍 Regions
- 💰 Campaign budgets

---

# 🔄 End-to-End Analytics Pipeline

```text
                 📁 RAW DATA
                      │
                      ▼
              🐍 PYTHON CLEANING
                      │
                      ▼
               🔍 PYTHON EDA
                      │
                      ▼
             📊 BUSINESS ANALYSIS
                      │
                      ▼
              📁 PROCESSED DATA
                      │
                      ▼
              🗄️ SQL SERVER
                      │
              ┌───────┴───────┐
              ▼               ▼
       📈 BUSINESS SQL   🚀 ADVANCED SQL
              │               │
              └───────┬───────┘
                      ▼
                📊 POWER BI
                      │
                      ▼
                 💡 INSIGHTS
                      │
                      ▼
             🎯 RECOMMENDATIONS
```

---

# 🧠 Skills Demonstrated

## 🐍 Python

- Pandas
- Data cleaning
- Data transformation
- Exploratory data analysis
- Statistical analysis
- Correlation analysis
- Data validation
- Data visualization

## 🗄️ SQL Server

- Database creation
- Table creation
- Primary keys
- Foreign keys
- Joins
- Aggregations
- CTEs
- CASE statements
- Window functions
- `LAG()`
- `RANK()`
- `DENSE_RANK()`
- `PARTITION BY`
- Data-quality checks
- Referential integrity

## 📊 Power BI

- Data modeling
- Star Schema
- DAX
- KPI development
- Interactive dashboards
- Slicers
- Filters
- Drill-down analysis
- Tooltips
- Business reporting
- Data visualization

## 📗 Excel

- Data analysis
- KPI analysis
- Business reporting
- Data exploration

---

# 📁 Main Project Files

## 🐍 Python

```text
python/scripts/01_data_cleaning.py
python/scripts/02_eda.py
python/scripts/03_business_analysis.py
python/scripts/04_advanced_analysis.py
python/scripts/05_export_results.py
```

## 🗄️ SQL

```text
sql/create_database.sql
sql/create_tables.sql
sql/load.sql
sql/Business Analysis.sql
sql/Advanced Analytics.sql
```

## 📊 Data

```text
data/raw/
data/processed/
data/analysis_results/
data/Marketing_Campaign_Cleaned.csv
```

---

# 🏁 Project Outcome

This project demonstrates the complete lifecycle of a real-world analytics solution:

```text
📁 Raw Data
      ↓
🐍 Python Notebooks
      ↓
🧹 Data Cleaning
      ↓
🔍 EDA
      ↓
📊 Excel Analysis
      ↓
🗄️ SQL Server
      ↓
🚀 Advanced SQL Analytics
      ↓
📊 Power BI
      ↓
🖼️ Dashboard Images
      ↓
💡 Business Insights
      ↓
🎯 Recommendations
```

The project combines:

```text
🐍 Python
    +
📗 Excel
    +
🗄️ SQL Server
    +
🚀 Advanced SQL
    +
📊 Power BI
    =
💡 End-to-End Business Analytics Solution
```

---

# 🌟 Why This Project Matters

This project demonstrates that data analytics is not only about creating charts.

It covers the complete process of:

**Cleaning → Modeling → Analyzing → Visualizing → Interpreting → Recommending**

It demonstrates practical skills required for:

- 📊 Data Analyst roles
- 💼 Business Analyst roles
- 📈 Business Intelligence roles
- 🗄️ SQL Analytics roles

---

# 📌 Project Highlights

| Area | Achievement |
|---|---|
| 📊 Dataset | 1,000 campaign records |
| 🐍 Python | Cleaning + EDA + analysis |
| 📗 Excel | Business analysis |
| 🗄️ SQL Server | Relational analytics database |
| ⭐ Data Model | Star Schema |
| 🚀 Advanced SQL | CTE + Window Functions |
| 📈 Power BI | Interactive dashboard |
| 💵 Total Revenue | 59.89M |
| 💸 Total Spend | 5.96M |
| 🎯 Total Conversions | 505K+ |
| 🚀 Average ROAS | 11.69 |
| ⚠️ Invalid CTR Records | 26 |

---

# 📜 License

This project is created for educational, portfolio, and learning purposes.

---

# 👩‍💻 Author

## **Mahak Chauhan**

📊 Aspiring Data Analyst

### 💻 Technical Skills

`Python` • `SQL` • `Power BI` • `Excel` • `DAX` • `Pandas` • `SQL Server` • `Data Analysis` • `Data Visualization`

### 🚀 Project Focus

**Turning raw data into meaningful business insights and data-driven decisions.**

---

⭐ **If you find this project useful, consider giving the repository a star!**

📊 **Marketing Campaign Business Performance Analytics**

**From Raw Data → Business Insights → Better Decisions 🚀**