#DROP QUERIES

staging_table_drop = "DROP TABLE IF EXISTS staging"

location_table_drop = "DROP TABLE IF EXISTS location"

orders_table_drop = "DROP TABLE IF EXISTS orders;"

invoices_table_drop = "DROP TABLE IF EXISTS invoices;"

products_table_drop = "DROP TABLE IF EXISTS products;"

customers_table_drop = "DROP TABLE IF EXISTS customers;"

time_table_drop = "DROP TABLE IF EXISTS time;"

#CREATE QUERIES

staging_table = ("""
CREATE TABLE staging_songs
(
  InvoiceNo     INTEGER    NOT NULL,
  StockCode     VARCHAR    NOT NULL,
  Description   VARCHAR    NULL,
  Quantity      INTEGER    NOT NULL,
  InvoiceDate   TIMESTAMP  NOT NULL,
  UnitPrice     FLOAT      NOT NULL,
  CustomerID    INTEGER    NULL,
  Country       VARCHAR    NOT NULL
);
""")

location_table = ("""
CREATE TABLE location
(
  country_id    BIGINT IDENTITY(0,1)  NOT NULL PRIMARY KEY,
  country       VARCHAR
);
""")

invoice_table = ("""
CREATE TABLE invoices
(
  invoice_id    BIGINT IDENTITY(0,1)  NOT NULL PRIMARY KEY,
  InvoiceNo     INTEGER NOT NULL
);
""")

time_table = ("""
CREATE TABLE time
(
  invoice_date  TIMESTAMP    NOT NULL, 
  hour          DECIMAL      NOT NULL, 
  day           INTEGER      NOT NULL, 
  week          INTEGER      NOT NULL, 
  month         INTEGER      NOT NULL, 
  year          INTEGER      NOT NULL, 
  weekday       INTEGER      NOT NULL
);
""")

customer_table = ("""
CREATE TABLE customers
(
  customer_id   INTEGER    PRIMARY KEY
);
""")

product_table = ("""
CREATE TABLE products
(
  product_id    BIGINT IDENTITY(0,1)  NOT NULL PRIMARY KEY,
  stock_code    VARCHAR    NOT NULL,
  description   VARCHAR    NULL,
  UnitPrice     FLOAT      NOT NULL
);
""")

order_table = ("""
CREATE TABLE orders
(
  order_id       BIGINT IDENTITY(0, 1) NOT NULL PRIMARY KEY,
  country_id     INTEGER    NOT NULL,
  invoice_id     INTEGER    NOT NULL,
  invoice_date   TIMESTAMP  NOT NULL,
  customer_id    INTEGER    NULL,
  product_id     INTEGER    NOT NULL,
  quantity       INTEGER    NOT NULL
);
""")

#copy query

staging_copy = ("""
    COPY {} 
    FROM {'s3://ciphor/TABLE_A.csv'}
    CREDENTIALS 'aws_iam_role={}'
    delimiter ','
    STATUPDATE ON
    region 'us-west-2'
    removequotes;
""").format(LOG_DATA, IAM_ROLE, LOG_JSONPATH)

