import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes and edges
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2, 5), (1, 3, 2), (2, 3, 4), (2, 4, 8), (2, 5, 6), (3, 5, 7)]

# Create a graph and add nodes and edges
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Initialize the MST
MST = nx.Graph()
MST.add_nodes_from(nodes)

# Boruvka's algorithm
while len(MST.nodes) < len(G.nodes):
    # Find the cheapest edge for each component
    cheapest_edges = {}
    for node in MST.nodes:
        for neighbor in G.neighbors(node):
            if neighbor not in MST.nodes:
                edge_data = G.get_edge_data(node, neighbor)
                edge_weight = edge_data["weight"]
                if node not in cheapest_edges or cheapest_edges[node][2] > edge_weight:
                    cheapest_edges[node] = (node, neighbor, edge_weight)

    # Add the cheapest edges to the MST
    for node, (u, v, w) in cheapest_edges.items():
        MST.add_edge(u, v, weight=w)

# Find the shortest path between nodes 1 and 5
shortest_path = nx.shortest_path(G, source=1, target=5, weight='weight')

# Draw the original graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Draw the MST on top of the original graph
nx.draw_networkx_edges(MST, pos, edge_color='r', width=2)

# Draw the shortest path in green   
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='g', width=2)

# Draw edge labels
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
print(edge_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()