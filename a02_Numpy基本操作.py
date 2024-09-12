import numpy as np
zero=np.zeros(shape=(3,4),dtype="int32")# 生成全0数组
print(zero)
data1=np.linspace(0,10,50)# 在[0,10]范围等距离取50个数
print(data1)
data2=np.arange(10,20,2)# [a,b),c是步长
print(data2)
# 均匀分布,取数的概率相等
x1=np.random.uniform(low=0.0,high=1.0,size=10)
print(x1)
# 正态分布,标准差越大，数据分布越散
x2=np.random.normal(loc=0.0,scale=1.0,size=10)# 均值，标准差，大小
print(x2)

# 矩阵乘法
A=np.array([
    [90,89],
    [78,86],
    [96,90]
])
B=np.array([
    [0.3],
    [0.7]
])
C=np.dot(A,B)
print(C)
C=np.matmul(A,B)
print(C)

A=np.mat([
    [90,89],
    [78,86],
    [96,90]
])
B=np.mat([
    [0.3],
    [0.7]
])
print(A*B)