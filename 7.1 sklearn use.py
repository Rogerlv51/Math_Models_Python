import numpy as np
import pandas as pd
from sklearn.datasets import load_wine#红酒数据集
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split #训练集训练集分类器
import graphviz #画文字版决策树的模块
import pydotplus #画图片版决策树的模块
from IPython.display import Image #画图片版决策树的模块
wine = load_wine()
print(wine.data)  # 数据
print(wine.target_names)  # 标签名
print(wine.target)  # 标签值
print(wine.feature_names)  # 特证名(列名)
wine_dataframe = pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
print(wine_dataframe)
Xtrain, Xtest, Ytrain,Ytest = train_test_split(wine.data,wine.target,test_size=0.3)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

clf = DecisionTreeClassifier()
clf.fit(Xtrain, Ytrain)
Ypredict=clf.predict(Xtest)
print(classification_report(Ypredict,Ytest))

from sklearn import tree
tree_data = tree.export_graphviz(
    clf
    ,feature_names =wine.feature_names
    ,class_names = wine.feature_names#也可以自己起名
    ,filled = True #填充颜色
    ,rounded = True #决策树边框圆形/方形
)
graph1 = graphviz.Source(tree_data.replace('helvetica','Microsoft YaHei UI'), encoding='utf-8')
graph1.render('./wine_tree')

