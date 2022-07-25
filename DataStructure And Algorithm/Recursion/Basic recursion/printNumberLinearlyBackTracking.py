def printNumber(n):
    if (n<1):
        return
    printNumber(n-1)
    print(n)

print("Enter the number :")
number = int(input())
printNumber(number)