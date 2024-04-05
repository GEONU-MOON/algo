import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(idx) :
    global graph, visited
    visited[idx] = True
    for i in range(1, n +1) :
        if not visited[i] and graph[idx][i] :
            dfs(i)

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for i in range(m) : 
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True
    
for i in range(1, n + 1) :
    if not visited[i] : 
        dfs(i)
        cnt += 1

print(cnt)