import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
location = [0] * n

for i in range(n):
    t = top[i]
    while stack and top[stack[-1]] < t:
        stack.pop()
    if stack:
        location[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, location))))
