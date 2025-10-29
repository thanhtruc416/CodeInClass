import pandas as pd
df=pd.read_csv("../Dataset/SalesTransactions.txt")
# 2 chấm vì Class -> DataSet -> file .py
print(df)
# Không có dấu tiếng việt -> không cần utf-8
# low_mermory -> ưu tiên bộ nhớ
df=pd.read_csv("../Dataset/SalesTransactions.txt", encoding='utf-8',dtype ='unicode',sep='\t',low_memory=False)
print(df)