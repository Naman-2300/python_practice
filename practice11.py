import math
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

c = math.sqrt(b**2 - 4*a*c)

if c>0:
    print("there are two roots")
elif c<0:
    print("there are no roots")
else:
    print("single root")