import pandas as pd


def top3_products_overall(df):
    """
    Trả về top 3 sản phẩm có tổng giá trị bán ra cao nhất trên toàn bộ dữ liệu.
    Output: list [(ProductID, TotalValue), ...]
    """
    # Tính tổng giá trị từng dòng
    df['Total'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])

    # Tính tổng giá trị theo ProductID
    product_totals = df.groupby('ProductID')['Total'].sum()

    # Lấy top 3 sản phẩm có tổng giá trị cao nhất
    top3 = product_totals.sort_values(ascending=False).head(3)

    return list(zip(top3.index, top3.values))


# ---- Demo ----
df = pd.read_csv('../Dataset/SalesTransactions.csv')

result = top3_products_overall(df)

print("Top 3 sản phẩm có giá trị bán ra cao nhất:")
for product_id, total in result:
    print(f"ProductID: {product_id}, TotalValue: {total}")
