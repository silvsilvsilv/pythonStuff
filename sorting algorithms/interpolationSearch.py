#Interpolation Search
def printSub(arr,start,end):
	print('[',end=' ')
	for i in range(start,end,1):
		print(arr[i],end=' ')
	print(']',end='')

def interpolationSearch(arr, toSearch):

	# Find indexes of two corners
	low = 0
	n = len(arr)
	high = (n - 1)

	# Since array is sorted, an element present
	# in array must be in range defined by corner
	while low <= high and toSearch >= arr[low] and toSearch <= arr[high]:
		if low == high:
			if arr[low] == toSearch:
				return low
			return -1

		# Probing the position with keeping
		# uniform distribution in mind.
		pos = int(low + (((float(high - low)/( arr[high] - arr[low])) * (toSearch - arr[low]))))
		print(f"Pos is: {pos}\n{arr}")
		# Condition of target found
		if arr[pos] == toSearch:
			print(f"Element {toSearch} is found at index {pos}\narr[{pos}] == {toSearch}? {'Yes' if arr[pos] == toSearch else 'No'}\n{arr}\n")
			return pos

		# If x is larger, x is in upper part
		if arr[pos] < toSearch:
			print(f"Element to search is greater than arr[{pos}]")
			low = pos + 1
			printSub(arr,low,len(arr))
			print('\n')

		# If x is smaller, x is in lower part
		else:
			print(f"Element to search is less than arr[{pos}]")
			high = pos - 1
			printSub(arr,high,len(arr))
			print('\n')
	print("Element not found")
	return -1

# Main function
if __name__ == "__main__":
	# Array of items on whighch search will
	# be conducted.
	arr = [10, 12, 13, 16, 18, 19, 20, 21,
		22, 23, 24, 33, 35, 42, 47]
	

	x = 18 # Element to be searched
	index = interpolationSearch(arr, x)

	# If element was found
	if index != -1:
		print ("Element found at index",index)
	else:
		print ("Element not found")
