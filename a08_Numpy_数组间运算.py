import numpy as np
arr1=np.array([[1,2,4,3,6,7,8],[3,4,6,5,3,2,7]])
arr2=np.array([[1,2,4,3,6,7,8],[3,4,6,5,3,2,7]])

# 数组与数的运算
data=arr1+10
print(data)
# 数组与数组运算
# 形状相同的
print(arr1*arr2)
# 形状不同的数组
arr3=np.array(
[[1,2,3],
 [4,5,6],
 [7,8,9]])
arr4=np.array(
    [1,2,3]
)
# arr3和arr4兼容
print(arr3*arr4)# 广播机制：arr3每一行乘arr4
