from sys import stdin

n, k = map(int, stdin.readline().split())

li =[]

for i in range(n):
   li.append(int(stdin.readline().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])
   
# 1. 데이터들을 1차원 배열에 담는다.
# 2. 최소 코인 갯수를 저장할 dp배열을 만들고 max(10001)으로 초기화시켜준다.
# 3. 코인 배열의 값을 가져오고
# 4. 그 값만큼 올리면서 for문을 돌아주는데
# 5. 현재 값에서 가져온 코인 값을 빼주었을 때의 코인 사용 개수에 지금 코인 개수 하나를 더한 값과 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교하여 더 작은 값을 dp배열에 담는다.