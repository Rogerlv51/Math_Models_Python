import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=5)
G.add_edge('A', 'D', weight=6)
G.add_edge('C', 'F', weight=7)
G.add_edge('A', 'G', weight=1)
G.add_edge('H', 'B', weight=2)
pos = nx.spring_layout(G) 

# 生成邻接矩阵
mat = nx.to_numpy_matrix(G)
print(mat)


# 计算两点间的最短路
# dijkstra_path
path=nx.dijkstra_path(G, source='H', target='F')
print('节点H到F的路径：', path)
distance=nx.dijkstra_path_length(G, source='H', target='F')
print('节点H到F的最短距离为：', distance)

# 一点到所有点的最短路
p=nx.shortest_path(G,source='H') # target not specified
d=nx.shortest_path_length(G,source='H')
for node in G.nodes():
    print("H 到",node,"的最短路径为:",p[node],end='\t')
    print("H 到",node,"的最短距离为:",d[node])
    
# 所有点到一点的最短距离
p=nx.shortest_path(G,target='H') # target not specified
d=nx.shortest_path_length(G,target='H')
for node in G.nodes():
    print(node,"到 H 的最短路径为:",p[node],end='\t')
    print(node,"到 H 的最短距离为:",d[node])
# 任意两点间的最短距离
p=nx.shortest_path_length(G)
p=dict(p)
d=nx.shortest_path_length(G)
d=dict(d)
# for node1 in G.nodes():
#     for node2 in G.nodes():
#         print(node1,"到",node2,"的最短距离为:",d[node1][node2])

# 最小生成树
T=nx.minimum_spanning_tree(G) # 边有权重
print(sorted(T.edges(data=True)))

mst=nx.minimum_spanning_edges(G,data=False) # a generator of MST edges
edgelist=list(mst) # make a list of the edges
print(sorted(edgelist))

# 使用A *算法的最短路径和路径长度
p=nx.astar_path(G, source='H', target='F')
print('节点H到F的路径：', path)
print('节点H到F的路径：', p)
#print('节点H到F的路径：', p1)
d=nx.astar_path_length(G, source='H', target='F')
print('节点H到F的距离为：', distance)
