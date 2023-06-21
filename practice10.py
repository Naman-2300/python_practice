list = []

user_input = int(input("number please: "))
list.append(user_input)

while(user_input!=1):
    if user_input%2==0:
        user_input = user_input//2
        list.append(user_input)
    elif user_input%2!=0:
        user_input = user_input*3 + 1
        list.append(user_input)
    else:
        print("wrong input")
print(list)
    