import pandas as pd

data=pd.read_csv("D:/factor_returns.csv")
print(data.head())
# 删除行列
data=data.drop([0,1],axis=0)
print(data.head())

# 索引操作
# 直接使用行列索引（先列后行）
print(data['date'][3])
# loc按名字索引，先行后列
print(data.columns)
print(data.loc[3:7,'index':'pb_ratio'])
# iloc按位置索引，先行后列
print(data.iloc[3,2])
