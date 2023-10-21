from collections import Counter, namedtuple
from heapq import heapify, heappop, heappush
import heapq
import networkx as nx
from EoN import hierarchy_pos
from pyvis.network import Network
import matplotlib.pyplot as plt

class Node:
    def __init__(self, count, letter,left=None,right=None):
        self.count = count
        self.letter = letter
        self.left = left
        self.right = right

    def __lt__(self, nxt):
            return self.count < nxt.count


text = "bachelorofscienceincomputersciencecollegeofartsandsciences"
c = Counter(text)
print(c)

# Node = namedtuple('Node', ['count', 'letter', 'left', 'right'])

# left = Node(4, 'a', None, None)
# print(left)
# right = Node(2,'n',None,None)
#print(right)

# count = left.count + right.count
root = Node(None, '\0', None, None)
#print(root)

nodes = [Node(count, letter, None, None) 
         for (letter, count) in c.items()]

# heap = nodes.copy()
# heapify(heap)

def make_tree(heap):
    while len(heap) > 1:
        # Combine the two nodes with the lowest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new node with the combined frequency
        combined_count = left.count + right.count
        new_node = Node(combined_count, '\0',left,right)
        
        # Set the left and right children
        new_node.left = left
        new_node.right = right
        
        # Add the new node back to the heap
        heapq.heappush(heap, new_node)
    
    # The last remaining node in the heap is the root of the Huffman tree
    return heap[0]

tree = make_tree(nodes)

def add_edges(parent, G):
    """Make a NetworkX graph that represents the tree."""
    if parent is None:
        return
    
    for child in (parent.left, parent.right):
        if child:
            G.add_edge(parent, child)
            add_edges(child, G)

# G = nx.DiGraph()
# add_edges(tree, G)

def get_labels(parent, labels):
    if parent is None:
        return
    
    if parent.letter == '\0':
        labels[parent] = parent.count
    else:
        labels[parent] = parent.letter
        
    get_labels(parent.left, labels)
    get_labels(parent.right, labels)

# labels = {}
# get_labels(tree, labels)

def get_edge_labels(parent, edge_labels):
    if parent is None:
        return
    
    if parent.left:
        edge_labels[parent, parent.left] = '0'
        get_edge_labels(parent.left, edge_labels)
        
    if parent.right:
        edge_labels[parent, parent.right] = '1'
        get_edge_labels(parent.right, edge_labels)

# edge_labels = {}
# get_edge_labels(tree, edge_labels)
# print(len(edge_labels))

def draw_tree(tree):
    G = nx.DiGraph()
    add_edges(tree, G)
    pos = hierarchy_pos(G)
    labels = {}
    get_labels(tree, labels)
    edge_labels = {}
    get_edge_labels(tree, edge_labels)
    subax1 = plt.subplot()
    nx.draw(G, pos, labels=labels, alpha=0.4)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='C1')
    plt.show()

draw_tree(tree)