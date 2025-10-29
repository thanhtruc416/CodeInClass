from retail_project.connectors.connector import Connector

conn = Connector(database="salesdatabase")  # tạo đối tượng
conn.connect()                               # mở kết nối
sql = "SELECT * FROM customer"
df = conn.queryDataset(sql)                  # lấy dữ liệu về DataFrame
print(df)
print(df.columns)
