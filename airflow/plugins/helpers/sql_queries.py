class SqlQueries:
    location_table_insert = ("""
        INSERT INTO location (
            country_name
        )
        SELECT DISTINCT 
            Country
        FROM staging_table;
    """)

    invoice_table_insert = ("""
        INSERT INTO invoices (
              invoice_num,
              invoice_date
        )
        SELECT DISTINCT 
            InvoiceNo,
            InvoiceDate
        FROM staging_table;
    """)

    customer_table_insert = ("""
        INSERT INTO customers (
            customer_id
        )
        SELECT DISTINCT 
            CustomerID
        FROM staging_table;
    """)

    product_table_insert = ("""
        INSERT INTO products (
            stock_code,
            description,
            UnitPrice       
        )
        SELECT DISTINCT
            StockCode,
            Description,
            UnitPrice   
        FROM staging_table;
    """)
    
    order_table_insert = ("""
        INSERT INTO orders (
        country_id,
        invoice_num,
        invoice_date,
        customer_id,
        product_id,
        quantity
        )
        SELECT 
            L.country_id,
            ST.InvoiceNo,
            ST.invoice_date,
            CU.customer_id,
            P.product_id,
            ST.quantity
        FROM staging_table ST
        LEFT JOIN location L on ST.Country = L.country_name
        LEFT JOIN products P on ST.StockCode = P.stock_code
            
    """)

    time_table_insert = ("""
        INSERT INTO time (
            invoice_date,
            hour,
            day,
            week,
            month,
            year,
            weekday
        )
        SELECT InvoiceDate, extract(hour from InvoiceDate), extract(day from InvoiceDate), extract(week from InvoiceDate), 
               extract(month from InvoiceDate), extract(year from InvoiceDate), extract(dayofweek from InvoiceDate)
        FROM staging_table;
    """)