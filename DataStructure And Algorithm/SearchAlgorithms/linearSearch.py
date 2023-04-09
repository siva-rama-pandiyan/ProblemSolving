arr = [1,2,6,4,7,5,9]
k = 4
#TC:- O(n)

def linearSearch(arr,k):
    for i in range(0, len(arr)):
        if arr[i] == k:
            return i
    return -1

print(linearSearch(arr, k)) #Op:-3