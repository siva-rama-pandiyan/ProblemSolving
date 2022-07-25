def printName(i,n):
    if(i > n):
        return
    print("Siva","-->",i,"times")
    printName(i+1, n)

print("Please enter the number :")
input = int(input())
printName(1,input)
