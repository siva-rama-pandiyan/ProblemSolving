#In this program we will return the second largest element in array
arr = [2,4,98,5,62,3,87,87]

#BruteForce Approach
#TC :- O(nLogn + n)
sorted_arr = sorted(arr)
largest = sorted_arr[len(sorted_arr)-1]
sLargest = -1
n = len(sorted_arr) -2
for i in reversed(range(n+1)):
    if sorted_arr[i] < largest:
        sLargest = sorted_arr[i]
        break
print('Second largest element -->',sLargest)

#Better Approach
#TC :- O(2N)

largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
    else:
        continue
sLargest = -1
for i in arr:
    if i > sLargest and i != largest:
        sLargest = i
    else:
        continue
print('Second largest element -->',sLargest)


#Optimal approach
#TC :- O(N)
def secondLargest(arr):
    largest = arr[0]
    sLargest = -1
    for i in arr:
        if i > largest:
            sLargest = largest
            largest = i
        elif i < largest and i > sLargest:
            sLargest = i
        
    return(sLargest)


# print(secondLargest(arr))
print('Second largest element -->',secondLargest(arr))
