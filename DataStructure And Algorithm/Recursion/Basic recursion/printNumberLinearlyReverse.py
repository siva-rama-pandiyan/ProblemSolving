def printNumber(n):
    if (n <=0):
        return
    print(n)
    printNumber(n-1)

print("Enter Number :")
number = int(input())
printNumber(number)