#tournament Sort
from binarytree import build

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
    
def tournamentIterative(arr):
    n = len(arr)
    arrCopy = list(arr)
    stack = []
    
    while not(is_power_of_two(len(arrCopy))):
        arrCopy.append('-inf')

    stack.append(arrCopy)
    print(arrCopy)
    while n > 1:
        unsortedArr = []
        for i in range(0, n, 2):  # Adjusted the range to avoid IndexError
            if (i + 1) < n:  # Check if there's a pair to compare
                if (isinstance(arrCopy[i], str) and isinstance(arrCopy[i + 1], int)):
                    largest = arrCopy[i + 1]
                    unsortedArr.append(largest)
                elif (isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], str)):
                    largest = arrCopy[i]
                    unsortedArr.append(largest)
                elif isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], int):
                    largest = max(arrCopy[i], arrCopy[i + 1])
                    unsortedArr.append(largest)
            else:
                unsortedArr.append(arrCopy[i])  # Handle odd-length lists
        while not(is_power_of_two(len(unsortedArr))):
            unsortedArr.append('-inf')

        stack.append(unsortedArr)
        n = len(unsortedArr)
        arrCopy = list(unsortedArr)

    return stack if stack else arr[0]

def tournamentSort(arr):
    
    arrCopy = list(arr)
    unSorted = []
    sorted = []
    
    x = tournamentIterative(arrCopy)
    x.reverse()

    for i in range(len(x)):
        for j in range(len(x[i])):
            unSorted.append(x[i][j])
    
    largest = unSorted[0]
    iter = 0
    while iter < len(arr):
        
        print(largest)
        tree = build(unSorted)

        print(tree)
        sorted.append(largest)
        iter += 1
    
    ite = 0
    while arrCopy[ite] == largest:
        arrCopy[ite] = '-inf'
        ite+=1
    
    print(arrCopy)
    print(sorted)

def tournaSort(arr):
    
    arrCopy = []
    sorted = []

    for num in arr:
        arrCopy.append(num)
    
    for i in range(len(arrCopy)):
        unSorted = []

        x = tournamentIterative(arrCopy)
        x.reverse()

        for j in range(len(x)):
            for k in range(len(x[j])):
                unSorted.append(x[j][k])
        
        largest = unSorted[0]

        print(largest)
        tree = build(unSorted)

        print(tree)
        sorted.append(largest)

        ite = 0
        while arrCopy[ite] != largest:
            ite += 1
        else:
            arrCopy.remove(largest)
            arrCopy.append('-inf')
            ite = 0

        
    print(sorted)


if __name__ == "__main__":
    arr = [55,2,4,99,25,78,3,48,8,5,100,44,6]
    # arr = [55 ,2 ,4 ,99, 25]

    print("Unsorted arr: ", arr)
    tournaSort(arr)
    