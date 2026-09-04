-- Select the project database
USE MarketingCampaignAnalytics;
GO

-- ============================================================
-- 1. OVERALL MARKETING PERFORMANCE
-- ============================================================

SELECT
    COUNT(*) AS Total_Records,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,
    SUM(Impressions) AS Total_Impressions,
    SUM(Clicks) AS Total_Clicks,
    SUM(Conversions) AS Total_Conversions
FROM FactMarketingPerformance;
GO

-- ============================================================
-- 2. KEY MARKETING PERFORMANCE METRICS
-- ============================================================

SELECT
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,
    SUM(Conversions) AS Total_Conversions,

    -- Overall CTR
    CAST(SUM(Clicks) AS FLOAT)
        / NULLIF(SUM(Impressions), 0) AS Overall_CTR,

    -- Overall Conversion Rate
    CAST(SUM(Conversions) AS FLOAT)
        / NULLIF(SUM(Clicks), 0) AS Overall_Conversion_Rate,

    -- Overall CPA
    SUM(Spend)
        / NULLIF(SUM(Conversions), 0) AS Overall_CPA,

    -- Overall ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS Overall_ROAS

FROM FactMarketingPerformance;
GO

-- ============================================================
-- 3. PLATFORM PERFORMANCE
-- ============================================================

SELECT
    p.Platform,
    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Platform CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Platform Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Platform CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Platform ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimPlatform p
    ON f.Platform_ID = p.Platform_ID

GROUP BY
    p.Platform

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 4. REGION PERFORMANCE
-- ============================================================

SELECT
    r.Region,
    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Region CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Region Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Region CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Region ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimRegion r
    ON f.Region_ID = r.Region_ID

GROUP BY
    r.Region

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 5. CONTENT TYPE PERFORMANCE
-- ============================================================

SELECT
    c.Content_Type,
    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Content CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Content Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Content CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Content ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimContent c
    ON f.Content_ID = c.Content_ID

GROUP BY
    c.Content_Type

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 6. AGE GROUP PERFORMANCE
-- ============================================================

SELECT
    a.Target_Age,
    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Age Group CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Age Group Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Age Group CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Age Group ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimAge a
    ON f.Age_ID = a.Age_ID

GROUP BY
    a.Target_Age

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 7. GENDER PERFORMANCE
-- ============================================================

SELECT
    g.Target_Gender,
    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Gender CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Gender Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Gender CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Gender ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimGender g
    ON f.Gender_ID = g.Gender_ID

GROUP BY
    g.Target_Gender

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 8. MONTHLY MARKETING PERFORMANCE
-- ============================================================

SELECT
    YEAR(d.Date) AS Performance_Year,
    MONTH(d.Date) AS Performance_Month,

    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Clicks) AS Total_Clicks,
    SUM(f.Conversions) AS Total_Conversions,

    -- Monthly CTR
    CAST(SUM(f.Clicks) AS FLOAT)
        / NULLIF(SUM(f.Impressions), 0) AS CTR,

    -- Monthly Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- Monthly CPA
    SUM(f.Spend)
        / NULLIF(SUM(f.Conversions), 0) AS CPA,

    -- Monthly ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimDate d
    ON f.Date_ID = d.Date_ID

GROUP BY
    YEAR(d.Date),
    MONTH(d.Date)

ORDER BY
    Performance_Year,
    Performance_Month;
GO


-- ============================================================
-- 9. TOP 10 CAMPAIGNS BY ROAS
-- ============================================================

SELECT TOP 10
    Campaign_ID,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,
    SUM(Conversions) AS Total_Conversions,

    -- Campaign ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS ROAS

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 10. TOP 10 CAMPAIGNS BY REVENUE
-- ============================================================

SELECT TOP 10
    Campaign_ID,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,
    SUM(Conversions) AS Total_Conversions,

    -- Campaign ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS ROAS

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    Total_Revenue DESC;
GO


