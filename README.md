# Data Processing Pipeline Assignment

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-blue)

A Python solution for processing CSV files from a data lake into a MySQL database with different transformations for each file type.
This project is designed to automate the ingestion and transformation of multiple CSV files from a data lake and load them into a structured SQL database. The solution supports **truncate-load** logic on a **daily basis**.

## Features

- Processes 3 distinct file types with custom transformations
- Extracts dates from filenames and adds as new columns
- Implements daily truncate-load functionality
- MySQL database integration with proper connection handling
- Automated file processing pipeline

## File Types Processed

| File Pattern | Transformations | Destination Table |
|-------------|----------------|------------------|
| `CUST_MSTR_YYYYMMDD.csv` | Adds `load_date` (format: YYYY-MM-DD) | `CUST_MSTR` |
| `master_child_export-YYYYMMDD.csv` | Adds `load_date` (YYYY-MM-DD) and `date_key` (YYYYMMDD) | `master_child` |
| `H_ECOM_ORDER.csv` | No transformations (loaded as-is) | `H_ECOM_Orders` |

## Repository Structure
├── datalake/
│ ├── CUST_MSTR_20191112.csv
│ ├── CUST_MSTR_20191113.csv
│ ├── master_child_export-20191112.csv
│ └── H_ECOM_ORDER.csv
├── script.py # Main ETL pipeline script
├── tesst.py # Script used for testing/debugging
└── server.sql # SQL file for creating required tables
