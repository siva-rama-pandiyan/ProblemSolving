'''
Facts about Prime number:-
-2 is the only even prime number
-Every prime number can be represented in form of 6n + 1 or 6n – 1 except the prime numbers 2 and 3, where n is any natural number.

steps:-

Naive solution:-
	- Start loop from 1 to n 
	- number% i == 0 means increase count
	- if count =2 means it is prime number 
TC:- o(n)

Optimal solution:-
	-Same but take sqrt of number and loop up to that.	
	-number % i ==0  means then increase count and also check the another factor of it by number//i and it should not be equal to the i.
	- if it not increase count by 1

TC:- O(sqrt(n))
'''
from math import sqrt

def isPrime(number):
    count = 0
    for i in range(1, int(sqrt(number))+1):
        if(number% i == 0):
            count+=1
            if(number//i != i):
                count+=1
    if(count == 2):
        return True
    else:
        return False
    
result = isPrime(36)

print('result-->',result) //False