import numpy as np
# 水平拼接
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.hstack((a,b))
print(c)
a=np.array([
    [1],
    [2],
    [3]
])
b=np.array([
    [4],
    [5],
    [6]
])
c=np.hstack((a,b))
print(c)
# 垂直拼接
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.vstack((a,b))
print(c)

c=np.concatenate((a,b),axis=0)# 水平
# c=np.concatenate((a,b),axis=1)
print(c)

# c=np.concatenate((a,b),axis=1)


# 分割
x=np.arange(9)
print(x)
y=np.split(x,3)# 分为三等份
print(y)
y=np.split(x,[4,7])# 分割点索引为4和7
print(y)