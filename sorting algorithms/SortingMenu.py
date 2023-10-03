#Sorting Menu
import insertionSort, mergeSort, quickSort, bubbleSort, shellSort, bucketSort, selectionSort, combSort, radixSort, treesort, minHeapSort, maxHeapSort,tournamentSort

arr = []
n = int(input("Enter number of elements: "))

for i in range(0,n):
    ele = int(input())
    arr.append(ele)

i = True
j = False

def success(arr):
    print("Sorted array: ",arr)
    global j
    j = False

while i:
    print("\n[1] Insertion Sort\n[2] Merge Sort\n[3] Quicksort\n[4] Selection Sort\n[5] Shell Sort\n[6] Bucket Sort\n[7] Bubble Sort\n[8] Comb Sort\n[9] Radix Sort\n[10] Min Heap\n[11] Max Heap\n[12] Tree Sort\n[13] Tournament Sort\n")
    print("Unsorted array:", arr)
    user = int(input("What sort? "))
        
    match user:
        case 1:
            insertionSort.insertionSort(arr)
            success(arr)
        case 2:
            mergeSort.mergeSort(arr)
            success(arr)
        case 3:
            quickSort.quickSort(arr, 0, n - 1)
            success(arr)
        case 4:
            selectionSort.selectionSort(arr,n)
            success(arr)
        case 5:
            shellSort.shellSort(arr,n)
            success(arr)
        case 6:
            bucketSort.bucketSort(arr)
            j = 0
        case 7:
            bubbleSort.bubbleSort(arr)
            success(arr)
        case 8:
            combSort.combSort(arr)
            success(arr)
        case 9:
            radixSort.radixSort(arr)
            success(arr)
        case 10:
            minHeapSort.minHeapSort(arr)
            success(arr)
        case 11:
            maxHeapSort.maxHeapSort(arr)
            success(arr)
        case 12:
            treesort.treeSort(arr)
            print('\n')
            success(arr)
        case 13:
            tournamentSort.tournaSort(arr)
            success(arr)
        case default:
            print("Invalid! Try again")
            j = True   
        
    if not(j):
        tryAgain = str(input("Do you want to sort again? Y/N "))

        match tryAgain:
            case 'Y': 
                i = True
            case 'y':
                i = True
            case 'N':
                i = False
            case 'n':
                i = False
            case default:
                i = False
