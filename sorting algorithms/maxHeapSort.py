#Max Heap Sort
import binarytree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value >= root.value:  # Handle duplicates by appending to the left subtree
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
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr
def maxHeapSort(arr):
    # Build a Binary Search Tree (BST) and display it
    root = None
    for value in arr:
        root = insert(root, value)
        in_order_list = []
        in_order_traversal(root, in_order_list)
        # print("BST after inserting", value, ":")
        print(binarytree.build(in_order_list))

    # Convert the sorted array into a max heap
    max_heap = build_max_heap(arr)
    print("Max Heap:", max_heap)

    # Display the max heap as a binary tree
    tree = binarytree.build(list(max_heap))  # Convert the max_heap list to match binarytree's input format
    print("Max Heap as a binary tree:")
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

    # Convert the sorted array into a max heap
    max_heap = build_max_heap(arr)
    print("Max Heap:", max_heap)

    # Display the max heap as a binary tree
    tree = binarytree.build(list(max_heap))  # Convert the max_heap list to match binarytree's input format
    print("Max Heap as a binary tree:")
    print(tree)
