from pyvis.network import Network

def prim(graph):
    # Initialize a list to keep track of selected vertices and a set to store the selected edges
    selected_vertices = []
    selected_edges = set()

    while len(selected_vertices) < len(graph):
        min_weight = float('inf')
        new_vertex = None
        edge_to_add = None

        for vertex in selected_vertices:
            for neighbor, weight in enumerate(graph[vertex]):
                if neighbor not in selected_vertices and weight >0:
                    if weight < min_weight:
                        min_weight = weight
                        new_vertex = neighbor
                        edge_to_add = (vertex, neighbor, weight)

        selected_vertices.append(new_vertex)
        selected_edges.add(edge_to_add)

    return selected_edges

# Example graph represented as an adjacency matrix
original_graph = [
    [0, 28, 0, 0, 0, 10, 0],
[28, 0, 16, 0, 0, 0, 14],
[0, 16, 0, 12, 0, 0, 0],
[0, 0, 12, 0, 22, 0, 18],
[0, 0, 0, 22, 0, 25, 24],
[10, 0, 0, 0, 25, 0, 0],
[0, 14, 0, 18, 24, 0, 0]
]

# Create a Pyvis graph for the original graph
G_original = Network(directed=False)
for i in range(len(original_graph)):
    G_original.add_node(i, label=str(i), font={'size':60})
    for j in range(i + 1, len(original_graph)):
        weight = original_graph[i][j]
        if weight > 0:              
            G_original.add_node(j, label=str(j), font={'size':60})  # Ensure both nodes exist
            G_original.add_edge(i, j, title=str(weight), label=str(weight), font={'size': 60})

# Set node positions
G_original.barnes_hut()
G_original.show("original_graph.html", notebook=False)

# Perform Prim's algorithm to find the minimum spanning tree
minimum_spanning_tree_edges = prim(original_graph)
print(minimum_spanning_tree_edges)
# Create a Pyvis graph for the minimum spanning tree
G_mst = Network(directed=False)
for edge in minimum_spanning_tree_edges:
    source, target, weight = edge
    G_mst.add_node(source, label=str(source), font={'size':60})
    G_mst.add_node(target, label=str(target), font={'size':60})
    G_mst.add_edge(source, target, title=str(weight), label=str(weight), font={'size':60})

# Set node positions
G_mst.barnes_hut()
G_mst.show("minimum_spanning_tree.html", notebook=False)
