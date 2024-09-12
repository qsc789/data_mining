import pandas as pd
import numpy as np
data=np.random.normal(0,1,(10,5))
stock=["股票{}".format(i) for i in range(10)]
date=pd.date_range(start="20180101",periods=5,freq="B")
data=pd.DataFrame(data,index=stock,columns=date)
# 索引修改
stock_=["股票_{}".format(i) for i in range(10)]
data.index=stock_
# 重设索引
data=data.reset_index(drop=True)
print(data)
print(data.index)
# 设置新索引
df=pd.DataFrame({'month':[1,4,7,10],'year':[2012,2014,2013,2014],'sale':[55,40,84,31]})
print(df)
# 把月份设置为新的行索引
new_df=df.set_index("month",drop=True)
print(new_df)

# 设置多个索引
df=df.set_index(['year','month'])
print(df)
print(df.index.names)
print(df.index.levels)