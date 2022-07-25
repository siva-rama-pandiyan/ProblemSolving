def printNumber(i,n):
    if(i>n):
        return
    printNumber(i+1,n)
    print(i)
    
print("Enter the number :")
number = int(input())
printNumber(1, number)