# 1. SI 模型，常微分非常，解析解与数值解的比较
from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np  # 导入 numpy包
import matplotlib.pyplot as plt  # 导入 matplotlib包

def dy_dt(y, t, lamda, mu):  # 定义导数函数 f(y,t)
    dy_dt = lamda*y*(1-y)  # di/dt = lamda*i*(1-i)
    return dy_dt

# 设置模型参数
number = 1e7  # 总人数
lamda = 1.0  # 日接触率, 患病者每天有效接触的易感者的平均人数
mu1 = 0.5  # 日治愈率, 每天被治愈的患病者人数占患病者总数的比例
y0 = i0 = 1e-6  # 患病者比例的初值
tEnd = 50  # 预测日期长度
t = np.arange(0.0,tEnd,1)  # (start,stop,step)

yAnaly = 1/(1+(1/i0-1)*np.exp(-lamda*t))  # 微分方程的解析解
yInteg = odeint(dy_dt, y0, t, args=(lamda,mu1))  # 求解微分方程初值问题
yDeriv = lamda * yInteg *(1-yInteg)

# 绘图
plt.plot(t, yAnaly, '-ob', label='analytic')
plt.plot(t, yInteg, ':.r', label='numerical')
plt.plot(t, yDeriv, '-g', label='dy_dt')
plt.title("Comparison between analytic and numerical solutions")
plt.legend(loc='right')
plt.axis([0, 50, -0.1, 1.1])
plt.show()
