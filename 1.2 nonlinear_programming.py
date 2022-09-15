# 使用scipy编程
'''
from scipy.optimize import minimize
import numpy as np

x0=np.array([100,200,400])
res=minimize(func,x0,method='L-BFGS-B',constraints=cons,bounds=(b1,b2,b3))
print(res)
'''
from sko.GA import GA
def func(x):
    return 10.5+0.3*x[0]+0.32*x[1]+0.32*x[2]+0.0007*x[0]**2+0.0004*x[1]**2+0.00045*x[2]**2
cons=lambda x: x[0]+x[1]+x[2]-700
b1,b2,b3=(100,200),(120,250),(150,300)
ga=GA(func=func,n_dim=3,size_pop=500,max_iter=500,constraint_eq=[cons],lb=[100,120,150],ub=[200,250,300])
best_x,best_y=ga.run()
print("best x:\n",best_x,"\nbest_y:\n",best_y)
