#Ternary Search
# Function to perform Ternary Search
def ternarySearch(l, r, toSearch, arr):
	while r >= l:
		
		# Find mid1 and mid2
		mid1 = l + (r-l) // 3
		mid2 = r - (r-l) // 3

		# Check if key is at any mid
		if toSearch == arr[mid1]:
			print(f"arr[{arr[mid1]}] == {toSearch}? {'Yes' if arr[mid1] == toSearch else 'No'}\nElement is found at index {mid1}\n{arr}")
			return mid1
		if toSearch == arr[mid2]:
			print(f"arr[{arr[mid2]}] == {toSearch}? {'Yes' if arr[mid2] == toSearch else 'No'}\nElement is found at index {mid2}\n{arr}")
			return mid2

		# Since key is not present at mid,
		# Check in which region it is present
		# Then repeat the search operation in that region
		if toSearch < arr[mid1]:
			# key lies between l and mid1
			print(f"Element to be searched is less than arr[{arr[mid1]}]\n{arr}")
			r = mid1 - 1
		elif toSearch > arr[mid2]:
			# key lies between mid2 and r
			print(f"Element to be searched is greater than arr[{arr[mid2]}]\n{arr}")
			l = mid2 + 1
		else:
			# key lies between mid1 and mid2
			print(f"Element to be searched is in betwee arr[{arr[mid1]}] and arr[{arr[mid2]}]\n{arr}")
			l = mid1 + 1
			r = mid2 - 1

	# key not found
	print("Element not found!")
	return -1

# Driver code
if __name__ == "__main__":
    # Get the list
    # Sort the list if not sorted
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Starting index
    l = 0

    # end element index
    r = 9

    # Checking for 5
    # Key to be searched in the list
    key = 5

    # Search the key using ternary search
    p = ternarySearch(l, r, key, ar)

    # Print the result
    # print("Index of", key, "is", p)

    # Checking for 50
    # Key to be searched in the list
    key = 50

    # Search the key using ternary search
    p = ternarySearch(l, r, key, ar)

    # Print the result
    # print("Index of", key, "is", p)

    # This code has been contributed by Sujal Motagi
