# AdventureWorks Azure Data Pipeline

> End-to-end Azure data engineering pipeline · Medallion Architecture · Power BI analytics

![Azure](https://img.shields.io/badge/Azure-Data%20Factory-0078D4?style=flat-square&logo=microsoftazure)
![Databricks](https://img.shields.io/badge/Databricks-PySpark-FF3621?style=flat-square&logo=databricks)
![Synapse](https://img.shields.io/badge/Synapse-Analytics-0078D4?style=flat-square&logo=microsoftazure)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi)

---

## Overview

This project implements a production-grade, end-to-end data engineering pipeline for **AdventureWorks Cycles** on Azure. Raw sales data is ingested from GitHub, transformed through a three-layer Medallion Architecture, and delivered as interactive Power BI analytics — revealing monthly order patterns across the full sales cycle.

---

## Architecture

```
GitHub CSVs
    │
    ▼
┌─────────────────────────────────────────┐
│  🥉 BRONZE LAYER — Azure Data Factory   │
│  Metadata-driven ingestion              │
│  Lookup + ForEach · 10 CSVs · No        │
│  hardcoding · Raw files → ADLS Gen2     │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  🥈 SILVER LAYER — Azure Databricks     │
│  PySpark transformation & enrichment    │
│  Derived columns · Type casting         │
│  SKU normalization · Snappy Parquet     │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  🥇 GOLD LAYER — Synapse Analytics      │
│  Serverless SQL · OPENROWSET views      │
│  External table: gold.extsales          │
│  Managed Identity · Scoped Credentials  │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  📊 ANALYTICS — Power BI                │
│  Direct connection to gold.extsales     │
│  Monthly order trend line charts        │
└─────────────────────────────────────────┘
```

---

## Layer Details

### 🥉 Bronze Layer — Raw Ingestion

**Tool:** Azure Data Factory

Dynamically ingests 10 CSV files from GitHub using a metadata-driven **Lookup → ForEach** pattern. Zero hardcoded paths — fully parameterized pipeline writes raw files straight to Azure Data Lake Gen2.

**Key techniques:**
- `Lookup` activity reads file metadata list
- `ForEach` loop iterates and copies each file dynamically
- HTTP connector pulls CSVs from GitHub
- Parameterized pipeline (no hardcoding)
- Raw zone in ADLS Gen2 preserves source fidelity

---

### 🥈 Silver Layer — Transformation & Enrichment

**Tool:** Azure Databricks (PySpark)

PySpark notebooks clean and enrich the raw Bronze data, adding derived columns and standardizing formats before writing Snappy-compressed Parquet to the Silver zone.

**Transformations applied:**
- Derived columns: `FullName`, `Month`, `Year`
- Type casting for date and numeric fields
- SKU normalization across product records
- Order number standardization
- Output: Snappy-compressed Parquet

---

### 🥇 Gold Layer — Serving

**Tool:** Azure Synapse Analytics (Serverless SQL)

Synapse serverless SQL exposes Silver Parquet files as views via `OPENROWSET`, then materializes `gold.extsales` as an external table for efficient, secure BI access.

**Key techniques:**
- `OPENROWSET` to query Parquet directly
- External table: `gold.extsales`
- Database Scoped Credentials for secure access
- Managed Identity authentication
- Views as lightweight abstraction layer

---

### 📊 Analytics Layer — Power BI

Power BI connects directly to `gold.extsales`, surfacing monthly order volume patterns through line charts.

**Insights discovered:**

| Period | Pattern |
|---|---|
| February | Notable dip — post-holiday demand contraction |
| March | Sharp recovery spike — Q1 purchasing resurgence |
| Summer (Jun–Aug) | Peak volume — seasonal cycling demand at maximum |
| Year-end | Gradual decline — inventory wind-down pattern |

---

## Tech Stack

| Tool | Role |
|---|---|
| Azure Data Factory | Pipeline orchestration & ingestion |
| Azure Data Lake Gen2 | Hierarchical storage for all three zones |
| Azure Databricks (PySpark) | Data transformation & enrichment |
| Azure Synapse Analytics | Serverless SQL serving layer |
| Power BI | Interactive dashboards & analytics |
| GitHub | Source CSV data via HTTP |

---

## Key Concepts Practiced

- Medallion Architecture (Bronze / Silver / Gold)
- Metadata-driven parameterized pipelines
- `OPENROWSET` for serverless Parquet querying
- External tables in Synapse
- Managed Identity & Database Scoped Credentials
- Snappy Parquet compression
- PySpark column derivation and type casting
- SKU & order number normalization
- Serverless SQL pool design

---

## Why Medallion Architecture?

The Medallion pattern keeps **raw data intact** in the Bronze layer — every transformation is testable and auditable independently. Silver handles all enrichment logic in isolation, so failures never corrupt source data. The Gold layer stays intentionally thin: just the views and external tables BI tools need, keeping query performance high and the serving surface clean.

Each layer can be reprocessed independently, making debugging and backfilling straightforward. For teams learning Azure data engineering, this pattern scales reliably from prototype to production without major restructuring.

---

## Tags

`#Azure` `#DataEngineering` `#AzureDataFactory` `#Databricks` `#PySpark` `#Synapse` `#PowerBI` `#MedallionArchitecture` `#DataLake` `#OpenToWork` `#Portfolio`
