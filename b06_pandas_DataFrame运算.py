import pandas as pd
# 算数运算
data=pd.read_csv("D:/factor_returns.csv")
print(data.head())
# 加
data['pe_ratio']=data['pe_ratio'].add(1)
print(data.head())
# 减
data['pe_ratio']=data['pe_ratio'].sub(1)
print(data.head())

# 逻辑运算
print(data[data['pe_ratio']>50])
print(data.head())

# query
print(data.query('pe_ratio>50'))

#isin参数不表示范围，而是列表
print(data[data['pe_ratio'].isin([59.4849,52.5408])])

# 统计运算
print(data.describe())
# 其他单独指标可以单独调用函数
print(data.idxmax(axis=0))# 每列最大值所在的行索引
print(data.idxmin(axis=0))# 每列最小值所在的行索引

# 累计统计函数
print(data['pe_ratio'].cumsum())# 前n个数据累计
print(data['pe_ratio'].cummax())# 前n个数据最大值
print(data['pe_ratio'].cummin())# 前n个数据最小值
print(data['pe_ratio'].cumprod())# 前n个数据乘积

# 自定义运算
print(data['pe_ratio'].apply(lambda x: x*2))# 默认对列操作，要修改则设置第二个函数axis=1