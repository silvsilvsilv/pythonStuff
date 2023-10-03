def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

def tournamentIterative(arr):
    n = len(arr)
    arrCopy = list(arr)
    stack = []
    
    print(len(arrCopy))
    while not(is_power_of_two(len(arrCopy))):
        arrCopy.append('-inf')

    stack.append(arrCopy)

    while n > 1:
        unsortedArr = []
        for i in range(0, n, 2):  # Adjusted the range to avoid IndexError
            if (i + 1) < n:  # Check if there's a pair to compare
                if (isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], str)):
                    largest = arrCopy[i]
                    unsortedArr.append(largest)
                elif (isinstance(arrCopy[i], str) and isinstance(arrCopy[i + 1], int)):
                    largest = arrCopy[i + 1]
                    unsortedArr.append(largest)
                elif isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], int):
                    largest = max(arrCopy[i], arrCopy[i + 1])
                    unsortedArr.append(largest)
            else:
                unsortedArr.append(arrCopy[i])  # Handle odd-length lists

        stack.append(unsortedArr)
        n = len(unsortedArr)
        arrCopy = list(unsortedArr)

    return stack if stack else arr[0]

# Example usage:
arr = [3, 2, 1, 4, 5]
result = tournamentIterative(arr)
print(result)
