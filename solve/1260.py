import sys

def dfs(idx) : 
    global vistied
    vistied[idx]  = True    # 1번 노드는 방문한 적이 있다
    print(idx, end  = ' ')  # 한 줄씩 출력해라
    for next in range(1, n + 1) :
        if not vistied[next] and graph[idx][next] : #만약에 다음 노드가 방문된 적이 없다면, 그리고 그래프에 인덱스의 넥스트가 있다면 가겠다
            dfs(next)
            
def bfs():
    global q, vistied # 큐랑 비지티드가 필요
    while q : # q에 값이 있을 때까지
        cur = q.pop(0) # 큐에 가장 위에 있는걸 pop = 0번 인덱스를 뽑아와서 cur에 담아주겠다
        print(cur, end = ' ')
        for next in range(1, n + 1) :
            if not vistied[next] and graph[cur][next] :
                vistied[next] = True
                q.append(next)
        
n, m, v = map(int, sys.stdin.readline().split()) # n = 노드의 개수 m = 간선의 개수 v = 시작지점

graph = [[False] * (n + 1) for _ in range(n + 1)]
vistied = [False] * (n + 1)

# 그래프 정보 입력
for _ in range(m) : 
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True
# dfs
dfs(v)
print() # 줄 바꿈
# bfs
vistied = [False] * (n + 1) # 위에서 dfs했으니까 visited 배열을 다시 한 번 초기화
q = [v]
vistied[v] = True # v라는 노드를 다시 재방문하지 않도록 
bfs()