#In this program we will move the elements in array left by k places
arr = [1,2,3,4,5,6,7]
arr_left = [1,2,3,4,5,6,7]
arr_right = [1,2,3,4,5,6,7]
k = 2 #[4,5,3,6,7,1,2]


#Bruteforce Approach :-
#TC:- O(n+k)
#SC :- o(K) temp is an extra space

def rotateArrayByLeft(arr, k):
    temp = arr[:k]
    for i in range(k,len(arr)): #o(n)
        arr[i-k] = arr[i]
    temp_index = 0
    for j in range(len(arr)-k, len(arr)): #O(k)
        arr[j] = temp[temp_index]
        temp_index+=1
    print(arr)

rotateArrayByLeft(arr, k)

#Optimal approach:-
#TC :- O(2N)
#sc :- O(1)

#Logic:-

#arr = [1,2,3,4,5,6,7]
#3 4 5 6 7 1 2 left rotation
#6 7 1 2 3 4 5 right rotation


#left rotation Logic  
#2 1 3 4 5 6 7 reverse first k elements
#2 1 7 6 5 4 3 reverse the remaining n elements
#3 4 5 6 7 1 2 reverse the whole array

#Right rotation Logic
#7 6 5 4 3 2 1 reverse whole array 
#6 7 5 4 3 2 1 reverse the first k elements
#6 7 1 2 3 4 5 reverse the remaining n elements

def rotateArray(l,r,arr):
    while(l<=r):
        arr[l],arr[r] = arr[r], arr[l]
        l += 1
        r -=1
    return arr

def rotateArrayByLeft(arr, k):
    rotateArray(0,k-1,arr)
    rotateArray(k,len(arr)-1,arr)
    rotateArray(0,len(arr)-1,arr)
    return arr

def rotateArrayByRight(arr, k):
    rotateArray(0,len(arr)-1,arr)
    rotateArray(0,k-1,arr)
    rotateArray(k,len(arr)-1,arr)
    return arr

leftRotateResult = rotateArrayByLeft(arr_left, k)
rightRotateResult = rotateArrayByRight(arr_right, k)

print(leftRotateResult)
print(rightRotateResult)