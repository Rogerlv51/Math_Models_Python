import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

def fun(t, w):
    x = w[0]
    y = w[1]
    return [-x**3-y,-y**3+x]

# 初始条件
y0 = [1,0.5]

yy = solve_ivp(fun, (0,100), y0, method='RK45',t_eval = np.arange(0,100,1) )
t = yy.t
data = yy.y
plt.plot(t, data[0, :])
plt.plot(t, data[1, :])
plt.xlabel("时间s")
plt.show()

