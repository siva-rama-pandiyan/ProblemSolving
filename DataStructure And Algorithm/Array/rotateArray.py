#In this Program we will rotate the array to the right by k steps, where k is non-negative.

arr = [1,2,3,4,5,6]
k =2

def rotateArray(left, right, arr):
    while(left < right):
        arr[left],arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

#Logic:-

#step :- 1 Reverse the Whole array(in-place) [5, 4, 3, 2, 1]
#step :- 2 Reverse the first k element [4, 5, 3, 2, 1]
#step :- 3 Reverse the remaining part of the array [4, 5, 1, 2, 3] 

#Time Complexity :- O(n)
#Space Complexity :- O(1) 
k = k % len(arr)

#Here above we are taking k modules with length of array because in some case our k will be more than length of array

print(rotateArray(0,len(arr)-1,arr))
print(rotateArray(0,k-1,arr))
print(rotateArray(k,len(arr)-1,arr))
