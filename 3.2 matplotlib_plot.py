import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

movies = {
    "流浪地球":[2.01,4.59,7.99,11.83,16],
    "飞驰人生":[3.19,5.08,6.73,8.10,9.35],
    "疯狂的外星人":[4.07,6.92,9.30,11.29,13.03],
    "新喜剧之王":[2.72,3.79,4.45,4.83,5.11],
    "廉政风云":[0.56,0.74,0.83,0.88,0.92],
    "神探蒲松龄":[0.66,0.95,1.10,1.17,1.23],
    "小猪佩奇过大年":[0.58,0.81,0.94,1.01,1.07],
    "熊出没·原始时代":[1.13,1.96,2.73,3.42,4.05]
}
mdf = pd.DataFrame(movies) 
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(15,5))
# 设置X轴刻度为一个数组(有广播功能)
xticks = np.arange(len(movies)) 
# 设置条形图宽度
bar_width = 0.15

#设置第一天所有影片条形图的位置
plt.bar(xticks-2*bar_width,mdf.iloc[0],width=bar_width,color='pink') # iloc[]取DataFrame的一行
#设置第二天所有影片条形图的位置 
plt.bar(xticks-bar_width,mdf.iloc[1],width=bar_width)
#设置第三天所有影片条形图的位置，默认在[0 1 2 3 4 5 6 7]center处
plt.bar(xticks,mdf.iloc[2],width=bar_width)
#设置第四天所有影片条形图的位置
plt.bar(xticks+bar_width,mdf.iloc[3],width=bar_width)
#设置第五天所有影片条形图的位置
plt.bar(xticks+2*bar_width,mdf.iloc[4],width=bar_width)

# 设置X轴信息
plt.xticks(xticks,mdf.columns,size=15)
#设置Y刻度
plt.yticks(range(0,20,2),["%d"%x for x in range(0,20,2)],size=16)
#设置X,Y轴名字
plt.ylabel('票房/亿',size=20)
plt.xlabel('影片名字',size=20)
plt.legend(['1','2','3','4','5'])
# 设置标题
plt.title("五日票房数据",size=20)
# 只保留图形信息
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# 计算x,y坐标对应的高度值
def fun(x, y):
    return (1-x/2+x**2+y**3) * np.exp(-x**2-y**2)
# 设置个背景色
plt.figure()
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 把x,y数据转换为二维数据（网格化）
X, Y = np.meshgrid(x, y)
# 填充等高线
plt.contourf(X, Y, fun(X, Y))
# 显示图表
plt.show()

