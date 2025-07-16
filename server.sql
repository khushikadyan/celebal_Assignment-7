CREATE DATABASE data_processing;

USE data_processing;

CREATE TABLE CUST_MSTR (
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    load_date DATE
);

CREATE TABLE master_child (
    parent_id INT,
    child_id INT,
    relationship VARCHAR(50),
    load_date DATE,
    date_key INT
);

CREATE TABLE H_ECOM_Orders (
    order_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);


SELECT * FROM CUST_MSTR;


SELECT * FROM master_child;

SELECT * FROM H_ECOM_Orders;
