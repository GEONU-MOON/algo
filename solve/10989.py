import sys

n = int(input())

count = [0] * 10001

for i in range(n) :
    nums = int(sys.stdin.readline())
    count[nums] += 1
    
for i in range(len(count)) :
    for j in range(count[i]) :
        print(i)