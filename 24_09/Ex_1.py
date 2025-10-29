"""
Viết 1 hàm có mô tả:
Input:
-DataFrame => df -> đọc file
-Tổng Giá Trị Min =>minValue ->
-Tổng Giá Trị Max =>maxValue
-SortType=>True/False

Output:
-Trả về danh sách các hóa đơn (mã hóa đơn + tổng giá trị ) mà tổng trị giá của nó nằm trong [minValue …maxValue] và sắp xếp theo SortType
"""
import pandas as pd


def find_orders_within_range(df,minValue,maxValue):
    # tổng giá trị từng đơn hàng
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    # Lọc đơn hàng trong range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
    #danh sach cac ma don hang khong trung nhau
    unique_orders = df [df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
    return unique_orders

df=pd.read_csv('../Dataset/SalesTransactions.csv')

minValue =float(input("Nhap Min: "))
maxValue =float(input("Nhap Max: "))
result=find_orders_within_range(df,minValue,maxValue)
print('Danh sach cac hoa don trong pham vi gia tri tu', minValue, 'den',maxValue,' la',result)