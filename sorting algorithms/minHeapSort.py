#Min Heap Sort
import binarytree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value <= root.value:  # Handle duplicates by appending to the right subtree
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root, arr):
    if root:
        in_order_traversal(root.left, arr)
        arr.append(root.value)
        in_order_traversal(root.right, arr)

def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        smallest = l
    if r < n and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr

def minHeapSort(arr):
    # Build a Binary Search Tree (BST) and display it
    root = None
    for value in arr:
        root = insert(root, value)
        in_order_list = []
        in_order_traversal(root, in_order_list)
        # print("BST after inserting", value, ":")
        print(binarytree.build(in_order_list))

    # Convert the sorted array into a min heap
    min_heap = build_min_heap(arr)
    print("Min Heap:", min_heap)

    # Display the min heap as a binary tree
    tree = binarytree.build(list(min_heap))  # Convert the min_heap list to match binarytree's input format
    print("Min Heap as a binary tree:")
    print(tree)

if __name__ == '__main__':
    # Input from the user
    input_string = input("Enter space-separated numbers: ")
    arr = list(map(int, input_string.split()))

    print("Input array:", arr)

    # Build a Binary Search Tree (BST) and display it
    root = None
    for value in arr:
        root = insert(root, value)
        in_order_list = []
        in_order_traversal(root, in_order_list)
        # print("BST after inserting", value, ":")
        print(binarytree.build(in_order_list))

    # Convert the sorted array into a min heap
    min_heap = build_min_heap(arr)
    print("Min Heap:", min_heap)

    # Display the min heap as a binary tree
    tree = binarytree.build(list(min_heap))  # Convert the min_heap list to match binarytree's input format
    print("Min Heap as a binary tree:")
    print(tree)
