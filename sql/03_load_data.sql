-- Select the project database
USE MarketingCampaignAnalytics;
GO


-- Check DimAge
SELECT TOP 10 *
FROM DimAge;
GO


-- Check DimContent
SELECT TOP 10 *
FROM DimContent;
GO


-- Check DimDate
SELECT TOP 10 *
FROM DimDate;
GO


-- Check DimGender
SELECT TOP 10 *
FROM DimGender;
GO


-- Check DimPlatform
SELECT TOP 10 *
FROM DimPlatform;
GO


-- Check DimRegion
SELECT TOP 10 *
FROM DimRegion;
GO


-- Check FactMarketingPerformance
SELECT TOP 10 *
FROM FactMarketingPerformance;
GO


-- Count rows in all dimension and fact tables
SELECT 'DimAge' AS Table_Name, COUNT(*) AS Row_Count
FROM DimAge

UNION ALL

SELECT 'DimContent', COUNT(*)
FROM DimContent

UNION ALL

SELECT 'DimDate', COUNT(*)
FROM DimDate

UNION ALL

SELECT 'DimGender', COUNT(*)
FROM DimGender

UNION ALL

SELECT 'DimPlatform', COUNT(*)
FROM DimPlatform

UNION ALL

SELECT 'DimRegion', COUNT(*)
FROM DimRegion

UNION ALL

SELECT 'FactMarketingPerformance', COUNT(*)
FROM FactMarketingPerformance;
GO

-- Verify that all project tables exist in the database
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
  AND TABLE_NAME IN (
      'DimAge',
      'DimContent',
      'DimDate',
      'DimGender',
      'DimPlatform',
      'DimRegion',
      'FactMarketingPerformance'
  )
ORDER BY TABLE_NAME;
GO


-- Check whether any Campaign_ID appears more than once in the fact table
SELECT Campaign_ID, COUNT(*) AS Duplicate_Count
FROM FactMarketingPerformance
GROUP BY Campaign_ID
HAVING COUNT(*) > 1
ORDER BY Duplicate_Count DESC;


-- Check that every foreign key in the fact table matches a dimension table

SELECT COUNT(*) AS Invalid_Age_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimAge d ON f.Age_ID = d.Age_ID
WHERE d.Age_ID IS NULL;

SELECT COUNT(*) AS Invalid_Content_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimContent d ON f.Content_ID = d.Content_ID
WHERE d.Content_ID IS NULL;

SELECT COUNT(*) AS Invalid_Gender_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimGender d ON f.Gender_ID = d.Gender_ID
WHERE d.Gender_ID IS NULL;

SELECT COUNT(*) AS Invalid_Platform_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimPlatform d ON f.Platform_ID = d.Platform_ID
WHERE d.Platform_ID IS NULL;

SELECT COUNT(*) AS Invalid_Region_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimRegion d ON f.Region_ID = d.Region_ID
WHERE d.Region_ID IS NULL;

SELECT COUNT(*) AS Invalid_Date_IDs
FROM FactMarketingPerformance f
LEFT JOIN DimDate d ON f.Date_ID = d.Date_ID
WHERE d.Date_ID IS NULL;