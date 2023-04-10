arr1 = [1,2,3,4,5,6]
arr2 = [1,2,3,4,5,7]
#op :- [1,2,3,4,5,6,7]

#BruteForce
#Tc:- O(n1 logn + n2 logn) + O(n1 + n2)
#Sc:-  O(n1+n2) + O(n1 + n2)

unique_set = set()
for i in arr1:
    unique_set.add(i)

for j in arr2:
    unique_set.add(j)

union_array = []
for k in unique_set:
    union_array.append(k)
print(union_array) #[1, 2, 3, 4, 5, 6, 7]

#Optimal approach:

arr1 = [1,2,3,4,5,6]
arr2 = [1,2,3,4,5,7]

def unionSortedArray(arr1,arr2):
    n1= len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    union_array = []
    while(i <n1 and j <n2):
        if(arr1[i] <= arr2[j]):
            if(len(union_array)== 0 or union_array[len(union_array) - 1] != arr1[i]):
                union_array.append(arr1[i])
            i+=1
        else:
            if(len(union_array)== 0 or union_array[len(union_array) - 1] != arr2[j]):
                union_array.append(arr2[j])
            i+=1
    while(i<n1):
        if(len(union_array)== 0 or union_array[len(union_array) - 1] != arr1[i]):
                union_array.append(arr1[i])
        i+=1
    while(j<n2):
        if(len(union_array)== 0 or union_array[len(union_array) - 1] != arr2[j]):
                union_array.append(arr2[j])
        i+=1
    return union_array