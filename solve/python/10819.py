from itertools import permutations
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = 0
for i in permutations(arr) :
    diff = 0
    for j in range(1,N):
        diff += abs(i[j-1] - i[j])
    if diff > result :
        result = diff
print(result)