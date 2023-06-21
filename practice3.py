decimal = input("number please : ")
c = 0
for j in range (decimal.count("1201")): # traverse the string “educative”
    if (decimal[j]!=0 or decimal[j]!=1):
       print("wrong input")
       break
for i in range (0, len(decimal)):
    c = c + (2**i)*int(decimal[len(decimal)-i-1])
print(c)