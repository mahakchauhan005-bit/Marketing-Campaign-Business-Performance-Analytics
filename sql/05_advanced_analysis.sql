-- ============================================================
-- ADVANCED ANALYTICS
-- Marketing Campaign Business Performance Analytics
-- Database: MarketingCampaignAnalytics
-- ============================================================

USE MarketingCampaignAnalytics;
GO

-- ============================================================
-- 1. MONTH-OVER-MONTH REVENUE GROWTH
-- ============================================================

WITH MonthlyRevenue AS
(
    SELECT
        YEAR(d.Date) AS Year_Number,
        MONTH(d.Date) AS Month_Number,
        SUM(f.Revenue) AS Monthly_Revenue
    FROM FactMarketingPerformance f
    INNER JOIN DimDate d
        ON f.Date_ID = d.Date_ID
    GROUP BY
        YEAR(d.Date),
        MONTH(d.Date)
)

SELECT
    Year_Number,
    Month_Number,
    Monthly_Revenue,

    LAG(Monthly_Revenue) OVER
    (
        ORDER BY Year_Number, Month_Number
    ) AS Previous_Month_Revenue,

    Monthly_Revenue
        - LAG(Monthly_Revenue) OVER
        (
            ORDER BY Year_Number, Month_Number
        ) AS Revenue_Change,

    CAST
    (
        (
            Monthly_Revenue
            - LAG(Monthly_Revenue) OVER
            (
                ORDER BY Year_Number, Month_Number
            )
        )
        * 100.0
        / NULLIF
        (
            LAG(Monthly_Revenue) OVER
            (
                ORDER BY Year_Number, Month_Number
            ),
            0
        )
        AS DECIMAL(10,2)
    ) AS Revenue_Growth_Percentage

FROM MonthlyRevenue
ORDER BY
    Year_Number,
    Month_Number;
GO


-- ============================================================
-- 2. RUNNING CUMULATIVE REVENUE
-- ============================================================

WITH MonthlyRevenue AS
(
    SELECT
        YEAR(d.Date) AS Year_Number,
        MONTH(d.Date) AS Month_Number,
        SUM(f.Revenue) AS Monthly_Revenue
    FROM FactMarketingPerformance f
    INNER JOIN DimDate d
        ON f.Date_ID = d.Date_ID
    GROUP BY
        YEAR(d.Date),
        MONTH(d.Date)
)

SELECT
    Year_Number,
    Month_Number,
    Monthly_Revenue,

    SUM(Monthly_Revenue) OVER
    (
        ORDER BY Year_Number, Month_Number
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS Cumulative_Revenue

FROM MonthlyRevenue
ORDER BY
    Year_Number,
    Month_Number;
GO


-- ============================================================
-- 3. PLATFORM REVENUE CONTRIBUTION
-- ============================================================

SELECT
    p.Platform,
    SUM(f.Revenue) AS Platform_Revenue,

    CAST
    (
        SUM(f.Revenue) * 100.0
        / SUM(SUM(f.Revenue)) OVER ()
        AS DECIMAL(10,2)
    ) AS Revenue_Contribution_Percentage

FROM FactMarketingPerformance f
INNER JOIN DimPlatform p
    ON f.Platform_ID = p.Platform_ID

GROUP BY
    p.Platform

ORDER BY
    Platform_Revenue DESC;
GO


-- ============================================================
-- 4. PLATFORM PERFORMANCE RANKING
-- ============================================================

SELECT
    p.Platform,

    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Spend) AS Total_Spend,

    SUM(f.Revenue) / NULLIF(SUM(f.Spend), 0) AS ROAS,

    RANK() OVER
    (
        ORDER BY
            SUM(f.Revenue) / NULLIF(SUM(f.Spend), 0) DESC
    ) AS ROAS_Rank

FROM FactMarketingPerformance f
INNER JOIN DimPlatform p
    ON f.Platform_ID = p.Platform_ID

GROUP BY
    p.Platform

ORDER BY
    ROAS_Rank;
GO


-- ============================================================
-- 5. CAMPAIGN PERFORMANCE RANKING
-- ============================================================

WITH CampaignPerformance AS
(
    SELECT
        Campaign_ID,
        SUM(Spend) AS Total_Spend,
        SUM(Revenue) AS Total_Revenue,
        SUM(Conversions) AS Total_Conversions,

        SUM(Revenue) / NULLIF(SUM(Spend), 0) AS ROAS

    FROM FactMarketingPerformance

    GROUP BY
        Campaign_ID
),

RankedCampaigns AS
(
    SELECT
        *,
        DENSE_RANK() OVER
        (
            ORDER BY ROAS DESC
        ) AS ROAS_Rank

    FROM CampaignPerformance
)

SELECT
    Campaign_ID,
    Total_Spend,
    Total_Revenue,
    Total_Conversions,
    ROAS,
    ROAS_Rank

FROM RankedCampaigns

WHERE ROAS_Rank <= 10

ORDER BY
    ROAS_Rank,
    ROAS DESC;
