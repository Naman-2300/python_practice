user_input =  str(input("please enter: "))
user_input = user_input[::-1]
k=""
for i in user_input:
    if i=="a":
        k += '0'
        
    elif i=="e":
        k+= '1'

    elif i=="i":
        k += '2'

    elif i=="o":
        k += '2'

    elif i=="u":
        k += '3'

    else:
        k+=i

print(k+"aca")

        
