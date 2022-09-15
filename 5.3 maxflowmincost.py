
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()#有向图
G.add_edges_from([('s','v1',{'capacity': 8, 'weight': 2}),
                  ('s','v3',{'capacity': 7, 'weight': 8}),
                  ('v1','v3',{'capacity': 5, 'weight': 5}),
                  ('v1','v2',{'capacity': 9, 'weight': 2}),
                  ('v3','v4',{'capacity': 9, 'weight': 3}),
                  ('v2','v3',{'capacity': 2, 'weight': 1}),
                  ('v4','t',{'capacity': 10, 'weight': 7}),
                  ('v2','t',{'capacity': 5, 'weight': 6}),
                  ('v4','v2',{'capacity': 6, 'weight': 4})])#图构造

pos=nx.spring_layout(G)#力导向布局算法默认分配的位置
pos['t'][0]=1;pos['t'][1]=0
pos['s'][0]=-1;pos['s'][1]=0
pos['v1'][0]=-0.33;pos['v1'][1]=1
pos['v3'][0]=-0.33;pos['v3'][1]=-1
pos['v2'][0]=0.33;pos['v2'][1]=1
pos['v4'][0]=0.33;pos['v4'][1]=-1
#pos=nx.spring_layout(G,None,pos={'s': [-1,0],'t': [1,0]},fixed=['s','t'])#初始化时可选定一些节点的初始位置/固定节点

#显示graph
edge_label1 = nx.get_edge_attributes(G,'capacity')
edge_label2 = nx.get_edge_attributes(G,'weight')
edge_label={}
for i in edge_label1.keys():
    edge_label[i]=f'({edge_label1[i]:},{edge_label2[i]:})'
#处理边上显示的(容量，单位价格)

nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edges(G,pos)
#nx.draw_networkx_edge_labels(G, pos,edge_label,font_size=15)#显示原图像


mincostFlow = nx.max_flow_min_cost(G, 's', 't')#最小费用最大流
mincost = nx.cost_of_flow(G, mincostFlow)#最小费用的值


for i in mincostFlow.keys():
    for j in mincostFlow[i].keys():
        edge_label[(i,j)]+=',F='+str(mincostFlow[i][j])
#取出每条边流量信息存入边显示值

nx.draw_networkx_edge_labels(G, pos,edge_label,font_size=12)#显示流量及原图
print(mincostFlow)#输出流信息
print(mincost)

plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()
