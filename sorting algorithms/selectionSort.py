# Selection sort in Python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        print(array)
        print("Minimum element is:",array[min_idx])
        print(array)
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    size = len(data)
    print("Unsorted array:",data)
    selectionSort(data, size)
    print('Sorted Array in Ascending Order:')
    print(data)