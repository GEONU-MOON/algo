N = int(input())
M = []

for _ in range(N) :
     M.append(int(input()))
    
M = sorted(M)

for i in range(len(M)) :
    print(M[i])