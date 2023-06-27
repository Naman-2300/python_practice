class math_operations:
    pass 
def add(a, b):
    print(a+b)
def subtract(a, b):
    print(a - b)
def multiply(a, b):
    print(a * b)
def divide(a, b):
    print(a//b)

a, b = map(int, input("enter the number: ").split())
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

