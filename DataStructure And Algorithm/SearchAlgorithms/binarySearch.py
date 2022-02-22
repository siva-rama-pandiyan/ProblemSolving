
"""
Binary Search is a searching algorithm for finding an element's position in a sorted array.

In this approach, the element is always searched in the middle of a portion of an array.

Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.

Binary search can be implemented by using 

1 --> Iterative method

2 --> Recursive Method

Algorithm --> 
    - set two pointers low and high at lowest and highest positions respectively
    - find the middle of the array
    - if mid == searching element(x) means return the mid
    - if x < mid. compare x with middle element of left side of middle (high = mid - 1)
    - if x > mid. compare x with middle element of right side of middle(low = mid + 1)
    - repeat the steps 3 to 6 until low meets high
"""

# Iterative method:-

def binarySearchIterative(arr,x,low,high):
    while(low <= high):
        mid = (low + (high - low)// 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

# Recursive method:- 

def binarySearchRecursive(arr, x, low, high):
    if low > high:
        return -1
    else:
        mid = (low + (high - low)// 2)
        if arr[mid] == x:
            return mid
        elif(arr[mid] < x):
            return binarySearchRecursive(arr, x, mid+1, high)
        else:
            return binarySearchRecursive(arr, x, low, mid-1)

arr = [3, 5, 9, 10, 66, 88]
x = 17
low = 0
high = len(arr)
print("Iterative result-->",binarySearchIterative(arr, x, low, high))
print("Recursive result-->",binarySearchRecursive(arr, x, low, high))


"""

Time Complexity:- 
---> Best case O(1)
---> Worst case O(log n)
---> Average Case O(log n)

"""
