#Exponential Search
def printSub(arr,start,end):
	for i in range(start,end,1):
		print(f"{arr[i]} ")

def exponentialSearch(arr, toSearch):
	n = len(arr)
	if n == 0:
		print("Element is not found")
		return -1

	# Find range for binary search by repeatedly doubling i
	i = 1
	while i < n and arr[i] < toSearch:
		i *= 2

	# Perform binary search on the range [i/2, min(i, n-1)]
	left = i // 2
	right = min(i, n-1)

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == toSearch:
			print(f"arr[{mid}] == {arr[mid]}\n{arr}")
			print(f"Element found at index {mid}")
			return mid
		elif arr[mid] < toSearch:
			print(f"arr[{mid}] is < to {toSearch}")
			left = mid + 1
			printSub(arr,left,mid)
		else:
			print(f"arr[{mid}] is > to {toSearch}")
			right = mid - 1
			printSub(arr,mid,right)

	print("Element is not found")
	return -1

	

# Driver Code
if __name__ == "__main__":
	arr = [2, 3, 4, 10, 40]
	n = len(arr)
	x = 10
	result = exponentialSearch(arr, x)
	
# This code is contributed by Ajay singh
