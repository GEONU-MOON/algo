import sys

N = int(sys.stdin.readline())
input_list = []

for i in range(N) : 
    input_list.append(int(sys.stdin.readline()))
    
max = input_list[-1]
cnt = 1

for j in range(N-1, -1, -1) :
    if input_list[j] > max :
        cnt += 1
        max = input_list[j]
        
print(cnt)