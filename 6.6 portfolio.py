import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

data=pd.read_csv("C:/Users/马世拓/Desktop/2022MCM/ARIMA预测.csv")
reinf=pd.read_csv("C:/Users/马世拓/Desktop/2022MCM/PPO收益.csv")['value']/1000



a1=0.98
a2=0.99
##### 马科维兹优化
def E(w,t=0):
    return a1*(data['Bitcoin_pre'][t+1]/data['Bitcoin'][t])*w[0]+a2*(data['Gold_pre'][t+1]/data['Gold'][t])*w[1]-1.02*w[0]-1.01*w[1]

def D(w,t=0):
    return data['predict_bitcoin_volatility'][t+1]*w[0]*w[0]+data['predict_gold_volatility'][t+1]*w[1]*w[1]+2*0.645*data['predict_both_volatility'][t+1]*w[0]*w[1]

def func(w,t=0):
    return -E(w,t)+10*D(w,t)




##### 最大夏普优化

def sharp(w,t=0):
    return -((E(w,t)/(w[0]+w[1])-0.04)/np.sqrt(D(w,t)))


##### 风险平价优化

def risk(w,t=0):
    return abs(data['predict_bitcoin_volatility'][t+1]*w[0]*w[0]-data['predict_gold_volatility'][t+1]*w[1]*w[1])/D(w,t)
Er1=[]
Er2=[]
Er3=[]
strategy=[]
for t in range(data.shape[0]-1):
    cons = ({'type': 'ineq',
         'fun': lambda w: E(w,t) + 1},
            {'type': 'ineq',
         'fun': lambda w: -w[0] - w[1] + 1})
    res1 = opt.minimize(func, [0.1, 0.1], args=(t,), bounds=[(0.1,1),(0.1,1)],
               constraints=cons, method='SLSQP', options={'disp': False})
    res2 = opt.minimize(sharp, [0.1, 0.1], args=(t,), bounds=[(0,1),(0,1)],
               constraints=cons, method='SLSQP', options={'disp': False})
    res3 = opt.minimize(risk, [0.1, 0.1], args=(t,), bounds=[(0,1),(0,1)],
               constraints=cons, method='SLSQP', options={'disp': False})
    w1=res1.x
    w2=res2.x
    w3=res3.x
    strategy.append(w3)
    e1=a1*(data['Bitcoin'][t+1]/data['Bitcoin'][t])*w1[0]+a2*(data['Gold'][t+1]/data['Gold'][t])*w1[1]-1.02*w1[0]-1.01*w1[1]
    Er1.append(-e1)
    e2=a1*(data['Bitcoin'][t+1]/data['Bitcoin'][t])*w2[0]+a2*(data['Gold'][t+1]/data['Gold'][t])*w2[1]-1.02*w2[0]-1.01*w2[1]
    Er2.append(-e2)
    e3=a1*(data['Bitcoin'][t+1]/data['Bitcoin'][t])*w3[0]+a2*(data['Gold'][t+1]/data['Gold'][t])*w3[1]-1.02*w3[0]-1.01*w3[1]
    Er3.append(-e3)

ler1=[1]
ler2=[1]
ler3=[1]
for i in range(len(Er1)):
    s1=1
    s2=1
    s3=1
    for j in range(i):
        '''
        s1*=0.998+Er1[j]
        s2*=0.969+Er2[j]
        s3*=0.984+Er3[j]
        '''
        s1*=0.9972+Er1[j]
        s2*=0.9679+Er2[j]
        s3*=0.9829+Er3[j]
        
    ler1.append(s1)
    ler2.append(s2)
    ler3.append(s3)

fig=plt.figure(figsize=(9,6))
plt.plot(ler1)
plt.plot(ler2)
plt.plot(ler3)
plt.plot(reinf)
plt.legend(['Markowitz','MaxSharp','Risk','Reinforcement'])
plt.xlabel("date")
plt.ylabel("cummulated return rate")
plt.show()
#pd.DataFrame(strategy).to_csv("C:/Users/马世拓/Desktop/2022MCM/日贪心投资策略.csv")
#print(e3)
df=pd.DataFrame({'Markowitz':ler1,'MaxSharp':ler2,'Risk':ler3})
df1=pd.DataFrame({'Reinforcement':reinf})
ddf=df.diff().dropna()
ddf1=df1.diff().dropna()
print("平均收益率：")
print(df.mean(),'\n',df1.mean())
print("年化波动率：")
print(df.var()*np.sqrt(252),'\n',df1.var()*np.sqrt(252))
print("平均夏普比率：")
print((df.mean()-0.04)/df.var(),'\n',(df1.mean()-0.04)/df1.var())
print("胜率：")
print(len(ddf[ddf['Markowitz']>0]['Markowitz'])/len(ddf),len(ddf[ddf['MaxSharp']>0]['MaxSharp'])/len(ddf),
        len(ddf[ddf['Risk']>0]['Risk'])/len(ddf),len(ddf1[ddf1['Reinforcement']>0]['Reinforcement'])/len(ddf1))
print("胜负比：")
print(len(ddf[ddf['Markowitz']>0]['Markowitz'])/len(ddf[ddf['Markowitz']<0]['Markowitz']),len(ddf[ddf['MaxSharp']>0]['MaxSharp'])/len(ddf[ddf['MaxSharp']<0]['MaxSharp']),
        len(ddf[ddf['Risk']>0]['Risk'])/len(ddf[ddf['Risk']<0]['Risk']),len(ddf1[ddf1['Reinforcement']>0]['Reinforcement'])/len(ddf1[ddf1['Reinforcement']<0]['Reinforcement']))
print("盈亏比：")
print(sum(ddf[ddf['Markowitz']>0]['Markowitz'])/sum(ddf[ddf['Markowitz']<0]['Markowitz']),sum(ddf[ddf['MaxSharp']>0]['MaxSharp'])/sum(ddf[ddf['MaxSharp']<0]['MaxSharp']),
        sum(ddf[ddf['Risk']>0]['Risk'])/sum(ddf[ddf['Risk']<0]['Risk']),sum(ddf1[ddf1['Reinforcement']>0]['Reinforcement'])/sum(ddf1[ddf1['Reinforcement']<0]['Reinforcement']))

