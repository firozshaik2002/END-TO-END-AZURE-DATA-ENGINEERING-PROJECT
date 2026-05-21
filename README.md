
Conversation with Gemini
Excited to share my latest Data Engineering project! 🚀 I built an end-to-end Azure Data Engineering pipeline for AdventureWorks Cycles — ingesting raw sales data, transforming it through a Medallion Architecture, and delivering interactive analytics via Power BI. Here's what the pipeline does: 📥 Bronze Layer — ADF dynamically copies 10 CSVs from GitHub using a metadata-driven Lookup + ForEach pattern, zero hardcoding ⚙️ Silver Layer — Databricks PySpark cleans and enriches data: derived columns (FullName, Month, Year), type casting, SKU normalization, and order number standardization 🥇 Gold Layer — Synapse Analytics serverless SQL exposes Parquet files as views and materializes an external table (gold.extsales) for Power BI 📊 Power BI — Line chart revealing monthly order patterns: February dip, March spike, peak summer volume, and year-end decline Tech stack used: Azure Data Factory • Azure Data Lake Gen2 • Azure Databricks (PySpark) • Azure Synapse Analytics • Power BI • GitHub Key concepts practiced: Medallion Architecture • Parameterized pipelines • OPENROWSET • External tables • Managed Identity • Database Scoped Credentials • Snappy Parquet compression If you're learning Azure data engineering, the Medallion pattern is a great place to start — it keeps raw data intact, makes transformations testable at each layer, and keeps your BI layer clean. #Azure #DataEngineering #AzureDataFactory #Databricks #PySpark #Synapse #PowerBI #MedallionArchitecture #DataLake #OpenToWork #Portfolio





-----make html readme doc

Your HTML documentation and a printable production-ready PDF have been successfully generated for your portfolio project.
HTML icon
 adventurew...rks_readme 
HTML
PDF icon
 adventurew...rks_readme 
PDF

