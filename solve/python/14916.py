change = int(input())
cnt = 0

while change > 0 :
    if change % 5 == 0:
        cnt += change // 5
        change %= 5
        break
    else:
        change -= 2
        cnt += 1

if change != 0:
    print(-1)
else:
    print(cnt)



# money = int(input())
# dp = [-1]*(100001)

# dp[2] = 1
# dp[4] = 2
# dp[5] = 1

# for i in range(6, money+1):
#     if dp[i-5]==-1 and dp[i-2]==-1:
#         dp[i] = -1
#     elif dp[i-5]==-1:
#         dp[i] = dp[i-2]+1
#     elif dp[i-2]==-1:
#         dp[i] = dp[i-5]+1
#     else:
#         dp[i] = min(dp[i-5]+1, dp[i-2]+1)
# print(dp[money])