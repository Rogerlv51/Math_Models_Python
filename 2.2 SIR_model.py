# modelCovid3_v1.py
# Demo01 of mathematical modeling for Covid2019
# SIR model for epidemic diseases.
# Copyright 2021 Youcans, XUPT
# Crated：2021-06-12
# Python小白的数学建模课 @ Youcans

# 1. SIR 模型，常微分方程组
from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np  # 导入 numpy包
import matplotlib.pyplot as plt  # 导入 matplotlib包


def dySIR(y, t, lamda, mu):  # SIR 模型，导数函数
    i, s = y
    di_dt = lamda*s*i - mu*i  # di/dt = lamda*s*i-mu*i
    ds_dt = -lamda*s*i  # ds/dt = -lamda*s*i
    return np.array([di_dt,ds_dt])

# 设置模型参数
number = 1e7  # 总人数
lamda = 0.2  # 日接触率, 患病者每天有效接触的易感者的平均人数
sigma = 2.5  # 传染期接触数
mu = lamda/sigma  # 日治愈率, 每天被治愈的患病者人数占患病者总数的比例
fsig = 1-1/sigma
tEnd = 200  # 预测日期长度
t = np.arange(0.0,tEnd,1)  # (start,stop,step)
i0 = 1e-6  # 患病者比例的初值
s0 = 1-i0  # 易感者比例的初值
Y0 = (i0, s0)  # 微分方程组的初值

print("lamda={}\tmu={}\tsigma={}\t(1-1/sig)={}".format(lamda,mu,sigma,fsig))

ySIR = odeint(dySIR, Y0, t, args=(lamda,mu))  # SIR 模型

# 绘图
#plt.title("Comparison among SI, SIS and SIR models")
plt.xlabel('t')
plt.axis([0, tEnd, -0.1, 1.1])
plt.axhline(y=0,ls="--",c='c')  # 添加水平直线
plt.plot(t, ySIR[:,0], '-r', label='i(t)-SIR')
plt.plot(t, ySIR[:,1], '-b', label='s(t)-SIR')
plt.plot(t, 1-ySIR[:,0]-ySIR[:,1], '-m', label='r(t)-SIR')
plt.legend(loc='best')  # youcans
plt.show()
