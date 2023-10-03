#Linear Search 
def linearSearch(arr,toSearch):
    
    for i in range(len(arr)):
        print(f"Finding {toSearch} at index {i}\n")
        print(f"Is {arr[i]} == {toSearch}?","Yes" if arr[i] == toSearch else "No")
        print(arr)
        if arr[i] == toSearch:
            print(f"{toSearch} found at index {i}")
            return
    
    print("Search unsuccesful! Element not found")


if __name__ == "__main__":
    arr = [2,34,2,5,6,7]
    toSearch = 7
    linearSearch(arr,toSearch)