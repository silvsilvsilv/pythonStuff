#Bucket Sort
def bucketSort(arr):
    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)
    
    # Determine the interval for buckets (e.g., interval of 10)
    interval = 10
    
    # Calculate the number of buckets based on the interval
    num_buckets = ((max_val - min_val) // interval) + 1
    buckets = [[] for _ in range(num_buckets)]
    
    print("Scatter:")
    # Scatter Step: Place each element in the appropriate bucket
    for num in arr:
        index = (num - min_val) // interval
        buckets[index].append(num)
    
    for i in range(num_buckets):
        print(f"Bucket {i*interval} to {(i+1)*interval-1}: {buckets[i]}")
    
    print("\nSort:")
    # Sort Step: Sort each bucket (you can use any sorting algorithm)
    for i in range(num_buckets):
        buckets[i].sort()
        print(f"Bucket {i*interval} to {(i+1)*interval-1}: {buckets[i]}")
    
    print("\nGather:")
    # Gather Step: Concatenate the sorted buckets to get the final sorted array
    sorted_arr = []
    for i, bucket in enumerate(buckets):
        sorted_arr.extend(bucket)
        print(f"Bucket {i*interval} to {(i+1)*interval-1}: {bucket}")
    
    print("Sorted array: ",sorted_arr)

# Example usage:
if __name__ == "__main__":
    arr = [-5, 3, 2, -1, 10, -7, 8, -3]
    bucketSort(arr)

