import numpy as np

A = np.array([[1,1/3,1/4,1/5],
              [3,1,3/4,3/5],
              [4,4/3,1,4/5],
              [5,5/3,5/4,1]])
m=len(A)                                    #获取指标个数
n=len(A[0])
RI=[0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]
R= np.linalg.matrix_rank(A)                #求判断矩阵的秩
V,D=np.linalg.eig(A)                       #求判断矩阵的特征值和特征向量，V特征值，D特征向量；
list1 = list(V)
B= np.max(list1)                           #最大特征值
index = list1.index(B)
C = D[:, index]                            #对应特征向量
CI=(B-n)/(n-1)                             #计算一致性检验指标CI
CR=CI/RI[n]
if CR<0.10:
    print("CI=", CI)
    print("CR=", CR)
    print('对比矩阵A通过一致性检验，各向量权重向量Q为：')
    sum=np.sum(C)

    Q=C/sum                               #特征向量标准化
    print(Q)                              #  输出权重向量
else:
    print("对比矩阵A未通过一致性检验，需对对比矩阵A重新构造")