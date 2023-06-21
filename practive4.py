import random

n=int(input("Enter the no teams: "))

#win -2 loss 0 draw 1
list1= ['w','l','d']
list2=[]
list2.append(random.choice(list1))

print(list1,list2)

dict1={'t1':0,'t2':0, 't3':0, 't4':0,'t5':0}
teams=['t1','t2','t3','t4','t5']
for i in teams:
    for j in range(1,len(teams)):
        if(i!=teams[j] and teams[j]>i):
            print(i + "vs"+ teams[j])
            res=str(input("Result as t?: "))
            if res in teams:
                dict1[res]+=2
            if (res=='D'):
                dict1[i]+=1
                dict1[teams[j]]+=1
print(dict1)

#print(sorted(dict1.keys(),reverse=True))

sorted_dict = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_dict)

print(converted_dict)
list1=[]
for keys in converted_dict:
    list1.append(keys)

print(list1)

ele=list1.pop()
print (list1)

q1=str(input(list1[0] + "vs" + list1[1] + ":"))
q2=str(input(list1[2] + "vs" + list1[3] + ":"))


print(q1+ " in Finals!")
print(q2+ " in Finals!")

f=str(input(q1 +" vs " +q2 + ": "))

print(f)



