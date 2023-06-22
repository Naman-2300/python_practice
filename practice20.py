user_input = input("enter the number: ")
list1 = []
for i in range(1, len(user_input)+1):
    # user_input[i] = int(i)*int(i)
    c = int(i)*int(i)
    list1.append(c)
print(list1)