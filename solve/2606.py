import sys


n=int(sys.stdin.readline())
v=int(sys.stdin.readline()) 

graph = [[] for i in range(n+1)]
visited=[0]*(n+1) 

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)

for i in range(v): 
    a,b=map(int,input().split())
    graph[a]+=[b] 
    graph[b]+=[a] 

dfs(1)
print(sum(visited)-1)