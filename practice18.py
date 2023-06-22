user_input = list(map(int, input("enter any 9 numbers from 1 to 9").split(" ")))
c=0
for i in range(0, 8):
    if user_input[i]!=i+1:
        c = i+1
        break
print(c)
    