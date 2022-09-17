from scipy.optimize import linear_sum_assignment
import numpy as np

# 整数规划(这里是0-1规划)的典型问题：指派问题，比如怎么分配工人去做任务耗时最短，收益最大等等

# 首先把成本矩阵列出来：
T=np.array([[25,29,31,42],[39,38,26,20],[34,27,28,40],[24,42,36,23]])
row_ind,col_ind=linear_sum_assignment(T)   
print(row_ind)    # row_ind返回的是任务列表的id
print(col_ind)    # col_ind返回的是最优指派的列索引
print(T[row_ind,col_ind])    # 打印求解出的指派任务所需时间
print(T[row_ind,col_ind].sum())    # 求解出时间代价总和