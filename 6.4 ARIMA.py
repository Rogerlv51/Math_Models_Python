import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from statsmodels.api import tsa
import matplotlib.pyplot as plt
df=pd.read_csv("Bitcoin.csv")
y=np.array(df.Bitcoin)[1000:1168]
x=np.arange(168)
#原图像

plt.xlabel('time')
plt.ylabel('Bitcoin')
plt.title('Bitcoin')
plt.plot(x,y)
plt.show()

from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
lag_acf = acf(y, nlags=20)
lag_pacf = pacf(y, nlags=20, method='ols')
#fig, axes = plt.subplots(1,2, figsize=(20,5))
plot_acf(x, lags=100)
plt.show()
plot_pacf(x, lags=100)
plt.show()
#自相关和偏相关图，虽然我也不知道有何卵用
cat=tsa.arma_order_select_ic(y,max_ar=6,max_ma=4,ic='aic')['aic_min_order']  # AIC定阶
#原图像在3.x附近波动说明用ARMA模型适合一点
md=tsa.ARMA(y,cat).fit()
print(md.summary())
yhat=md.predict()
err=np.sqrt(((y-yhat)**2).mean())
print(cat)
print(err)
y=y[1:]
yhat=yhat[1:]
x=x[1:]
#画图比较
plt.xlabel('time')
plt.ylabel('Bitcoin')
plt.title('Bitcoin')
plt.plot(x,y,'r-',x,yhat,'b-')
plt.legend(('real data','predict data'))
plt.show()
#残差分析
residuals=pd.DataFrame(md.resid)
residuals.plot(title="residuals")
plt.show()
residuals.plot(kind='kde',title="density")
plt.show()
#预测值
x_predict=np.arange(168,193)
dnext=md.predict(168,192)
plt.plot(x_predict,dnext)
plt.xlabel('time')
plt.ylabel('Bitcoin')
plt.title('Bitcoin')
plt.show()