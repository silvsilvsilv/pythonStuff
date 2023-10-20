from pyvis.network import Network
import networkx as nx
from networkx.algorithms import tree


nt = Network()
G = nx.cycle_graph(4)

mst = nx.minimum_spanning_tree(G)
mst2 = nx.minimum_spanning_edges(G, data=False)

# nt.show_buttons(filter_=['edges'])
# nt.set_options("""
# const options = {
#   "edges": {
#     "color": {
#       "inherit": false,
#       "color": "#FF0303",
#       "highlight": "#00EFFF"    
#     },
#     "selfReferenceSize": null,
#     "selfReference": {
#       "angle": 0.7853981633974483
#     },
#     "smooth": {
#       "forceDirection": "none"
#     }
#   }
# }""")

# nx.draw(G)
# populates the nodes and edges data structures
nt.from_nx(mst)
print(list(mst2))
nt.toggle_physics(False)
nt.toggle_drag_nodes(False)
nt.show('nx.html',notebook=False)

# mst = tree.minimum_spanning_edges(G, algorithm="kruskal")

# nt.from_nx(tree.minimum_spanning_edges(G,data=False))
# nt.show('nx.html',notebook=False)