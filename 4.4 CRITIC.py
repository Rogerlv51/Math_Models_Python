# coding=gbk
import pandas as pd
import numpy as np
 
if __name__ == '__main__':
    df = pd.DataFrame([[1, 0.875, 0.625, 0.75, 0.625],
          [0.571, 0.857, 0.714, 0.857, 1],
          [1, 0.4, 0.6, 0.7, 0.6],
          [0.25, 0.75, 0.875, 1, 0.75]])
    std_d=np.std(df,axis=1)
    mean_d=np.mean(df,axis=1)
    cor_d=np.corrcoef(df)
    w_j=(1-cor_d).sum(0) *std_d
    print(w_j)
    w=(mean_d/(1-mean_d)*w_j)/sum(mean_d/(1-mean_d)*w_j)
    print(w)