import sys
import os

def calc():
    def add(a,b):
        result = a+b
        return result
    def sub(a,b):
        result = a-b
        return result
    def mul(a,b):
        result = a*b
        return result
    def div(a,b):
        result = a/b
        return result

    a = int(sys.argv[1])
    operation = sys.argv[2]
    b = int(sys.argv[3])

    if operation == "add":
        output = add(a,b)
        print(output)
    elif operation == "sub":
        output = sub(a,b)
        print(output)
    elif operation == "mul":
        output = mul(a,b)
        print(output)
    elif operation =="div":
        output = div(a,b)
        print(output)
    else:
        print("enter valid input")
calc()





