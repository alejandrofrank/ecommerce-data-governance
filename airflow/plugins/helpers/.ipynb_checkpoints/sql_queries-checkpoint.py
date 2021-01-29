class SqlQueries:
    location_table_insert = ("""
        INSERT INTO location (
            country_id,
            country
        )
        SELECT DISTINCT 
            
            FROM staging_table
    """)

    invoice_table_insert = ("""
        INSERT INTO invoices (
              invoice_id,
              InvoiceNo
        )
        SELECT DISTINCT 
        FROM staging_table
    """)

    customer_table_insert = ("""
        INSERT INTO customers (
            customer_id
        )
        SELECT DISTINCT 
        FROM staging_table
    """)

    artist_table_insert = ("""
        INSERT INTO artists (
            artistid,
            name,
            location,
            latitude,
            longitude        
        )
        SELECT DISTINCT 
        FROM staging_table
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
        FROM staging_table
    """)