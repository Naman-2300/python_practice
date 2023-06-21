c = 0
# number_of_guests = input()
number_of_guests = int(input("number of guest: "))
for i in range (0, number_of_guests):
        age = int(input("age please: "))
        if (age<2):
         c += 0
        elif (age>2 and age<=12):
         c += 14
        elif (age>=65):
         c += 18
        else:
         c += 23
print("--------------------------------------")
print("----welcome to the billing system-----")
print("                                      ")
print(c)




