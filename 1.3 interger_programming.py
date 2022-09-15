from scipy.optimize import linear_sum_assignment
import numpy as np
T=np.array([[25,29,31,42],[39,38,26,20],[34,27,28,40],[24,42,36,23]])
row_ind,col_ind=linear_sum_assignment(T)
print(row_ind)
print(col_ind)
print(T[row_ind,col_ind])
print(T[row_ind,col_ind].sum())