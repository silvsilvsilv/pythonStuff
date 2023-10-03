#Binary Search
def printSub(arr,start,end):
    for i in range(start,end,1):
        print(f"{arr[i]} ")

def binarySearch(arr, toSearch):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
 
        mid = (high + low) // 2
        print(f"Mid is {mid}\narr[{mid}] is {arr[mid]}")
        print(arr)
        # If x is greater, ignore left half
        if arr[mid] < toSearch:
            low = mid + 1
            printSub(arr,low,mid)
        # If x is smaller, ignore right half
        elif arr[mid] > toSearch:
            high = mid - 1
            printSub(arr,mid,high)
        # means x is present at mid
        else:
            print(f"Element is present at index {mid}")
            return mid
 
    # If we reach here, then the element was not present
    print("Element is not present in the array")
    return -1
 
 
# Test array
if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    
    # Function call
    binarySearch(arr,x)