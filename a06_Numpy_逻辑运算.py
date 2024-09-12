import numpy as np

stock_change = np.random.normal(0, 1, (8, 10))
# 逻辑判断，涨跌幅大于0.5标记为True，否则为False
data = stock_change > 0.5
print(data)
# 筛选出来
data = stock_change[stock_change > 0.5]
print(data)

# 通用判断函数
print(np.all(stock_change > 0))  # 全是True才返回True
print(np.any(stock_change > 0))  # 一个是True就返回True
data = np.where(stock_change > 0, 1, 0)  # True则置为第二个参数，False则置为第三个参数
print(data)
data = np.where(np.logical_and(stock_change > 0, stock_change < 0.5), 1, 0) # 前两个条件与，True则置为第二个参数，False则置为第三个参数
print(data)
data = np.where(np.logical_or(stock_change > 0, stock_change < -0.5), 1, 0) # 前两个条件或，True则置为第二个参数，False则置为第三个参数
print(data)
