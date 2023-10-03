# Bubble sort in Python
def bubbleSort(array):
  print("Unsorted array: ",array)
  # loop to access each array element
  for i in range(len(array)):
    print(array)
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):
      print(f"Comparing {array[j]} and {array[j+1]}")
      print(f"Is {array[j]} > {array[j+1]}? {'Yes' if array[j] > array[j+1] else 'No'}")
      print(f"{'===Swap===' if array[j] > array[j+1] else '===No Swap===' }")
      print(array)
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]

    bubbleSort(data)

    print('Sorted Array in Ascending Order:')
    print(data)