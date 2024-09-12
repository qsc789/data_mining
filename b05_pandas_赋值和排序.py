import pandas as pd

data=pd.read_csv("D:/factor_returns.csv")
print(data.head())
# 直接改
data.iloc[0,1]=5.9672
print(data.head())

# 排序
# 内容排序
data=data.sort_values(by="pe_ratio",ascending=False)
data=data.sort_values(by=["pe_ratio","pb_ratio"],ascending=False)
print(data.head())
# 索引排序
data=data.sort_index(ascending=True)
print(data.head())

sr=data['pe_ratio']
sr=sr.sort_values(ascending=True)
print(sr.head())