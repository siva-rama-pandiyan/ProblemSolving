"""
A^B for large number

Steps

2^13 having 13 digit
1000^ 1000 have more digits

1^ any = 1
2^1 = 2 , 2^2 = 4, 2^3 = 8, 2^4 = 16, 2^5 = 32, 2^6 = 64, 2^7 = 128, 2^8 = 256


2^1 --> 2^5 --> 2^9
2^2 --> 2^6 --> 2^10
2^3 --> 2^7 --> 2^11
2^4 --> 2^8 --> 2^12

Last digit repeating after every 4 times

Same for all the further numbers like 3,4,5,6...

eg:- a=3 b=10

-Take modules of 10 with four and it will return the remaining.
-In case the value of b is multiple of means modulus will be 0 then take the power value as 4
-with that number do power calulation with a
-At last find the last digit by doing modulas with 10
-It will be the answer

Edge case 
-length of a and b is 1 and its value is 0 means answer is 0. 0^0 = 1
-a value is zero means answer is 0.Any power value to number 0 means its value is 0. 0^3 = 0
-b value is zero means answer is 1. any number to power of 0 means its value is 1. 1^0 = 1

Python Program:-
"""
def getLastDigit(self, a, b):
    if(len(a)==1 and a[0]=='0' and len(b)==1 and b[0]=='0'):
        return 1
    elif(len(a)==1 and a[0]=='0'):
        return 0
    elif(len(b)==1 and b[0]=='0'):
        return 1
    
    numA= int(a)
    numB = int(b)
    remaining = 0
    
    if(numB%4 == 0):
        remaining = 4
    else:
        remaining = numB % 4
    power = pow(numA, remaining)
    answer  = abs(power)%10
    return answer
