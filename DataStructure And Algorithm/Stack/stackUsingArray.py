"""
Stack follows Last in First out  or first in last out 

Time Complexity of each operation in Stack is 
Push, pop, isEmpty, peek all take ---> O(1) 
"""

def createStack():
    stack = []
    return stack

def push(stack,stackValue):
    stack.append(stackValue)
    print(stackValue ,"is pushed to stack")

def isEmpty(stack):
    if(len(stack) == 0):
        return True
    else:
        return False

def pop(stack):
    if (isEmpty(stack)):
        return("stack is empty")
    else:
        stack.pop()

def topOfStack(stack):
    topElement = stack[len(stack)-1]
    return topElement

stack = createStack()
push(stack,20)
push(stack,60)
push(stack,40)
push(stack,10)
print("stack after pushing element-->",stack)
pop(stack)
print("stack after removing one element",stack)
currentTop = topOfStack(stack)
print("current top of stack-->",currentTop)


#Pros: Easy to implement. Memory is saved as pointers are not involved. 
#Cons: It is not dynamic. It doesn’t grow and shrink depending on needs at runtime.
