import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n) :

    s = sys.stdin.readline().split()
    if s[0] == '1' :
        stack.append(s[1])
    elif s[0] == '2' :
        if stack : 
            a = stack.pop()
            print(a)
        else :
            print('-1')
    elif s[0] == '3' :
        print(len(stack))
    elif s[0] == '4' :
        if not stack : 
            print('1')
        else :
            print('0')
    elif s[0] == '5' :
        if stack : 
            print(stack[-1])
        else : 
            print('-1')