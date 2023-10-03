# Python3 program for implementation
# of Heap Sort
from binarytree import build
# To heapify a subtree rooted with
# node i which is an index in arr[].
# n is size of heap
def heapify(arr, n, i):
	smallest = i # Initialize smallest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

	# If left child is smaller than root
	if l < n and arr[l] < arr[smallest]:
		smallest = l

	# If right child is smaller than
	# smallest so far
	if r < n and arr[r] < arr[smallest]:
		smallest = r

	# If smallest is not root
	if smallest != i:
		(arr[i],
		arr[smallest]) = (arr[smallest],
						arr[i])

		# Recursively heapify the affected
		# sub-tree
		heapify(arr, n, smallest)

# main function to do heap sort
def heapSort(arr, n):
	
	# Build heap (rearrange array)
	for i in range(int(n / 2) - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract an element
	# from heap
	for i in range(n-1, -1, -1):
		
		# Move current root to end #
		arr[0], arr[i] = arr[i], arr[0]

		# call min heapify on the reduced heap
		heapify(arr, i, 0)

# A utility function to print
# array of size n
def printArray(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")
	print()

# Driver Code
if __name__ == '__main__':
	arr = [4, 6, 3, 2, 9]
	n = len(arr)

	heapSort(arr, n)

	print("Sorted array is ")
	c = build(arr)
	print(c)
	print(arr)

# This code is contributed by PranchalK
