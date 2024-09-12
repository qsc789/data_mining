import numpy as np
stock_change=np.random.normal(0,1,(8,10))
# 重新分割数据，顺序没变
print(stock_change.reshape((10,8)))
# 没有返回值，对原始数组进行修改。也是顺序没变
stock_change.resize((10,8))
print(stock_change)
stock_change.resize((8,10))
print(stock_change)
# 纯转置
print(stock_change.T)

# 转类型
print(stock_change.astype(int))
# 转字节
print(stock_change.tobytes())