import matplotlib.pyplot as plt
import networkx as nx

nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
edges = [(1,2,55),(1,7,106),(2,3,79),(2,7,104),(3,4,112),(3,5,98),(3,8,110),(4,6,58),(5,6,139),(5,9,131),(5,12,126),(6,12,69),(6,13,140),(6,20,135),(7,8,85),(7,10,101),(7,17,97),(8,9,83),(8,11,70),(8,14,141),(9,12,136),(10,11,105),(11,16,106),(11,17,109),(12,13,109),(12,14,140),(13,15,141),(13,20,138),(14,15,122),(14,16,128),(15,20,102),(16,20,139),(16,18,136),(16,19,141),(17,18,74),(18,19,93)]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G,algorithm="prim")

totalEdgeWeight = 0

for (u,v) in mst.edges:
    for (a,b,w) in edges:
        if(u,v) == (a,b):
            totalEdgeWeight += w

print(f"Total edge weight is: {totalEdgeWeight}") 

pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)

edgeLabels = {}

for (u,v,w) in edges:
    edgeLabels.setdefault((u,v),w)

nx.draw_networkx_edges(mst,pos,edge_color="r",width=2,label='weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=edgeLabels)

plt.show()