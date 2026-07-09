
# Real-Time Streaming Data Pipeline 🚀

\# Real-Time Sales Analytics Pipeline 🚀
>>>>>>> 4b3dd6a (Add detailed README with architecture image)

## 📌 Project Overview

This project is a **Real-Time Data Streaming Pipeline** built to process live data using **Python, Apache Spark / PySpark, and Medallion Architecture**.

The main goal of this project is to simulate real-time incoming data, process it step by step, clean the data, transform it, and prepare it for analytics and reporting.

\## 📌 Project Overview

This project follows the modern **Bronze → Silver → Gold** architecture used in real-world Data Engineering projects.

## 🏗️ Architecture

This project is a \*\*Real-Time Sales Analytics Pipeline\*\* built using \*\*Apache Kafka, Apache Spark Structured Streaming, Docker, PySpark, Hadoop, CSV Data Lake, and Power BI\*\*.



The pipeline ingests real-time sales order data into Kafka topics, processes the streaming data using PySpark Structured Streaming, stores data using \*\*Medallion Architecture\*\* in \*\*Bronze, Silver, and Gold layers\*\*, and visualizes business KPIs in Power BI.



\---



\## 🏗️ Architecture

![Project Architecture](images/Architecture1.png)

```text

Order Data Producer

&#x20;       ↓

Apache Kafka Topic

&#x20;       ↓

Apache Spark Structured Streaming

&#x20;       ↓

Bronze Layer - Raw Data

&#x20;       ↓

Silver Layer - Cleaned Data

&#x20;       ↓

Gold Layer - Aggregated Data

&#x20;       ↓

Power BI Dashboard

```



\---



\## 🛠️ Technologies Used



\- Python

\- Apache Kafka

\- Apache Spark Structured Streaming

\- PySpark

\- Docker

\- Docker Compose

\- Hadoop

\- CSV Data Lake

\- Power BI

\- Git \& GitHub



\---



\## 🥉 Bronze Layer



The \*\*Bronze Layer\*\* stores raw streaming sales order data received from Kafka.



\### Purpose



\- Store raw order events

\- Keep original data for backup

\- Support future reprocessing

\- Maintain source-level data



\---



\## 🥈 Silver Layer



The \*\*Silver Layer\*\* contains cleaned and transformed data.



\### Transformations Performed



\- Removed duplicate records

\- Cleaned invalid records

\- Converted timestamp columns

\- Standardized data format

\- Prepared data for analysis



\---



\## 🥇 Gold Layer



The \*\*Gold Layer\*\* contains aggregated and business-ready data.



\### Metrics Created



\- Total Orders

\- Total Revenue

\- Average Order Value

\- City-wise Revenue

\- Highest Sales

\- Lowest Sales



\---



\## 📊 Power BI Dashboard



An interactive Power BI dashboard was created to analyze sales performance and business KPIs.



\### Dashboard Includes



\- Total Revenue

\- Total Orders

\- Average Order Value

\- City-wise Sales

\- Sales Trends

\- KPI Cards

\- Visual Analytics



\---



\## 👩‍💻 Responsibilities



\- Designed a real-time event-driven data pipeline

\- Ingested streaming order data into Kafka topics

\- Processed streaming data using PySpark Structured Streaming

\- Implemented Medallion Architecture: Bronze, Silver, Gold

\- Performed data cleansing, deduplication, timestamp conversion, and aggregations

\- Built an interactive Power BI dashboard with KPIs and visual analytics

\- Containerized Kafka environment using Docker Compose

\- Managed project version control using Git and GitHub



\---



\## 📁 Project Structure



```text

RealTime-Streaming-Project/

│

├── producer/

│   └── producer.py

│

├── spark\_jobs/

│   ├── bronze\_to\_silver.py

│   └── silver\_to\_gold.py

│

├── data/

│   ├── bronze/

│   ├── silver/

│   └── gold/

│

├── docker-compose.yml

├── README.md

└── .gitignore

```



\---



\## ⚙️ How to Run the Project



\### 1. Start Kafka using Docker



```bash

docker-compose up -d

```



\### 2. Run the Data Producer



```bash

python producer/producer.py

```



\### 3. Run Spark Streaming Job



```bash

spark-submit spark\_jobs/bronze\_to\_silver.py

```



\### 4. Run Gold Layer Aggregation



```bash

spark-submit spark\_jobs/silver\_to\_gold.py

```



\### 5. Open Power BI Dashboard



Open the Power BI file and connect it with Gold Layer output data.



\---



\## 🎯 Project Outcome



This project demonstrates how real-time sales data can be ingested, processed, cleaned, aggregated, and visualized using modern Data Engineering tools.



It shows practical implementation of:



\- Real-time data streaming

\- Kafka-based ingestion

\- Spark Structured Streaming

\- Medallion Architecture

\- CSV Data Lake storage

\- Power BI reporting



\---



\## 👤 Author



\*\*Vedanti Rohankar\*\*



Data Analyst | Power BI Developer | Aspiring Data Engineer



\---



\## 🔗 GitHub Repository



```text

https://github.com/vedantirohankar/RealTime-Streaming-Project

```
>>>>>>> 4b3dd6a (Add detailed README with architecture image)

```text
Data Producer
     ↓
Raw Streaming Data
     ↓
Bronze Layer
     ↓
Silver Layer
     ↓
Gold Layer
     ↓
Analytics / Reporting
