import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',          # your MySQL username
        password='sonikhushi@123',  # your MySQL password
        database='data_processing'
    )
    print("Successfully connected to MySQL!")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")