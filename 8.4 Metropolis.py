from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
# define aim function
def aimFunction(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y
x = [i / 10 for i in range(1000)]
y = [0 for i in range(1000)]
for i in range(1000):
    y[i] = aimFunction(x[i])
plt.plot(x, y)
plt.show()
T = 1000  # initiate temperature
Tmin = 10  # minimum value of terperature
x = np.random.uniform(low=0, high=100)  # initiate x
k = 50  # times of internal circulation
y = 0  # initiate result
t = 0  # time
while T >= Tmin:
    for i in range(k):
        # calculate y
        y = aimFunction(x)
        # generate a new x in the neighboorhood of x by transform function
        xNew = x + np.random.uniform(low=-0.055, high=0.055) * T
        if (0 <= xNew and xNew <= 100):
            yNew = aimFunction(xNew)
            if yNew - y < 0:
                x = xNew
            else:
                # metropolis principle
                p = math.exp(-(yNew - y) / T)
                r = np.random.uniform(low=0, high=1)
                if r < p:
                    x = xNew
    t += 1
    T = 1000 / (1 + t)  #降温函数，也可使用T=0.9T
print(x, aimFunction(x))
