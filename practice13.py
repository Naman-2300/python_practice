user_input = str(input("enter a string: "))
sum = 0

for k in user_input:
    if k!="a" and k!="e" and k!="i" and k!="o" and k!="u":
        continue
    elif k=="a":
        sum = sum + 4
    elif k=="e":
        sum = sum + 3
    elif k=="i":
        sum = sum + 1
    elif k=="o":
        sum = sum + 0
    elif k=="u":
        sum = sum + 0
print(sum)
    