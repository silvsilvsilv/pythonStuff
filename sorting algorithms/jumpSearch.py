#Jump Search
import math
def jumpSearch(arr, toSearch):

	n = len(arr)
	print("N is: ", n)
	#Finding block size to be jumped
	step = math.sqrt(n)
	print(f"Step is {int(step)}\n{arr}")
	#Finding the block where the element is, if element is present
	prev = 0
	while arr[int(min(step,n))-1] < toSearch:
		prev = step
		step += math.sqrt(n)
		print(f"\nStep is {int(step)}\n{arr[int(step)]} == {toSearch}? {'Yes' if arr[int(step)] == toSearch else 'No'}\n{arr}")
		if prev >= n:
			print("Element not found")
			return -1
	
	#Doing a linear search for toSearch in block, begins with prev
	while arr[int(prev)] < toSearch:
		prev += 1
		print(f"\nLinear search\nIs {arr[int(prev)]} == {toSearch}? {'Yes' if arr[int(prev)] == toSearch else 'No'}\n{arr}")
		#If we reached next block or end of array, then element is not present
		if prev == min(step,n):
			print("Element not found")
			return -1
		
	#If element is found
	if arr[int(prev)] == toSearch:
		print(f"Element found at index {int(prev)}")
		return prev
	
	print("Element not found")
	return -1

# Driver code to test function
if __name__ == "__main__":
	arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
	x = 55
	
	# Find the index of 'x' using Jump Search
	index = jumpSearch(arr, x)
	
	# Print the index where 'x' is located
	print("Number" , x, "is at index" ,"%.0f"%index)