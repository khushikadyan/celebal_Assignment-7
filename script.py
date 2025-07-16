import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
import re
import warnings

# Suppress specific warnings
warnings.filterwarnings('ignore', category=UserWarning, message='The provided table name.*')

def get_db_connection():
    try:
        password = "sonikhushi@123"
        encoded_password = quote_plus(password)
        
        # Added charset and other parameters for better connection
        connection_string = f'mysql+pymysql://root:{encoded_password}@localhost/data_processing?charset=utf8mb4'
        engine = create_engine(connection_string)
        
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise

def create_tables(engine):
    """Ensure all tables exist with correct structure"""
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS cust_mstr (
                customer_id INT,
                customer_name VARCHAR(100),
                email VARCHAR(100),
                load_date DATE
            )
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS master_child (
                parent_id INT,
                child_id INT,
                relationship VARCHAR(50),
                load_date DATE,
                date_key INT
            )
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS h_ecom_orders (
                order_id INT,
                product_id INT,
                quantity INT,
                order_date DATE
            )
        """))

def process_files_in_directory(directory):
    try:
        engine = get_db_connection()
        create_tables(engine)
        
        # Truncate tables (using lowercase names)
        with engine.begin() as connection:
            connection.execute(text("TRUNCATE TABLE cust_mstr"))
            connection.execute(text("TRUNCATE TABLE master_child"))
            connection.execute(text("TRUNCATE TABLE h_ecom_orders"))
        
        # Process files
        for filename in sorted(os.listdir(directory)):
            file_path = os.path.join(directory, filename)
            
            try:
                if filename.startswith('CUST_MSTR_') and filename.endswith('.csv'):
                    # Process CUST_MSTR files
                    date_str = re.search(r'CUST_MSTR_(\d{8})\.csv', filename).group(1)
                    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
                    df = pd.read_csv(file_path)
                    df['load_date'] = pd.to_datetime(formatted_date)
                    df.to_sql('cust_mstr', engine, if_exists='append', index=False)
                    
                elif filename.startswith('master_child_export-') and filename.endswith('.csv'):
                    # Process master_child files
                    date_str = re.search(r'master_child_export-(\d{8})\.csv', filename).group(1)
                    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
                    date_key = int(date_str)
                    df = pd.read_csv(file_path)
                    df['load_date'] = pd.to_datetime(formatted_date)
                    df['date_key'] = date_key
                    df.to_sql('master_child', engine, if_exists='append', index=False)
                    
                elif filename.lower() == 'h_ecom_order.csv':
                    # Process H_ECOM_ORDER file (case insensitive)
                    df = pd.read_csv(file_path)
                    if 'order_date' in df.columns:
                        df['order_date'] = pd.to_datetime(df['order_date'])
                    df.to_sql('h_ecom_orders', engine, if_exists='append', index=False)
                    
                print(f"Processed {filename} successfully")
                
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                
    except Exception as e:
        print(f"Error in processing directory: {str(e)}")
    finally:
        if 'engine' in locals():
            engine.dispose()

if __name__ == "__main__":
    data_lake_directory = "data_lake"
    if not os.path.exists(data_lake_directory):
        os.makedirs(data_lake_directory)
        print(f"Created directory: {data_lake_directory}")
        print("Please add your CSV files to this directory and run again")
    else:
        process_files_in_directory(data_lake_directory)