-- ============================================================
-- 11. TOP 10 CAMPAIGNS BY CONVERSIONS
-- ============================================================

SELECT TOP 10
    Campaign_ID,
    SUM(Conversions) AS Total_Conversions,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,

    -- Campaign ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS ROAS

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    Total_Conversions DESC;
GO


-- ============================================================
-- 12. BEST AUDIENCE COMBINATIONS
-- ============================================================

SELECT TOP 20
    a.Target_Age,
    g.Target_Gender,
    r.Region,
    p.Platform,

    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Conversions) AS Total_Conversions,

    -- Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimAge a
    ON f.Age_ID = a.Age_ID

JOIN DimGender g
    ON f.Gender_ID = g.Gender_ID

JOIN DimRegion r
    ON f.Region_ID = r.Region_ID

JOIN DimPlatform p
    ON f.Platform_ID = p.Platform_ID

GROUP BY
    a.Target_Age,
    g.Target_Gender,
    r.Region,
    p.Platform

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 13. OVERSPENT CAMPAIGNS
-- ============================================================

SELECT
    Campaign_ID,
    SUM(Budget) AS Total_Budget,
    SUM(Spend) AS Total_Spend,

    -- Amount overspent
    SUM(Spend) - SUM(Budget) AS Overspent_Amount,

    -- Budget utilization
    CAST(SUM(Spend) AS FLOAT)
        / NULLIF(SUM(Budget), 0) AS Budget_Utilization,

    SUM(Revenue) AS Total_Revenue,

    -- ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS ROAS

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

HAVING
    SUM(Spend) > SUM(Budget)

ORDER BY
    Overspent_Amount DESC;
GO


-- ============================================================
-- 14. BUDGET UTILIZATION ANALYSIS
-- ============================================================

SELECT
    Campaign_ID,
    SUM(Budget) AS Total_Budget,
    SUM(Spend) AS Total_Spend,

    -- Percentage of budget used
    CAST(SUM(Spend) AS FLOAT)
        / NULLIF(SUM(Budget), 0) * 100 AS Budget_Utilization_Percent,

    -- Remaining budget
    SUM(Budget) - SUM(Spend) AS Remaining_Budget

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    Budget_Utilization_Percent DESC;
GO


-- ============================================================
-- 15. DATA QUALITY CHECKS
-- ============================================================

-- Check negative values
SELECT
    COUNT(*) AS Negative_Value_Records
FROM FactMarketingPerformance
WHERE
    Budget < 0
    OR Spend < 0
    OR Revenue < 0
    OR Clicks < 0
    OR Conversions < 0
    OR Impressions < 0;
GO


-- Check duplicate Campaign_ID records
-- Campaign_ID is allowed to repeat because the fact table
-- contains multiple performance observations.
SELECT
    Campaign_ID,
    COUNT(*) AS Record_Count
FROM FactMarketingPerformance
GROUP BY
    Campaign_ID
HAVING
    COUNT(*) > 1
ORDER BY
    Record_Count DESC;
GO


-- Check missing Campaign_ID
SELECT
    COUNT(*) AS Missing_Campaign_ID
FROM FactMarketingPerformance
WHERE Campaign_ID IS NULL;
GO


-- Check invalid CTR values
SELECT
    COUNT(*) AS Invalid_CTR_Records
FROM FactMarketingPerformance
WHERE CTR < 0
   OR CTR > 1;
GO


-- ============================================================
-- 16. FOREIGN KEY INTEGRITY CHECKS
-- ============================================================

-- Invalid Age IDs
SELECT COUNT(*) AS Invalid_Age_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimAge d
    ON f.Age_ID = d.Age_ID
WHERE d.Age_ID IS NULL;
GO


-- Invalid Content IDs
SELECT COUNT(*) AS Invalid_Content_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimContent d
    ON f.Content_ID = d.Content_ID
WHERE d.Content_ID IS NULL;
GO


-- Invalid Gender IDs
SELECT COUNT(*) AS Invalid_Gender_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimGender d
    ON f.Gender_ID = d.Gender_ID
