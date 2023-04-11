arr1 = [1,2,2,3,3,4,5,6,7]
arr2 = [2,3,3,5,6,6,7]

#Brute force approach
#TC:- O(n2) nsquare
#SC :- O(n)
visited = []
answer = []

for i in range(0, len(arr2)):
    visited.append(0)

for j in range(0, len(arr1)):
    for k in range(0, len(arr2)):
        if arr1[j] == arr2[k] and visited[k] == 0:
            answer.append(arr1[j])
            visited[k] = 1
            break
        
print(answer)#[2, 3, 3, 5, 6, 7]

#Optimal Approach:-
#TC:- O(n1+n2)
#SC:- O(1)
answer =[]
i =0 
j = 0
while(i < len(arr1) and j < len(arr2)):
    if(arr1[i] < arr2[j]):
        i+=1
    elif(arr1[i] > arr2[j]):
        j+=1
    if(arr1[i] == arr2[j]):
        answer.append(arr1[i])
        i+=1
        j+=1

print(answer) #[2, 3, 3, 5, 6, 7]

