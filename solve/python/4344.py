c = int(input())  # 학생의 수 입력
for _ in range(c):
    score = list(map(int, input().split()))  # 각 학생의 점수 입력
    avg = sum(score) / len(score)  # 평균 계산
    cnt = 0
    for i in score:
        if i > avg:
            cnt += 1
    ans = cnt / len(score) * 100
    print('%.3f' % ans + '%')