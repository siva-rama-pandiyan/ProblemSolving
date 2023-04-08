#In this program we will move each element by one place left
#Optimal Approach
#TC :- O(n)
#SC :- O(1) for extra space and O(n) for space
arr = [1,2,3,4,5]

temp = arr[0]
for i in range(1,len(arr)):
    arr[i-1] = arr[i]

arr[len(arr) - 1] = temp

print(arr) #[2, 3, 4, 5, 1]