import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    
    cnt = 1
    firstplace = arr[0][1]
    for i in range(1, N) :
        if firstplace > arr[i][1] :
            cnt += 1
            firstplace = arr[i][1]           
    print(cnt)
    