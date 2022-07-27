#normal for loop approach
def reverseUsingForLoop(arr,low, high):
    for i in range(low, high):
        if (low>=high):
            break
        arr[low],arr[high] = arr[high], arr[low]
        low +=1
        high -=1
    return arr
    
#using two pointer approach
def reverseUsingRecursion(arr,low,high):
    if low>=high:
        return arr
    arr[low],arr[high] = arr[high], arr[low]
    low+=1
    high -=1
    return reverseUsingRecursion(arr,low, high)

def reverseArray(arr,low, n):
    if ( low >= n//2):
        return 
    arr[low], arr[n-low-1] = arr[n-low-1], arr[low]
    reverseArray(arr,low+1, n)

arr = [1,2,3,4,5]
arr1= [10,11,12,13,14]
arr2 = [110,109,108,107,106]
low = 0
high = len(arr)
reverseArray(arr,low, high)
forLoopResult = reverseUsingForLoop(arr1, 0, len(arr1)-1)
recursionResult = reverseUsingRecursion(arr2, 0, len(arr2)-1)

print("Reverse Array-->", arr)
print("using normal function-->", arr1)
print("using recursion with two pointer-->", arr2)
    
    
    