WHERE d.Gender_ID IS NULL;
GO


-- Invalid Platform IDs
SELECT COUNT(*) AS Invalid_Platform_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimPlatform d
    ON f.Platform_ID = d.Platform_ID
WHERE d.Platform_ID IS NULL;
GO


-- Invalid Region IDs
SELECT COUNT(*) AS Invalid_Region_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimRegion d
    ON f.Region_ID = d.Region_ID
WHERE d.Region_ID IS NULL;
GO


-- Invalid Date IDs
SELECT COUNT(*) AS Invalid_Date_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimDate d
    ON f.Date_ID = d.Date_ID
WHERE d.Date_ID IS NULL;
GO


-- ============================================================
-- 17. CAMPAIGN EFFICIENCY CLASSIFICATION
-- ============================================================

SELECT
    Campaign_ID,

    SUM(Budget) AS Total_Budget,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,

    -- ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS ROAS,

    -- Efficiency classification
    CASE
        WHEN SUM(Revenue) / NULLIF(SUM(Spend), 0) >= 12
            THEN 'High Performing'

        WHEN SUM(Revenue) / NULLIF(SUM(Spend), 0) >= 8
            THEN 'Average Performing'

        ELSE 'Low Performing'
    END AS Performance_Category

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 18. PLATFORM + REGION PERFORMANCE
-- ============================================================

SELECT
    p.Platform,
    r.Region,

    COUNT(*) AS Campaign_Count,
    SUM(f.Spend) AS Total_Spend,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Conversions) AS Total_Conversions,

    -- Conversion Rate
    CAST(SUM(f.Conversions) AS FLOAT)
        / NULLIF(SUM(f.Clicks), 0) AS Conversion_Rate,

    -- ROAS
    SUM(f.Revenue)
        / NULLIF(SUM(f.Spend), 0) AS ROAS

FROM FactMarketingPerformance f

JOIN DimPlatform p
    ON f.Platform_ID = p.Platform_ID

JOIN DimRegion r
    ON f.Region_ID = r.Region_ID

GROUP BY
    p.Platform,
    r.Region

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 19. FINAL BUSINESS SUMMARY
-- ============================================================

SELECT
    COUNT(*) AS Total_Records,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,
    SUM(Conversions) AS Total_Conversions,

    -- Overall ROAS
    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS Overall_ROAS,

    -- Overall CTR
    CAST(SUM(Clicks) AS FLOAT)
        / NULLIF(SUM(Impressions), 0) AS Overall_CTR,

    -- Overall Conversion Rate
    CAST(SUM(Conversions) AS FLOAT)
        / NULLIF(SUM(Clicks), 0) AS Overall_Conversion_Rate,

    -- Overall CPA
    SUM(Spend)
        / NULLIF(SUM(Conversions), 0) AS Overall_CPA

FROM FactMarketingPerformance;
GO


-- ============================================================
-- FINAL SQL DATABASE VALIDATION
-- ============================================================

USE MarketingCampaignAnalytics;
GO

-- Check all project tables and their row counts
SELECT
    t.name AS Table_Name,
    SUM(p.rows) AS Row_Count
FROM sys.tables t
INNER JOIN sys.partitions p
    ON t.object_id = p.object_id
WHERE
    p.index_id IN (0, 1)
    AND t.name IN (
        'DimAge',
        'DimContent',
        'DimDate',
        'DimGender',
        'DimPlatform',
        'DimRegion',
        'FactMarketingPerformance'
    )
GROUP BY
    t.name
ORDER BY
    t.name;
GO

-- Check primary keys in the marketing analytics database
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    CONSTRAINT_NAME LIKE 'PK%'
ORDER BY
    TABLE_NAME;
GO

-- Check foreign-key relationships in the database
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    CONSTRAINT_NAME LIKE 'FK%'
ORDER BY
    TABLE_NAME,
    COLUMN_NAME;
GO


