# Insertion sort
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        print("Array before pass", step)
        print(array)
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            print("Key is ", key)
            print(array)
            print("\n===Swap===")
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

        if not(array[j] > key):
            print("Key is ", key)
            print(array)
            print("\n===No Swap===")
    
if __name__ == "__main__":
    arr = [2,3,5,4,0,9,1]
    print("Unsorted array: ",arr)
    insertionSort(arr)
    print("Sorted: ", arr)
