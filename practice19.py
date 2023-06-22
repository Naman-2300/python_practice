user_input = int(input("enter the pin: "))
c = len(str(user_input))
if c==4 or c==6:
    print("valid")
else:
    print("invalid")
    