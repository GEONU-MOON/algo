import sys

# 초기 변수 설정
k = 0  # k 초기화
nums = set()  # 중복을 허용하지 않는 빈 집합 nums 생성
visit = []  # 방문 여부를 나타내는 리스트 visit 생성
num = []  # 조합된 숫자를 저장할 리스트 num 생성
arr = []  # 입력으로 받은 숫자들을 저장할 리스트 arr 생성

# 재귀 함수 정의
def solve(n: int):
    if n == k:  # n이 k와 같을 때, 조합된 숫자를 nums에 추가
        nums.add(''.join(num))  # 리스트 num을 문자열로 변환하여 집합 nums에 추가
    else:
        for i in range(len(arr)):  # 입력된 숫자들을 하나씩 확인
            if visit[i]:  # 해당 숫자를 방문하지 않았을 때
                visit[i] = False  # 해당 숫자를 방문했다고 표시
                num[n] = str(arr[i])  # 조합된 숫자의 n번째 자리에 숫자를 추가
                solve(n + 1)  # 재귀적으로 다음 자리를 채우기 위해 solve 함수 호출
                visit[i] = True  # 해당 숫자의 방문 여부를 초기화하여 다른 경우를 확인하기 위함

# 입력 처리
n, k = [int(sys.stdin.readline()) for _ in range(2)]  # 첫 번째 입력은 n, 두 번째 입력은 k로 받음
visit = [True] * n  # 초기에는 모든 숫자가 사용 가능하므로 visit 리스트를 True로 초기화
arr = [0] * n  # 입력받은 숫자를 저장할 리스트 arr을 0으로 초기화
num = [''] * k  # 조합된 숫자를 저장할 리스트 num을 빈 문자열로 초기화

for i in range(n):  # 입력받은 숫자를 arr 리스트에 저장
    arr[i] = int(sys.stdin.readline())

# 조합 함수 호출
solve(0)

# 결과 출력
print(len(nums))  # 중복을 허용하지 않는 집합 nums의 크기를 출력
