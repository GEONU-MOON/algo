import sys

T = int(sys.stdin.readline())

for i in range(T) :
    str = input()
    stack = []
    for j in str : 
        if j == '(' :
            stack.append('(')
        elif j == ')' :
           if len(stack) == 0 :
               stack.append(')')
               break 
           else : 
               stack.pop()
    
    if len(stack) == 0 :
        print('YES')
    else : 
        print('NO')