def fact(n):
    if (n == 0):
        return 1
    return n * n-1

print("Enter the number :")
number = int(input())
result = fact(number)
print("Factorial of",number,"is",result)