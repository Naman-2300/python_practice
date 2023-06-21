user_input =  str(input("please enter: "))
j = 1
ans = 0
for i in user_input:
    ans = int(i)**j + ans
    j = j+1
print(ans)
