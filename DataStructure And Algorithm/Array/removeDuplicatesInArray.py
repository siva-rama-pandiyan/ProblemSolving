#In this Program we will remove the duplicates from array in place.
arr =[1,1,2,3,4,2,4]

#Brute force approace
#TC :- O(nLogN)
uniqueSet = set()

for i in arr:
    uniqueSet.add(i)

index = 0

for j in uniqueSet:
    arr[index] = j
    index +=1

print(index, arr) #4 [1, 2, 3, 4, 4, 2, 4]
#Optimal approach:-(Two pointer)
#Tc :-  O(n)
arr =[1,1,2,2,3,4,4]

i = 0
for j in range(1, len(arr)):
    if arr[i] != arr[j]:
        arr[i+1] = arr[j]
        i += 1

print(i+1, arr) #4 [1, 2, 3, 4, 4, 2, 4]
