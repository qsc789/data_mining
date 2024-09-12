import numpy as np
stock_change=np.random.normal(0,1,(8,10))
# 统计运算
temp=stock_change[0:4,0:4]
print(temp)
print(f"前4只股票前4天涨幅最大为：{temp.max()}")
print(f"前4只股票前4天涨幅最大为：{np.max(temp)}")
print(f"前4只股票前4天涨幅最小为：{temp.min()}")
print(f"前4只股票前4天涨幅最小为：{np.min(temp)}")

print(f"前4只股票每只股票在这4天内涨幅最大为：{temp.max(axis=0)}")# axis=0表示按列求最大值
print(f"前4只股票前4天每天涨幅最大为：{temp.max(axis=1)}")# axis=1表示按行求最大值
print(f"前4只股票前4天标准差：{temp.std(axis=1)}")
print(f"前4只股票前4天平均值：{temp.mean(axis=1)}")

print(f"每行最大值索引：{np.argmax(temp,axis=1)}")