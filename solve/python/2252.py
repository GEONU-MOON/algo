import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split()) # 학생 수, 학생 순서
graph = [[] for _ in range(n+1)] # 학생 순서 그래프
table = [0] * (n+1) # 진입차수표

# 학생 수만큼 입력
for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    table[b] += 1
    
q = deque()
for i in range(1, n+1) :
    if table[i] == 0 :
        q.append(i)
        
while q : 
    now = q.popleft()
    for i in graph[now] :
        table[i] -= 1
        if table[i] == 0 :
            q.append(i)
    
    print(now, end = " ")