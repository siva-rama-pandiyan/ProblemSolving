#In this program we will return the largest element in array

arr = [2,3,1,5,10,4]

#Brute force approach
#Time complexity :- o(nLogn)

sorted_arr = sorted(arr)
print('Largest element in array is -->',sorted_arr[len(arr) - 1])


#Optimal approach
#Time complexity :- o(n)

largest_element = arr[0]
for i in arr:
    if i > largest_element:
        largest_element = i
    else:
        continue

print('Largest element in array is -->',largest_element)
