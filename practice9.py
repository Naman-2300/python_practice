from collections import deque
stack = [] 
s = "like"
st = "dislike"
stack.append(st)
stack.append(s)


if stack.append(s)==stack.pop():
    print("like is off")
elif stack.append(st)==stack.pop():
    print("dislike is off")
elif stack.append(s)!=stack.pop():
    print("like is active")
elif stack.append(st)!=stack.pop():
    print("dislike is active")
    
