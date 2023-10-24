#Dial's Algorithm with Graph
import networkx as nx
import matplotlib.pyplot as plt

#A B C D E F G 
nodes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
edges = [('A','B',270),('A','C',250),('A','D',2000),('B','I',1800),('C','B',0),('D','C',750),('D','E',2700),('E','F',1200),('C','H',290),('C','I',2000),('I','J',2000),('H','I',2500),('H','J',2500),('F','G',7000),('F',
'L',500),('L','G',350),('L','K',10000),('L','M',1500),('K','H',500),('G','H',1300),('K','M',900),('M','N',0),('N','J',2000),('K','J',2200),('J','O',270),('L','Q',400),('Q','R',700),('R','U',550),('R','S',400),('S','U',500),('U','T',270),('S','T',480),('O','T',3200),('Q','P',1000),('Q','M',550),('M','P',450),('P','S',180)]
#[('A', 'D'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'G'), ('F', 'G')]
G = nx.DiGraph()

G.add_nodes_from(nodes_for_adding=nodes)

edgeLabels = {}
for (u,v,w) in edges:
    G.add_edge(u,v,weight=w)
    edgeLabels.setdefault((u,v),w)

shortest_path = nx.shortest_path(G,source='A',target='U')

totalEdgeWeight = 0

for i in range(len(shortest_path)-1):
    (u,v) = (shortest_path[i],shortest_path[i+1])
    for (a,b,w) in edges:
        if (u,v) == (a,b):
            totalEdgeWeight += w

print(f"Total edge weight is: {totalEdgeWeight}")
pos = nx.layout.planar_layout(G)

nx.draw(G,pos,with_labels=True,node_size=10)

nx.draw_networkx(G, pos)

nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, pos,edge_labels=edgeLabels)

plt.show()