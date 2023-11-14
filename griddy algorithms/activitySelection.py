#Activity Selection
def printMaxActivities(node, s, f):

	n = len(f)
	print("The following activities are selected\nActivities: ",end="")

	# The first activity is always selected
	i = 0
	print(nodes[i],end=" ")

	# Consider rest of the activities
	for j in range(n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(nodes[j],end=" ")
			i = j

if __name__ == "__main__":

	# Driver program to test above function
	# nodes = ['a','b','c','d','e','f']
	# start = [1, 3, 0, 5, 8, 5]
	# finish = [2, 4, 6, 7, 9, 9]


	# printMaxActivities(nodes,start, finish)

	nodes = []
	start = []
	finish = []

	n = str(input("Input node names: "))
	x = str(input("Start: "))
	y = str(input("Finish: "))

	x = x.split(',')
	y = y.split(',')
	n = n.split(',')

	start = [int(i) for i in x]
	finish = [int(i) for i in y]
	nodes = [i for i in n]
	

	printMaxActivities(nodes, start,finish)

	
