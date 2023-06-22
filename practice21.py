dict1 ={}
for i in range (0, 4):
    user_input = input("enter the names: ")
    dict1[i] = user_input

print(sorted(dict1.values()))