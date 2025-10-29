import pandas as pd

df=pd.read_json ('../Dataset/SalesTransactions.json',encoding='utf-8',dtype ="unicode")
print(df)