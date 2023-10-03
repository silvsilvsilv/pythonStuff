#Comb Sort
import math
# To find next gap from current
def getNextGap(gap):

	# Shrink gap by Shrink factor
	gap = math.floor(gap * 10/13)
	if gap < 1:
		return 1
	return gap

# Function to sort arr[] using Comb Sort


def combSort(arr):
    n = len(arr)

    #Initialize gap
    gap = n
    #Initialized as true so that loop runs
    swapped = True

    #Keep running is gap is more than 1 or if swap has occured
    while gap != 1 or swapped == 1:
        #Find next gap
        gap = getNextGap(gap)
        print("\nCurrent gap:", gap) 
        #To check if swap happened or not
        swapped = False

        for i in range(0, n - gap):
            print(f"Comparing {arr[i]} and {arr[i+gap]}")
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            
            print(arr)



# Driver code to test above
if __name__ == "__main__":
    arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
    combSort(arr)

    print ("Sorted array:", arr)
