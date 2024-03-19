'''

 
'''

from math import *

def printDivisors (n): 
    i = 1
    while (i * i < n): 
        if (n % i == 0): 
            print(i, end = " ") 
  
        i += 1
  
    for i in range(int(sqrt(n)), 0, -1): 
        if (n % i == 0): 
            print(n // i, end = " ") 
  
print("The divisors of 100 are: ") 
  
printDivisors(100)