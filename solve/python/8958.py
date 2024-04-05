n=int(input())
for i in range(n) :
    ox = input()
    score = 0
    sumScore = 0
    for j in ox : 
        if j == "O" :
            score += 1
        else :
            score = 0
        sumScore += score
    print(sumScore)

# 점수를 더하다가 x가 나오면 총합을 내고 score를 0으로 초기화하는게 핵심!