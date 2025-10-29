import pandas as pd
from numpy import nan as NA
data =pd.DataFrame([[1.,6.5,3.],
                    [1.,NA,NA],
                    [NA, NA, NA],
                    [NA,6.5,3]])
print (data)
print ("-"*10)
clean=data.dropna() # loại dòng có NA (chỉ 1 cột vẫn bỏ)
print (clean)
clean2=data.dropna(how='all') # chỉ loại dòng chứa toàn bộ NA
print ("-"*10)
print(clean2)