import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

Q = deque()
result = []

for i in range(1, n+1) :
    Q.append(i)
    
while Q : 
    for i in range(k-1) :
        Q.append(Q.popleft())
    result.append(Q.popleft())
    
print("<"+", ".join(list(map(str, result))) + ">")
        
    