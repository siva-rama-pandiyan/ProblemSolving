def addNumbers(n):
    if(n == 0):
        return 0
    return n+ addNumbers(n-1)

print("Enter the number :")
number = int(input())
result = addNumbers(number)
print("Total sum :", result)