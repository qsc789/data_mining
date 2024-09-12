import numpy as np
import pandas as pd
data=np.random.normal(0,1,(10,5))
stock=["股票{}".format(i) for i in range(10)]
date=pd.date_range(start="20180101",periods=5,freq="B")
data=pd.DataFrame(data,index=stock,columns=date)# 行索引，列索引
print(data)
print(data.shape)
print(data.index)
print(data.columns)
print(data.values)
print(data.T)
print(data.head())
print(data.tail())
