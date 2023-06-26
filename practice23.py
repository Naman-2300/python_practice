def logic(a1, b1):
    j=0
    for i in a1:
        if i==b1[j]:
            dict1["black"]+=1
            print(b[j], i)
        elif b1[j] in a1:
            dict1["white"]+=1
            print(b[j], i)
        j+=1
    print(dict1)
while(1):
    b = str(input("Enter the number: "))
    dict1 = {"black": 0, "white": 0}
    a = "1234"
    logic(a, b)

