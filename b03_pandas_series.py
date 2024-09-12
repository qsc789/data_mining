import pandas as pd
import numpy as np

data=np.random.normal(0,1,(10,5))
stock=["股票{}".format(i) for i in range(10)]
date=pd.date_range(start="20180101",periods=5,freq="B")
data=pd.DataFrame(data,index=stock,columns=date)
print(data)
# 截取series
sr=data.iloc[1,:]# 索引为1的行
print(sr)
print(sr.index)
print(sr.values)
# 创建series
sr2=pd.Series(np.arange(10))
print(sr2)
# 指定索引
sr3=pd.Series([8.3,8.4,7.4,3.6,5.9],index=[1,2,3,4,5])
print(sr3)
# 字典创建
sr4=pd.Series({'red':100,'blue':200,'green':500,'yellow':1000})
print(sr4)

# 获取索引
print(sr4.index)
# 获取值
print(sr4.values)