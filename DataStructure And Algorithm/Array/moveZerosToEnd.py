#In this program we will move the zero's in the array to end

arr=[1,0,8,9,0,2,4,5,6,0,7]
#output :- [1,8,9,2,4,5,6,7,0,0,0]

#Brute forch approach
#Tc:- O(2n)
#SC :- O(n) because of temp extra space

temp = []
for i in arr:
    if i !=0:
        temp.append(i)

for i in range(0, len(temp)):
    arr[i] = temp[i]

for j in range(len(temp), len(arr)):
    arr[j] = 0

print(arr) #[1, 8, 9, 2, 4, 5, 6, 7, 0, 0, 0]

#Optimal solution
#TC:- O(n)
#Sc :- O(1)

#Logic:- 
#Declare variable j find the first position of zero
#Start loop from j+1 to end and if you found non zero element means swap it with j and increment the j position

arr=[1,0,8,9,0,2,4,5,6,0,7]

j = -1
for i in range(0, len(arr)):
    if arr[i] == 0:
        j = i
        break
if (j == -1):
    print(arr)
for k in range(j+1, len(arr)):
    if arr[k] != 0:
        arr[j], arr[k] = arr[k],arr[j]
        j +=1
print(arr)