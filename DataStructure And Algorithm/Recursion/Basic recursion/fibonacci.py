def fibonacci(n):
    if (n <= 1):
        return n
    last = fibonacci(n-1)
    sLast = fibonacci(n-2)
    return last + sLast

print("Enter the number :")
number = int(input())
result = fibonacci(number)
print("Fibnacci result-->",result)