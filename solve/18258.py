from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

s = deque()

for i in range(n) :
    input_str = input().split()
    if input_str[0] == 'push' :
        s.append(input_str[1])
    elif input_str[0] == 'pop' :
        if not s :
            print('-1')
        else : print(s.popleft())
    elif input_str[0] == 'size' :
        print(int(len(s)))
    elif input_str[0] == 'empty' :
        if not s : 
            print('1')
        else : print('0')   
    elif input_str[0] == 'front' :
        if not s : 
            print('-1')
        else : print(s[0])
    elif input_str[0]  == 'back' :
        if not s :
            print('-1')
        else : print(s[len(s)-1])