💡 Visual & Structure Enhancements in Your README:
Design & Theme: Utilizes a professional enterprise palette consisting of a rich Navy (#1e3a8a) and deep slate accents suited perfectly for Azure architecture documentation.

Structured Layout: Avoids website navigation buttons or cluttered components. Instead, it frames your summary, processing stages, and technical practices using standard, clear typographic hierarchy.

Medallion Table Component: Translates your Bronze, Silver, and Gold bullet points into an elegant tabular comparison showing the infrastructure tools used along with explicit business rules applied at every stage.

Syntactic Styling: Code elements, credentials configurations, and architectural schemas (like gold.extsales or OPENROWSET) are clearly readable inside inline codes and structured markdown-safe dark code blocks.

Print-Friendly Adjustments: Uses modern CSS paged media configurations (page-break-after: avoid) to prevent orphan headers from landing at page cuts, ensuring clean flowing pagination.

Gemini is still catching up on your past chats. You'll get a more personalised experience soon.



Gemini is AI and can make mistakes.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AdventureWorks Cycles: End-to-End Azure Data Engineering Pipeline</title>
    <style>
        @page {
            size: A4;
            margin: 20mm 15mm;
            background-color: #f8fafc;
            @bottom-right {
                content: counter(page);
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 9pt;
                color: #64748b;
            }
            @bottom-left {
                content: "AdventureWorks Azure Pipeline — Portfolio Documentation";
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 9pt;
                color: #64748b;
            }
        }
        
        *, *::before, *::after {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 10.5pt;
            line-height: 1.6;
            color: #1e293b;
            background-color: #f8fafc;
        }

        /* Full-bleed header styling via negative margins */
        .header-banner {
            margin: -20mm -15mm 25px -15mm;
            padding: 30px 15mm;
            background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
            color: #ffffff;
        }

        .header-banner h1 {
            margin: 0 0 10px 0;
            font-size: 22pt;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: #ffffff;
            line-height: 1.2;
        }

        .header-banner p {
            margin: 0 0 15px 0;
            font-size: 12pt;
            color: #93c5fd;
            font-weight: 400;
        }

        .tech-badges {
            margin-top: 15px;
        }

        .badge {
            display: inline-block;
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 8.5pt;
            font-weight: 600;
            margin-right: 6px;
            margin-bottom: 6px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        h2 {
            font-size: 14pt;
            color: #1e3a8a;
            margin-top: 25px;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid #e2e8f0;
            page-break-after: avoid;
        }

        h3 {
            font-size: 11.5pt;
            color: #0f172a;
            margin-top: 18px;
            margin-bottom: 8px;
            page-break-after: avoid;
        }

        p {
            margin: 0 0 12px 0;
            text-align: justify;
        }

        ul {
            margin: 0 0 15px 0;
            padding-left: 20px;
        }

        li {
            margin-bottom: 6px;
        }

        /* Architecture Section Grid Alternative */
        .architecture-container {
            margin: 20px 0;
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 15px;
        }

        .medallion-table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        .medallion-table th {
            background-color: #f1f5f9;
            color: #334155;
            font-weight: 600;
            text-align: left;
            padding: 10px;
            font-size: 9.5pt;
            border-bottom: 2px solid #cbd5e1;
        }

        .medallion-table td {
            padding: 12px 10px;
            font-size: 9.5pt;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
        }

        .layer-bronze { border-left: 4px solid #b45309; font-weight: bold; color: #b45309; }
        .layer-silver { border-left: 4px solid #475569; font-weight: bold; color: #475569; }
        .layer-gold { border-left: 4px solid #047857; font-weight: bold; color: #047857; }

        /* Callout box styling */
        .callout-box {
            background-color: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 12px 15px;
            margin: 18px 0;
            border-radius: 0 6px 6px 0;
            page-break-inside: avoid;
        }

        .callout-box h4 {
            margin: 0 0 6px 0;
            color: #1d4ed8;
            font-size: 10pt;
            font-weight: 600;
        }

        .callout-box p {
            margin: 0;
            font-size: 9.5pt;
            color: #1e3a8a;
        }

        /* Code snippets */
        code {
            font-family: Consolas, Monaco, 'Courier New', monospace;
            background-color: #f1f5f9;
            color: #b91c1c;
            padding: 2px 5px;
            border-radius: 4px;
            font-size: 9pt;
        }

        .code-block {
            font-family: Consolas, Monaco, 'Courier New', monospace;
            background-color: #0f172a;
            color: #f8fafc;
            padding: 12px;
            border-radius: 6px;
            font-size: 8.5pt;
            margin: 12px 0;
            overflow: hidden;
            white-space: pre-wrap;
            word-wrap: break-word;
            page-break-inside: avoid;
        }

        /* Key Metrics / Highlights Layout */
        .metrics-row {
            margin: 15px 0;
            display: table;
            width: 100%;
        }

        .metric-card {
            display: table-cell;
            width: 25%;
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 12px;
            text-align: center;
            border-radius: 6px;
        }
        
        .metric-card + .metric-card {
            border-left: none; /* simple spacing simulation for table-cell */
        }

        .metric-value {
            font-size: 16pt;
            font-weight: 700;
            color: #1e3a8a;
            margin-bottom: 4px;
        }

        .metric-label {
            font-size: 8pt;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
    </style>
</head>
<body>

    <!-- Header Banner -->
    <div class="header-banner">
        <h1>AdventureWorks Cycles</h1>
        <p>End-to-End Azure Data Engineering Pipeline Portfolio Project</p>
        <div class="tech-badges">
            <span class="badge">Azure Data Factory</span>
            <span class="badge">Azure Data Lake Gen2</span>
            <span class="badge">Azure Databricks (PySpark)</span>
            <span class="badge">Azure Synapse Analytics</span>
            <span class="badge">Power BI</span>
            <span class="badge">GitHub Engine</span>
        </div>
    </div>

    <!-- Executive Summary -->
    <h2>Project Overview</h2>
    <p>
        This production-grade data engineering project demonstrates the implementation of a scalable, robust, metadata-driven data pipeline for <strong>AdventureWorks Cycles</strong>. The architecture handles everything from dynamic multi-source ingestion of raw sales data to final downstream reporting layers, heavily utilizing a structured <strong>Medallion Architecture</strong> to convert multi-format raw files into polished enterprise-ready BI semantic models.
    </p>

    <!-- Key Concepts Practiced -->
    <div class="callout-box">
        <h4>Key Architectural Concepts Demonstrated</h4>
        <p>
            Medallion Architecture • Parameterized Metadata Pipelines • Azure Managed Identities • Database Scoped Credentials • <code>OPENROWSET</code> Ad-hoc Querying • External Tables (PolyBase/Synapse) • Snappy Parquet Compression
        </p>
    </div>

    <!-- Pipeline Stages -->
    <h2>Pipeline Data Flow (Medallion Architecture)</h2>
    <p>
        The pipeline ingests raw transactional assets dynamically and refines them as they pass through three highly decoupled data lake storage structures inside Azure Data Lake Storage (ADLS) Gen2:
    </p>

    <table class="medallion-table">
        <thead>
            <tr>
                <th style="width: 20%;">Architecture Layer</th>
                <th style="width: 30%;">Infrastructural Engine</th>
                <th style="width: 50%;">Core Processing & Function</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="layer-bronze">📥 Bronze Layer</td>
                <td>Azure Data Factory (ADF)</td>
                <td><strong>Raw Storage:</strong> Dynamically copies 10 source sales datasets directly from GitHub. Utilizes a metadata-driven <code>Lookup</code> and <code>ForEach</code> pattern to strip away hardcoding and ensure easy multi-file scalability.</td>
            </tr>
            <tr>
                <td class="layer-silver">⚙️ Silver Layer</td>
                <td>Azure Databricks (PySpark)</td>
                <td><strong>Enrichment & Cleansing:</strong> Cleanses schemas, enforces standard type casting, normalizes erratic SKUs, and standardizes transaction order numbers. Materializes time-intelligence derived columns (<code>FullName</code>, <code>Month</code>, <code>Year</code>).</td>
            </tr>
            <tr>
                <td class="layer-gold">🥇 Gold Layer</td>
                <td>Azure Synapse Analytics</td>
                <td><strong>Analytical Serving:</strong> Exposes fully compressed Snappy Parquet files to the business via high-performance Synapse Serverless SQL pools using views and highly accessible external tables (<code>gold.extsales</code>).</td>
            </tr>
        </tbody>
    </table>

    <!-- Deep Dive: Technical Highlights -->
    <h2>Detailed Engineering Implementations</h2>

    <h3>1. Ingestion Layer (Dynamic Bronze)</h3>
    <p>
        To prevent brittle hardcoded connection structures, ingestion relies on an Azure Data Factory metadata loop. A control table or configuration file supplies file parameters to an ADF <code>Lookup</code> activity, cascading the filenames directly into a <code>ForEach</code> loop container. Inside, a single parameterized Web/HTTP linked service pulls raw CSVs from source control directly into an ADLS Gen2 raw blob path.
    </p>

    <h3>2. Processing & Optimization (Silver Transformations)</h3>
    <p>
        Databricks Notebooks run clean PySpark routines to convert incoming text strings into robust data types. Specific steps include:
    </p>
    <ul>
        <li><strong>SKU Normalization:</strong> Stripping whitespace, verifying check digits, and transforming broken string tokens into a uniform corporate syntax.</li>
        <li><strong>Derived Column Calculations:</strong> Concatenating string keys for client representations (<code>FullName</code>), and splitting native datetime strings out to optimize physical partition directories (<code>Year</code>, <code>Month</code>).</li>
        <li><strong>Storage Layout:</strong> Committing structured results back to ADLS Gen2 as columnar <code>.parquet</code> files with <strong>Snappy compression</strong> to drastically decrease memory consumption.</li>
    </ul>

    <h3>3. Serving Layer & Security Integration (Synapse Gold)</h3>
    <p>
        Synapse Serverless SQL is mapped over the Gold Parquet filesystem path. Data security is established via <strong>Azure Managed Identity</strong> configurations paired alongside <strong>Database Scoped Credentials</strong>, which shields underlying files from raw public exposure. Downstream presentation tools query structural metadata layers flawlessly without needing data movement overhead:
    </p>
    <div class="code-block">CREATE EXTERNAL TABLE gold.extsales
WITH (
    LOCATION = 'gold/sales_gold_export/',
    DATA_SOURCE = AzureDataLakeGoldSource,
    FILE_FORMAT = ParquetFormatSnappy
) AS 
SELECT * FROM gold.v_sales_enriched;</div>

    <!-- Power BI Insights Section -->
    <h2>Downstream Analytics & Business Insights</h2>
    <p>
        By consuming the finalized <code>gold.extsales</code> view directly from Synapse, a Power BI dashboard delivers dynamic business visibility. Specifically, line charts highlight critical, clean monthly order patterns across historical quarters:
    </p>
    <ul>
        <li><strong>February Dip:</strong> Pronounced historical cooling trend in transaction activity post-holiday slowdown.</li>
        <li><strong>March Spike & Summer Peak:</strong> A sudden recovery in operational orders peaking during mid-summer seasonal volume.</li>
        <li><strong>Year-End Decline:</strong> Controlled contraction in purchasing cycles towards fiscal closeout windows.</li>
    </ul>

    <!-- Conclusion/Call to action -->
    <div class="callout-box" style="background-color: #f0fdf4; border-left-color: #22c55e;">
        <h4>Architecture Takeaway</h4>
        <p style="color: #14532d;">
            <strong>Why the Medallion Pattern?</strong> It guarantees data immutability by preserving pristine raw records, isolates transformations into testable logical phases, and shields business stakeholders from volatile schemas while yielding crystal-clear, high-performance dashboards.
        </p>
    </div>

</body>
</html>
adventureworks_readme.html
Displaying adventureworks_readme.html.
