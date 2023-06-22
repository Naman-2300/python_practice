user_input = (input("enter credit card number: "))
r = ""
for i in range(0, 8):
    r = r + "*"
s = user_input[-4::1]
print(r+s)