from pyvis.network import Network
import networkx as nx

nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2, label="20")
nx_graph.add_node(21, size=15, title='couple', group=2, label="20")
nx_graph.add_edge(20, 21, weight=5, label="123", physics=False)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
nt = Network()
# populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('nx.html',notebook=False)