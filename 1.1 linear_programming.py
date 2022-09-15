import numpy as np
from scipy.optimize import linprog

c=np.array([-2,-3,5])
Aeq=np.array([[1,1,1]])
beq=np.array([7])
A=np.array([[-2,5,-1],[1,3,1]])
b=np.array([-10,12])
x1,x2,x3=(0,None),(0,None),(0,None)

res=linprog(c,A,b,Aeq,beq,bounds=(x1,x2,x3))
print(res)
