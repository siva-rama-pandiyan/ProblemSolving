"""
1 ---> Create a stack
2 ---> Push to the stack when it is opening bracket 
3 ---> If it is closing bracket means check whether the stack is empty or not if empty means return false
4 ---> If not empty means take the last element and check it with current bracket
5 ---> If both are same means continue else return false
6 ---> If all opening brackets matched with closing bracket means it is balance bracket.
"""

print("Enter the bracket string")
brackets = input()

stack = []
openingBrackets = ["(", "{", "["]
def isEmpty(stack):
        if len(stack) == 0:
            return True
        else:
            return False

for i in brackets:
    if i in openingBrackets:
        stack.append(i)
    else:
        if(isEmpty(stack)):
            print(False)
            break
        else:
            lastIn = stack.pop()
            if lastIn =="(" and i == ")":
                continue
            elif lastIn =="{" and i == "}":
                continue
            elif lastIn =="[" and i == "]":
                continue
            else:
                print(False)
                break
#Below if condition is to check when the test case is full of open brackets means it will help to provide solution
if(isEmpty(stack)):
    print(True)
else:
    print(False)


