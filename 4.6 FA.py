# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 09:19:43 2021

@author: mashituo
"""
from factor_analyzer import FactorAnalyzer
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import math
from scipy.stats import bartlett
plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.style.use("ggplot")

n_factors=3#因子数量
cols=['小学生师比(教师人数=1)', '初中生师比(教师人数=1)',
       '普通高中生师比(教师人数=1)', '职业高中生师比(教师人数=1)', '普通中专生师比(教师人数=1)',
       '普通高校生师比(教师人数=1)', '本科院校生师比(教师人数=1)', '专科院校生师比(教师人数=1)']
 
#用检验是否进行
corr=list(newdata[cols].corr().to_numpy())
print(bartlett(*corr))
def kmo(dataset_corr):
    corr_inv = np.linalg.inv(dataset_corr)
    nrow_inv_corr, ncol_inv_corr = dataset_corr.shape
    A = np.ones((nrow_inv_corr,ncol_inv_corr))
    for i in range(0,nrow_inv_corr,1):
        for j in range(i,ncol_inv_corr,1):
            A[i,j] = -(corr_inv[i,j])/(math.sqrt(corr_inv[i,i]*corr_inv[j,j]))
            A[j,i] = A[i,j]
    dataset_corr = np.asarray(dataset_corr)
    kmo_num = np.sum(np.square(dataset_corr)) - np.sum(np.square(np.diagonal(A)))
    kmo_denom = kmo_num + np.sum(np.square(A)) - np.sum(np.square(np.diagonal(A)))
    kmo_value = kmo_num / kmo_denom
    return kmo_value

print(kmo(newdata[cols].corr().to_numpy()))
 
#开始计算
fa = FactorAnalyzer(n_factors=n_factors,method='principal',rotation="varimax")
fa.fit(newdata[cols])
communalities= fa.get_communalities()#共性因子方差
loadings=fa.loadings_#成分矩阵，可以看出特征的归属因子
 
#画图
plt.figure(figsize=(9,6),dpi=800)
ax = sns.heatmap(loadings, annot=True, cmap="BuPu")
ax.set_xticklabels(['基础教育','职业教育','高等教育'],rotation=0)
ax.set_yticklabels(cols,rotation=0)
plt.title('Factor Analysis')
plt.savefig("热力图.png",bbox_inches = 'tight')
plt.show()
 
factor_variance = fa.get_factor_variance()#贡献率
fa_score = fa.transform(newdata[cols])#因子得分
 
#综合得分
complex_score=np.zeros([fa_score.shape[0],])
for i in range(n_factors):
    complex_score+=fa_score[:,i]*factor_variance[1][i]#综合得分s