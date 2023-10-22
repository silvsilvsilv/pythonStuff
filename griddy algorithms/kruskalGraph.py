import matplotlib.pyplot as plt
import networkx as nx

nodes = [1,2,3,4,5]
edges = [(1,2,5),(1,3,2),(2,3,4),(2,4,8),(2,5,6),(3,5,7)]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G)

pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)

edgeLabels = {}

for (u,v,w) in edges:
    edgeLabels.setdefault((u,v),w)

nx.draw_networkx_edges(mst,pos,edge_color="r",width=2,label='weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=edgeLabels)

plt.show()