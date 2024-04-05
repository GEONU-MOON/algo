import sys
n = int(sys.stdin.readline())
stack = [] 
start = 1
answer = []

for _ in range(n):
    nums = int(sys.stdin.readline())
    while start <= nums: 
        stack.append(start) 
        answer.append('+')
        start += 1
    
    if stack[-1] == nums : 
        stack.pop()
        answer.append('-')
    
    else : 
        print("NO") 
        break

else :
    for i in answer :
        print(i)


