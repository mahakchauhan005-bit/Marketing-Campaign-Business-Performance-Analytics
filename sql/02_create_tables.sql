USE MarketingCampaignAnalytics;
GO

-- Create the Age dimension table
CREATE TABLE DimAge(
   Age_ID INT  PRIMARY KEY,
   Target_Age VARCHAR(50)
);

-- Create the content type dimension table
CREATE TABLE DimContent(
    Content_ID INT PRIMARY KEY,
    Content_Type VARCHAR(50)
);

-- Create the target gender dimension table
CREATE TABLE DimGender(
    Gender_ID INT PRIMARY KEY,
    Target_Gender VARCHAR(50)
);

-- Create the platform dimension table
CREATE TABLE DimPlatform(
    Platform_ID INT PRIMARY KEY,
    Platform VARCHAR(50)
);

-- Create the region dimension table
CREATE TABLE DimRegion(
    Region_ID INT PRIMARY KEY,
    Region VARCHAR(50)
);

-- Create the date dimension table
CREATE TABLE DimDate(
    Date_ID INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Month_Number INT,
    Month_Name VARCHAR(20),
    Quarter VARCHAR(5)
);

-- Create the main marketing performance fact table
CREATE TABLE FactMarketingPerformance(
    Campaign_ID VARCHAR(20) PRIMARY KEY,

    Age_ID INT,
    Content_ID INT,
    Gender_ID INT,
    Platform_ID INT,
    Region_ID INT,
    Date_ID INT,

    Budget DECIMAL(12,2),
    Clicks INT,
    CTR DECIMAL(10,4),
    CPC DECIMAL(10,2),
    Conversions INT,
    CPA DECIMAL(10,2),
    Conversion_Rate DECIMAL(10,4),
    Duration INT,
    Revenue DECIMAL(14,2),
    Spend DECIMAL(14,2),
    ROAS DECIMAL(10,2),
    Impressions INT
);


-- Connect the fact table to the dimension tables
ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Age
FOREIGN KEY (Age_ID) REFERENCES DimAge(Age_ID);

ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Content
FOREIGN KEY (Content_ID) REFERENCES DimContent(Content_ID);

ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Gender
FOREIGN KEY (Gender_ID) REFERENCES DimGender(Gender_ID);

ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Platform
FOREIGN KEY (Platform_ID) REFERENCES DimPlatform(Platform_ID);

ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Region
FOREIGN KEY (Region_ID) REFERENCES DimRegion(Region_ID);

ALTER TABLE FactMarketingPerformance
ADD CONSTRAINT FK_Fact_Date
FOREIGN KEY (Date_ID) REFERENCES DimDate(Date_ID);

-- Check that all required tables were created
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME;

