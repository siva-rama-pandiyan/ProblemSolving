#optimal approach
#TC:- O(n)
#SC :- O(1)

def missingNumber(nums):
        n = len(nums)
        total = (n *(n+1))//2
        missing = total - sum(nums)
        return missing
        
def missingNumberWithXor(nums):
        xor2 = 0
        xor1 = 0
        for i in range(0, len(nums)-1):
                xor2 = xor2^nums[i]
                xor1 = xor1^i+1
        return(xor1^xor2)
arr=[1,2,3,4,5,0,7]
result = missingNumber(arr)
xor_result = missingNumberWithXor(arr)
print(result) # 6
print(xor_result) #6