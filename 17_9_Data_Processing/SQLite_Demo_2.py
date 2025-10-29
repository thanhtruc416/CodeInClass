import sqlite3
import pandas as pd

def top_customers_with_invoices(db_path):
    # Nhập input top_n từ người dùng
    top_n = int(input("Nhập số khách hàng cần lấy (top_n): "))

    # Kết nối CSDL
    conn = sqlite3.connect(db_path)

    query = f"""
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName AS CustomerName,
        c.Email,
        COUNT(i.InvoiceId) AS InvoiceCount,
        SUM(i.Total) AS TotalValue
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId
    ORDER BY TotalValue DESC, InvoiceCount DESC
    LIMIT {top_n};
    """

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Gọi hàm
db_path = "../databases/Chinook_Sqlite.sqlite"
df_result = top_customers_with_invoices(db_path)
print(df_result)