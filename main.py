import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')


customer_country_count = pd.read_sql("""
    SELECT country, COUNT(*) 
    FROM customers 
    GROUP BY country;
""", conn).head()
# print(customer_country_count)


customer_country_count = pd.read_sql("""
    SELECT country, COUNT(*) AS customer_count 
    FROM customers 
    GROUP BY country
    HAVING COUNT(*) > 3;
""", conn)
# print(customer_country_count)


summary_stats = pd.read_sql("""
    SELECT 
    customerNumber,
    COUNT(*) AS payments_num,
    MIN(CAST(amount AS FLOAT)) AS min_purchase,
    MAX(CAST(amount AS FLOAT)) AS max_purchase,
    AVG(CAST(amount AS FLOAT)) AS avg_purchase,
    SUM(CAST(amount AS FLOAT)) AS total_spent
    
    FROM payments
    WHERE strftime('%Y', paymentDate) = '2004'
    GROUP BY customerNumber;
""", conn)
# print(summary_stats)


avg_payment_5000 = pd.read_sql("""
    SELECT 
    customerNumber,
    COUNT(*) AS payments_num,
    MIN(CAST(amount AS FLOAT)) AS min_purchase,
    MAX(CAST(amount AS FLOAT)) AS max_purchase,
    AVG(CAST(amount AS FLOAT)) AS avg_purchase,
    SUM(CAST(amount AS FLOAT)) AS total_spent
    
    FROM payments
    GROUP BY customerNumber
    HAVING AVG(CAST(amount AS FLOAT)) > 50000;
""", conn)
# print(avg_payment_5000)


summary_stats = pd.read_sql("""
    SELECT 
    customerNumber,
    COUNT(*) AS purchase_num,
    MIN(CAST(amount AS FLOAT)) AS min_purchase,
    MAX(CAST(amount AS FLOAT)) AS max_purchase,
    AVG(CAST(amount AS FLOAT)) AS avg_purchase,
    SUM(CAST(amount AS FLOAT)) AS total_spent
    
    FROM payments
    WHERE CAST(amount AS FLOAT) > 50000
    GROUP BY customerNumber
    HAVING purchase_num >= 2;
""", conn)
# print(summary_stats)


lowest_50000_spender = pd.read_sql("""
    SELECT 
    customerNumber,
    COUNT(*) AS purchase_num,
    MIN(CAST(amount AS FLOAT)) AS min_purchase,
    MAX(CAST(amount AS FLOAT)) AS max_purchase,
    AVG(CAST(amount AS FLOAT)) AS avg_purchase,
    SUM(CAST(amount AS FLOAT)) AS total_spent
    
    FROM payments
    WHERE CAST(amount AS FLOAT) > 50000
    GROUP BY customerNumber
    HAVING purchase_num >= 2
    ORDER BY total_spent
    LIMIT 1;
""", conn)
print(lowest_50000_spender)


conn.close()