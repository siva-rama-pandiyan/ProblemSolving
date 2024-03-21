'''
steps:-
    -find number of digits n from given digit
    -calculate each number to the power of n and sum all of it 
    -if it is same to the given digit means it is armstrong number
'''

def numberOfDigits(num):
    count =0
    while(num > 0):
        count+=1
        num = num//10
    return count

def isArmStrongNumber(number):
    n = numberOfDigits(number)
    total = 0 
    temp = number
    while(temp > 0):
        digit = temp%10
        print('digit->',digit)
        print('total->',total)
        print('pow(digit, n)->',pow(digit, n))
        total = total + pow(digit, n)
        temp = temp//10
    print(number, total)
    if(total == number):
        print(number,'is armstrong number')
    else:
        print(number, 'is not armstrong number')
    
isArmStrongNumber(1634) 
#1634 is armstrong number