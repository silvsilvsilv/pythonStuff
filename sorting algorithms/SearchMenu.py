#Search Menu
import linearSearch, binarySearch, jumpSearch, interpolationSearch, ternarySearch, exponentialSearch

arr = []
n = int(input("Enter number of elements: "))

for i in range(0,n):
    ele = int(input())
    arr.append(ele)

i = True
j = False

def printMenu():
    print("\n[1] Linear Search\n[2] Binary Search\n[3] Jump Search\n[4] Interpolation Search\n[5] Ternary Search\n[6] Exponential Search\n")

while i:
    arr.sort()
    print("Array to search: ",arr)    
    toSearch = int(input("What element to search? "))
    printMenu()
    user = int(input("What search? "))

    match user:
        case 1:
            linearSearch.linearSearch(arr,toSearch)
            j = False
        case 2:
            binarySearch.binarySearch(arr,toSearch)
            j = False
        case 3:
            jumpSearch.jumpSearch(arr,toSearch)
            j = False
        case 4:
            interpolationSearch.interpolationSearch(arr,toSearch)
            j = False
        case 5:
            ternarySearch.ternarySearch(0,n-1,toSearch,arr)
            j = False
        case 6:
            exponentialSearch.exponentialSearch(arr,toSearch)
            j = False
        case default:
            print("Invalid! Try again")
            j = True  
    
    if j == 0:
        tryAgain = str(input("Do you want to search again? Y/N "))

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