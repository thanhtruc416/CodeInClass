import pandas as pd
from numpy import nan as NA
data =pd.DataFrame([[1.,6.5,3.],
                    [1.,NA,NA],
                    [NA, NA, NA],
                    [NA,6.5,3],
                    [3, 6.5,3],
                    [4, 7.5, 7],
                    [5, 2.5, 3.],
                    [NA, NA, NA],
                    [6,3.5,3]
                    ])
print (data)
print("*"*10)
cleaned=data.fillna(data.mean())
print(cleaned)