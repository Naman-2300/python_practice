def numbers(a, b):
    print(a+b)

def string(a, b):
    z = ord(a) + ord(b)
    print(z)
    
n = int(input("select 1 for integer and 2 for string please: "))
if n==1:
    a,b = input("enter the parameters: ").split(" ")
    numbers(a,b)
    
elif n==2:
    a,b = input("enter the parameters: ").split(" ")
    string(a,b)