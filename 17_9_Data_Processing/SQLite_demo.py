import sqlite3
import pandas as pd

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print("DB Init")

    # Write a query and execute it with cursor
    query = 'SELECT * FROM Invoiceline LIMIT 5;'
    cursor.execute(query)

    # Fetch result
    rows = cursor.fetchall()

    # Lấy tên cột từ cursor
    col_names = [description[0] for description in cursor.description]

    # Chuyển sang DataFrame với tên cột
    df = pd.DataFrame(rows, columns=col_names)
    print(df)

    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print("Error occurred - ", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection closed")
