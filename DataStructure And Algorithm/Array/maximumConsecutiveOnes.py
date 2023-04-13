#In this program we will return the maximum consecutive 1's 
#[1,1,1,0,1,1,0,1,1] O/p :- 3
#TC:- O(n)

def maximumConsecutiveOne(arr):
    maximum = 0
    count =0
    for i in arr:
        if i == 1:
            count +=1
            maximum = max(maximum,count)
        else:
            count = 0
    return maximum

arr = [1,1,0,1,1,1,0,1,1]
result = maximumConsecutiveOne(arr)
print(result) #3