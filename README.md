Excited to share my latest Data Engineering project! 🚀
I built an end-to-end Azure Data Engineering pipeline for AdventureWorks Cycles — ingesting raw sales data, transforming it through a Medallion Architecture, and delivering interactive analytics via Power BI.
Here's what the pipeline does:
📥  Bronze Layer — ADF dynamically copies 10 CSVs from GitHub using a metadata-driven Lookup + ForEach pattern, zero hardcoding
⚙️  Silver Layer — Databricks PySpark cleans and enriches data: derived columns (FullName, Month, Year), type casting, SKU normalization, and order number standardization
🥇  Gold Layer — Synapse Analytics serverless SQL exposes Parquet files as views and materializes an external table (gold.extsales) for Power BI
📊  Power BI — Line chart revealing monthly order patterns: February dip, March spike, peak summer volume, and year-end decline
Tech stack used:
Azure Data Factory  •  Azure Data Lake Gen2  •  Azure Databricks (PySpark)  •  Azure Synapse Analytics  •  Power BI  •  GitHub
Key concepts practiced:
Medallion Architecture  •  Parameterized pipelines  •  OPENROWSET  •  External tables  •  Managed Identity  •  Database Scoped Credentials  •  Snappy Parquet compression
If you're learning Azure data engineering, the Medallion pattern is a great place to start — it keeps raw data intact, makes transformations testable at each layer, and keeps your BI layer clean.
#Azure #DataEngineering #AzureDataFactory #Databricks #PySpark #Synapse #PowerBI #MedallionArchitecture #DataLake #OpenToWork #Portfolio
