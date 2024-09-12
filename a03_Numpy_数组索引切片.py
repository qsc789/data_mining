import numpy as np
stock_change=np.random.normal(0,1,(8,10))
print(stock_change)
# 获取第一个股票前3个交易日的涨跌
print(stock_change[0,0:3])
data1=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(data1[0,0,0])