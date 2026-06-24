Databricks Medallion Architecture Pipeline 🚀

An end-to-end cloud ETL pipeline built on Databricks Serverless Compute using Apache Spark (PySpark) and Delta Lake, demonstrating the industry-standard Bronze-Silver-Gold (Medallion) data architecture.

This project simulates a production-grade data engineering workflow, leveraging Databricks Unity Catalog Volumes for secure data storage and processing a simulated e-commerce dataset for business intelligence.

🛠️ Tech Stack & Infrastructure

Cloud Platform: Databricks (Serverless Compute)

Data Processing: PySpark

Storage Format: Delta Lake

Data Catalog: Databricks Unity Catalog (Volumes)

Language: Python

🏗️ Architecture Flow

Mock Data Generation: Generated 10,000+ rows of realistic sales data locally, injecting intentional duplicates and NULL values to mimic dirty, real-world data, which was then uploaded to a Databricks Volume.

Bronze Layer (01_bronze_ingestion): Ingests the raw CSV data directly from the Unity Catalog Volume into a Delta table, appending an ingestion_timestamp for metadata tracking and data lineage.

Silver Layer (02_silver_transformation): Data cleansing and standardization. Drops duplicate records, handles NULL values, and enforces schema types (casting strings to date objects). The data is partitioned by product_category for optimized downstream querying.

Gold Layer (03_gold_aggregation): Business-level aggregations. Calculates total order counts and revenue by product category, returning a query-optimized analytics table ready for BI tools.

💡 Key Features Highlighted

Cloud-Native Storage: Transitioned from local file systems to secure cloud storage using Databricks /Volumes/.

Delta Lake Capabilities: Utilized Delta formatting for ACID transactions and scalable metadata handling.

Serverless Optimization: Executed on Databricks Serverless compute, eliminating the need for manual memory management by relying on advanced background caching and auto-scaling.
