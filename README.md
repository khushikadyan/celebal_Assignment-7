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
| Path                                       | Description                       |
| ------------------------------------------ | --------------------------------- |
| `ASSIG.../`                                | 📁 Parent folder                  |
| ├── `data_lake/`                           | 📂 Input files directory          |
| │   ├── `CUST_MSTR_20191112.csv`           | Customer master file (2019-11-12) |
| │   ├── `CUST_MSTR_20191113.csv`           | Customer master file (2019-11-13) |
| │   ├── `H_ECOM_ORDER.csv`                 | E-commerce orders file            |
| │   └── `master_child_export-20191112.csv` | Master-child data file            |
| ├── `script.py`                            | 🧠 Main data processing script    |
| ├── `test.py`                              | 🔌 Database connection test       |
| └── `server.sql`                           | 🗄️ SQL schema creation script    |


## Setup
1. Install requirements: `pip install -r requirements.txt`
   ```bash
   pip install -r requirements.txt
   ```
3. Configure database connection in `config.ini`
4. Place CSV files in `data_lake` directory
5. Run:
   ```bash
    `python src/main.py`
   ```

6. Clone the repository:
   ```bash
   git clone https://github.com/your-username/assignment-data-pipeline.git
   cd assignment-data-pipeline
   ```
---
## Screenshots

<img width="605" height="172" alt="Screenshot 2025-07-16 190504" src="https://github.com/user-attachments/assets/fc493231-b68e-4782-b471-090946375d1a" />

<img width="455" height="123" alt="Screenshot 2025-07-16 190515" src="https://github.com/user-attachments/assets/0f1b06b3-c49c-41cd-b321-a8e7835842b4" />

<img width="365" height="104" alt="Screenshot 2025-07-16 190525" src="https://github.com/user-attachments/assets/d6d47f65-9a50-426f-9d05-9508529fc341" />

## Author
Khushi Kadyan

Btech CSE (DSAI)
