import networkx as nx
import matplotlib.pyplot as plt
# 创建空的网格
nf=nx.Graph()
# 添加节点
nf.add_node('JFK')
nf.add_nodes_from(['SFO','LAX','ATL','FLO','DFW','HNL'])
# nf.number_of_nodes()  # 查看节点数，输出结果7

# 添加连线
nf.add_edges_from([('JFK','SFO'),('JFK','LAX'),('LAX','ATL'),('FLO','ATL'),('ATL','JFK'),('FLO','JFK'),('DFW','HNL')])
nf.add_edges_from([('OKC','DFW'),('OGG','DFW'),('OGG','LAX')])
print(nf.number_of_edges()) # 查看连线数，结果输出10

# 绘制网络图
nx.draw(nf,with_labels=True)
plt.show()

print(nx.info(nf))
print(nx.density(nf))
print(nx.diameter(nf))
print(nx.clustering(nf))
print(nx.transitivity(nf))
print(list(nf.neighbors('OGG')))
print(nx.degree_centrality(nf))
print(nx.closeness_centrality(nf))
print(nx.betweenness_centrality(nf))

