import networkx as nx
import matplotlib.pyplot as plt

nodes = [0,1,2,3,4,5,6,7,8]
edges = [(0,1,4),(1,2,8),(2,3,7),(3,4,9),(4,5,10),(3,5,14),(2,5,4),(5,6,2),(6,7,1),(6,8,6),(7,8,7),(7,1,11),(7,0,8)]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G,algorithm="kruskal")

pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)

edgeLabels = {}

for (u,v,w) in edges:
    edgeLabels.setdefault((u,v),w)

nx.draw_networkx_edges(mst,pos,edge_color="r",width=2,label='weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=edgeLabels)

plt.show()