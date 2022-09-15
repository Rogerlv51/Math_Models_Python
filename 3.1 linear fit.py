import statsmodels.api as sm
import numpy as np
x1=np.random.normal(0,1,1000)
x2=np.random.normal(0,1.5,1000)
x3=np.random.normal(0,2,1000)
eps=np.random.normal(0,0.3,1000)
c=np.array([1,2,3])
x=np.c_[x1,x2,x3]
y=x.dot(c)+eps
x_model=sm.add_constant(x)
model=sm.OLS(y,x_model)
results=model.fit()
print(results.summary())