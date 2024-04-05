import math

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for j in nums : 
    if isPrime(j) : 
        cnt += 1
        
print(cnt)