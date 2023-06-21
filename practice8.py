import math 

traingle = []
print("Enter the entries: ")
for i in range(0, 3):         
    a =[]
    for j in range(0, 2):     
         a.append(int(input()))
    traingle.append(a)
    
for i in range(0, 3):
    for j in range(0, 2):
        print(traingle[i][j], end = " ")
    print()
d1 = math.sqrt((traingle[0][0] - traingle[1][0])**2 + (traingle[0][1] - traingle[1][1])**2)
d2 = math.sqrt((traingle[1][0] - traingle[2][0])**2 + (traingle[1][1] - traingle[2][1])**2)
d3 = math.sqrt((traingle[0][0] - traingle[2][0])**2 + (traingle[0][1] - traingle[2][1])**2)

print(d1+d2+d3)
    
    