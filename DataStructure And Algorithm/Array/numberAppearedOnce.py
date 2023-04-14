#In this program we will find the number which appeared once 
#[1,1,2,2,3,4,4,5,5] O/p:- 2

#Bruteforce approach:-
#TC :- O(n2) nsquare
#SC :- O(1)
arr = [1,1,2,2,3,4,4,5,5]

for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count +=1
        
    if count == 1:
        print(i)
        break

#Better Approach:-
#TC:- O(3N)
#SC :- O(n)

arr = [1,1,2,2,3,4,4,5,5]
maxi = arr[0]
for i in arr:
    maxi = max(i, maxi)
unique_arr = []
for j in range(0, maxi+1):
    unique_arr.append(0)

for k in arr:
    unique_arr[k] +=1

print(unique_arr)

for l in range(0, len(unique_arr)):
    if unique_arr[l] == 1:
        print(l)
        break


#Optimal approach 
#Tc:- O(n)
#SC:- O(1)
arr = [1,1,2,2,3,4,4,5,5]

xor = 0
for i in arr:
    xor = i^xor
    print(xor)
print(xor)