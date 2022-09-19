# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:54:04 2022

@author: Mashituo
"""
import numpy as np
import pandas as pd

#TOPSIS方法函数
def Topsis(A1):
    W0=[0.2,0.3,0.4,0.1] #权重矩阵，这个权重矩阵可以根据4.2的熵权法去算而不是简单的主观赋值（这里就是自己直接设了个权值）
    W=np.ones([A1.shape[1],A1.shape[1]],float)
    for i in range(len(W)):
        for j in range(len(W)):
            if i==j:
                W[i,j]=W0[j]
            else:
                W[i,j]=0
    Z=np.ones([A1.shape[0],A1.shape[1]],float)
    Z=np.dot(A1,W) #加权矩阵
    
    #计算正、负理想解
    Zmax=np.ones([1,A1.shape[1]],float)
    Zmin=np.ones([1,A1.shape[1]],float)
    for j in range(A1.shape[1]):
        if j==3:
            Zmax[0,j]=min(Z[:,j])
            Zmin[0,j]=max(Z[:,j])
        else:
            Zmax[0,j]=max(Z[:,j])
            Zmin[0,j]=min(Z[:,j])

    #计算各个方案的相对贴近度C
    C=[]  
    for i in range(A1.shape[0]):
            Smax=np.sqrt(np.sum(np.square(Z[i,:]-Zmax[0,:])))
            Smin=np.sqrt(np.sum(np.square(Z[i,:]-Zmin[0,:])))
            C.append(Smin/(Smax+Smin))
    C=pd.DataFrame(C,index=['院校' + i for i in list('12345')])   
    return C

#标准化处理
def standard(A):
    #效益型指标
    A1=np.ones([A.shape[0],A.shape[1]],float)
    for i in range(A.shape[1]):
        if i==0 or i==2:
            if max(A[:,i])==min(A[:,i]):
                A1[:,i]=1
            else:
                for j in range(A.shape[0]):
                    A1[j,i]=(A[j,i]-min(A[:,i]))/(max(A[:,i])-min(A[:,i]))
    
    #成本型指标
        elif i==3:
            if max(A[:,i])==min(A[:,i]):
                A1[:,i]=1
            else:
                for j in range(A.shape[0]):
                    A1[j,i]=(max(A[:,i])-A[j,i])/(max(A[:,i])-min(A[:,i])) 

    #区间型指标
        else:
            a,b,lb,ub=5,6,2,12
            for j in range(A.shape[0]):
                if lb <= A[j,i] < a:
                    A1[j,i]=(A[j,i]-lb)/(a-lb)
                elif a <= A[j,i] < b:
                    A1[j,i]=1		
                elif b <= A[j,i] <= ub:
                    A1[j,i]=(ub-A[j,i])/(ub-b)
                else:  #A[i,:]< lb or A[i,:]>ub
                    A1[j,i]=0	
    return A1

#读取初始矩阵并计算
def data(file_path):
    data=pd.read_excel(file_path).values
    A=data[:,1:]
    A=np.array(A)
    #m,n=A.shape[0],A.shape[1] #m表示行数,n表示列数
    return A

#权重
A=np.array([[0.1,5,5000,4.7],[0.2,6,6000,5.6],[0.4,7,7000,6.7],[0.9,10,1000,2.3],[1.2,2,400,1.8]])
A1=standard(A)
C=Topsis(A1)
print(C)


