import sys

n = int(input())  # 회의의 수를 입력받음

endPoint: int = 0  # 마지막 회의의 종료 시간을 추적하는 변수
answer: int = 0  # 사용할 수 있는 최대 회의 수

arr = []  # 회의 시간을 저장할 리스트

# 모든 회의의 시작 시간과 종료 시간을 입력받아 리스트에 저장
for i in range(0,n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])

# 회의를 종료 시간을 기준으로 정렬하고, 종료 시간이 같다면 시작 시간을 기준으로 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# 정렬된 회의 리스트를 순회
for newStart, newEnd in arr:
    # 직전에 선택된 회의의 종료 시간이 현재 회의의 시작 시간보다 작거나 같다면,
    # 현재 회의를 선택할 수 있음
    if endPoint <= newStart:
        answer += 1  # 선택된 회의 수를 하나 증가시킴
        endPoint = newEnd  # 마지막 회의의 종료 시간을 현재 회의의 종료 시간으로 업데이트

# 사용할 수 있는 최대 회의 수를 출력
print(answer)