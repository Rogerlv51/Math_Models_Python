# modelCovid4_v1.py
# Demo01 of mathematical modeling for Covid2019
# SIR model for epidemic diseases.
# Copyright 2021 Youcans, XUPT
# Crated：2021-06-13
# Python小白的数学建模课 @ Youcans

# 1. SEIR 模型，常微分方程组
from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np  # 导入 numpy包
import matplotlib.pyplot as plt  # 导入 matplotlib包

def dySEIR(y, t, lamda, delta, mu):  # SEIR 模型，导数函数
    s, e, i = y  # youcans
    ds_dt = -lamda*s*i  # ds/dt = -lamda*s*i
    de_dt = lamda*s*i - delta*e  # de/dt = lamda*s*i - delta*e
    di_dt = delta*e - mu*i  # di/dt = delta*e - mu*i
    return np.array([ds_dt,de_dt,di_dt])

# 设置模型参数
number = 1e5  # 总人数
lamda = 0.3  # 日接触率, 患病者每天有效接触的易感者的平均人数
delta = 0.03  # 日发病率，每天发病成为患病者的潜伏者占潜伏者总数的比例
mu = 0.06  # 日治愈率, 每天治愈的患病者人数占患病者总数的比例
sigma = lamda / mu  # 传染期接触数
fsig = 1-1/sigma
tEnd = 300  # 预测日期长度
t = np.arange(0.0,tEnd,1)  # (start,stop,step)
i0 = 1e-3  # 患病者比例的初值
e0 = 1e-3  # 潜伏者比例的初值
s0 = 1-i0  # 易感者比例的初值
Y0 = (s0, e0, i0)  # 微分方程组的初值

# odeint 数值解，求解微分方程初值问题
ySEIR = odeint(dySEIR, Y0, t, args=(lamda,delta,mu))  # SEIR 模型

# 输出绘图
print("lamda={}\tmu={}\tsigma={}\t(1-1/sig)={}".format(lamda,mu,sigma,fsig))
plt.title("Comparison among SI, SIS, SIR and SEIR models")
plt.xlabel('t')
plt.axis([0, tEnd, -0.1, 1.1])

plt.plot(t, ySEIR[:,0], '--', color='r', label='s(t)-SEIR')
plt.plot(t, ySEIR[:,1], '-.', color='g', label='e(t)-SEIR')
plt.plot(t, ySEIR[:,2], '-', color='b', label='i(t)-SEIR')
plt.plot(t, 1-ySEIR[:,0]-ySEIR[:,1]-ySEIR[:,2], ':', color='k', label='r(t)-SEIR')
plt.legend(loc='right')  # youcans
plt.show()
