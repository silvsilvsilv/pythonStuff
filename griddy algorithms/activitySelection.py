#Activity Selection
def printMaxActivities(s, f):
	n = len(f)
	print("The following activities are selected\nActivities: ",end="")

	# The first activity is always selected
	i = 0
	print(i,end=" ")

	# Consider rest of the activities
	for j in range(n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(j,end=" ")
			i = j

# Driver program to test above function
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
printMaxActivities(start, finish)

# This code is contributed by Nikhil Kumar Singh
