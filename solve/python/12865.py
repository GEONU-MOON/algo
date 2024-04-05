import sys

input = sys.stdin.readline

N, K = map(int, input().split())

weight = [0] * 101
value = [0] * 101

d = [[0] * 100001 for _ in range(N + 1)]

for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= weight[i]:
            d[i][j] = max(d[i-1][j], d[i-1][j-weight[i]] + value[i])
        else:
            d[i][j] = d[i-1][j]

print(d[N][K])