GO


-- ============================================================
-- 6. ADVANCED CAMPAIGN EFFICIENCY CLASSIFICATION
-- ============================================================

WITH CampaignPerformance AS
(
    SELECT
        Campaign_ID,
        SUM(Budget) AS Total_Budget,
        SUM(Spend) AS Total_Spend,
        SUM(Revenue) AS Total_Revenue,
        SUM(Conversions) AS Total_Conversions,

        SUM(Revenue) / NULLIF(SUM(Spend), 0) AS ROAS

    FROM FactMarketingPerformance

    GROUP BY
        Campaign_ID
)

SELECT
    Campaign_ID,
    Total_Budget,
    Total_Spend,
    Total_Revenue,
    Total_Conversions,
    ROAS,

    CASE
        WHEN ROAS >= 12 THEN 'High Performer'
        WHEN ROAS >= 8 THEN 'Average Performer'
        ELSE 'Low Performer'
    END AS Performance_Category,

    CASE
        WHEN Total_Spend > Total_Budget THEN 'Overspent'
        ELSE 'Within Budget'
    END AS Budget_Status

FROM CampaignPerformance

ORDER BY
    ROAS DESC;
GO


-- ============================================================
-- 7. REVENUE TO SPEND EFFICIENCY
-- ============================================================

SELECT
    Campaign_ID,
    SUM(Spend) AS Total_Spend,
    SUM(Revenue) AS Total_Revenue,

    SUM(Revenue) - SUM(Spend) AS Net_Return,

    SUM(Revenue) / NULLIF(SUM(Spend), 0) AS ROAS,

    CAST
    (
        (SUM(Revenue) - SUM(Spend))
        * 100.0
        / NULLIF(SUM(Spend), 0)
        AS DECIMAL(10,2)
    ) AS Return_Percentage

FROM FactMarketingPerformance

GROUP BY
    Campaign_ID

ORDER BY
    Return_Percentage DESC;
GO


-- ============================================================
-- 8. PLATFORM + REGION PERFORMANCE RANKING
-- ============================================================

WITH PlatformRegion AS
(
    SELECT
        p.Platform,
        r.Region,

        SUM(f.Spend) AS Total_Spend,
        SUM(f.Revenue) AS Total_Revenue,
        SUM(f.Conversions) AS Total_Conversions,

        SUM(f.Revenue) / NULLIF(SUM(f.Spend), 0) AS ROAS

    FROM FactMarketingPerformance f

    INNER JOIN DimPlatform p
        ON f.Platform_ID = p.Platform_ID

    INNER JOIN DimRegion r
        ON f.Region_ID = r.Region_ID

    GROUP BY
        p.Platform,
        r.Region
)

SELECT
    Platform,
    Region,
    Total_Spend,
    Total_Revenue,
    Total_Conversions,
    ROAS,

    RANK() OVER
    (
        PARTITION BY Platform
        ORDER BY ROAS DESC
    ) AS Region_Rank_Within_Platform

FROM PlatformRegion

ORDER BY
    Platform,
    Region_Rank_Within_Platform;
GO


-- ============================================================
-- 9. FINAL ADVANCED EXECUTIVE SUMMARY
-- ============================================================

SELECT
    COUNT(DISTINCT Campaign_ID) AS Total_Campaigns,

    SUM(Spend) AS Total_Spend,

    SUM(Revenue) AS Total_Revenue,

    SUM(Revenue) - SUM(Spend) AS Net_Return,

    SUM(Conversions) AS Total_Conversions,

    CAST
    (
        SUM(Clicks) * 100.0
        / NULLIF(SUM(Impressions), 0)
        AS DECIMAL(10,2)
    ) AS Overall_CTR_Percentage,

    CAST
    (
        SUM(Conversions) * 100.0
        / NULLIF(SUM(Clicks), 0)
        AS DECIMAL(10,2)
    ) AS Overall_Conversion_Rate_Percentage,

    SUM(Spend)
        / NULLIF(SUM(Conversions), 0) AS Overall_CPA,

    SUM(Revenue)
        / NULLIF(SUM(Spend), 0) AS Overall_ROAS

FROM FactMarketingPerformance;
GO


-- ============================================================
-- 10. ADVANCED DATA QUALITY SUMMARY
-- ============================================================

SELECT
    COUNT(*) AS Total_Records,

    SUM
    (
        CASE
            WHEN Spend < 0
              OR Revenue < 0
              OR Budget < 0
              OR Clicks < 0
              OR Impressions < 0
              OR Conversions < 0
            THEN 1
            ELSE 0
        END
    ) AS Negative_Value_Records,

    SUM
    (
        CASE
            WHEN CTR < 0 OR CTR > 1
            THEN 1
            ELSE 0
        END
    ) AS Invalid_CTR_Records,

    SUM
    (
        CASE
            WHEN Campaign_ID IS NULL
            THEN 1
            ELSE 0
        END
    ) AS Missing_Campaign_IDs

FROM FactMarketingPerformance;
GO


