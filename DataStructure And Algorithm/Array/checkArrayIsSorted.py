#In this program we will check whether the array is sorted or not

#Time complexity:- o(N)
arr= [1,2,3,4,5,6,7]
second_arr = [1,2,1,35,5]

def checkSorted(arr):
    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        else:
            return False
    return True

arr_result = checkSorted(arr)
second_arr_result = checkSorted(second_arr)

print(arr_result,second_arr_result) #True False
