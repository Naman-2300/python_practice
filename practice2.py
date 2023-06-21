decimal = int(input("number please : "))
s = ""
while(decimal>0):
    c = decimal%2
    decimal = decimal//2
    s = s + str(c)
    
print(s[::-1])

