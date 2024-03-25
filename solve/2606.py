import sys

input = sys.stdin.readline

def dfs(idx) : 
    global visited, graph, answer
    visited[idx] = True
    answer += 1
    
    for i in range(1, n + 1) :
        if not visited[i] and graph[idx][i] :
            dfs(i)

n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

# 1. graph 연결 정보 채우기
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
    
# 2. dfs(재귀함수) 호출
dfs(1)

# 3. 출력
print(answer - 1)
