def printNumber(i,n):
    if (i>n):
        return
    print(i)
    printNumber(i+1, n)

print("Enter Number :")
number = int(input())
printNumber(1, number)