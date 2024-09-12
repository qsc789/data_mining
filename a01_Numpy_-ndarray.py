import numpy as np
score=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(f"几行几列：{score.shape}")
print(f"数据类型：{score.dtype}")
print(f"数据个数：{score.size}")
data=np.array([1,2,3,4,5])
print(f"几行几列：{data.shape}")# (5,)
data1=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(f"几行几列：{data1.shape}")# (2,2,3)