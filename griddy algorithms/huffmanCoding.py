# A Huffman Tree Node
import heapq

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''

	def __lt__(self, nxt):
		return self.freq < nxt.freq


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):

	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {node.freq} -> {newVal}({len(newVal)}) = {len(newVal)*int(node.freq)}")

def huffmanTree():
	# characters for huffman tree
	# chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'l', 'm', 'n', 'o', 'p', 'r', 's',  't', 'u']

	# frequency of characters
	#a b c d e f g h i l m n o p r s t u
	#freq = [3, 1, 9, 1, 10, 2, 1, 1, 1, 4, 2, 1 ,5,5,1,3,5,2,1]

	# list containing unused nodes
	nodes = []

	charFreqDict = {}

	# * handles userinput
	y = []
	x = str(input("What word? "))

	for i in range(len(x)):
		if x[i] != " ":
			y.append(x[i])
	
	y.sort()
	# //print(y)
	
	charFrequency = 1
	# adds the characters and its frequency into the charFreq dict
	for i in range(1,len(y),1):
		
		# sets char as key and charFrequency as value if not in dict
		if i == 1:
			charFreqDict.setdefault(y[i-1],charFrequency)
		else:
			charFreqDict.setdefault(y[i],charFrequency)

		if y[i] == y[i-1]:
			charFrequency += 1
			charFreqDict[y[i]] = charFrequency 
		elif y[i] != y[i-1]:
			charFrequency = 1
			charFreqDict[y[i]] = charFrequency 
		

	# //print(charFreqDict)

	# converting characters and frequencies
	# into huffman tree nodes
	for x in range(1,len(y),1):
		
		if x == 1:
			heapq.heappush(nodes, node(charFreqDict.get(y[x]), y[x]))
		
		if y[x] != y[x-1]:
			heapq.heappush(nodes, node(charFreqDict.get(y[x]), y[x]))

	while len(nodes) > 1:

		# sort all the nodes in ascending order
		# based on their frequency
		left = heapq.heappop(nodes)
		right = heapq.heappop(nodes)

		# assign directional value to these nodes
		left.huff = 0
		right.huff = 1

		# combine the 2 smallest nodes to create
		# new node as their parent
		newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

		heapq.heappush(nodes, newNode)
	
	print("Huffman Tree\n")
	# Huffman Tree is ready!

	printNodes(nodes[0])

huffmanTree()

