import sys

N = int(sys.stdin.readline())
Nums = list(map(int, sys.stdin.readline().split()))
Nums.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    # 왼쪽 포인터를 정렬된 리스트의 시작으로 설정합니다.
    left = 0
    # 오른쪽 포인터를 정렬된 리스트의 끝으로 설정합니다.
    right = N - 1
    
    # 이진 탐색을 수행합니다.
    while left <= right:
        # 중간값을 찾습니다.
        mid = (left + right) // 2
        # 쿼리 값이 중간값보다 큰 경우 왼쪽 포인터를 이동시킵니다.
        if m > Nums[mid]:
            left = mid + 1
        # 쿼리 값이 중간값보다 작은 경우 오른쪽 포인터를 이동시킵니다.
        elif m < Nums[mid]:
            right = mid - 1
        # 쿼리 값과 중간값이 일치하는 경우 반복을 종료합니다.
        else:
            left = mid
            right = mid
            break
    
    # left와 right가 동일한 경우는 쿼리 값이 리스트에 존재하는 경우입니다.
    if left == mid and right == mid:
        print(1)
    # 그렇지 않은 경우는 쿼리 값이 리스트에 존재하지 않는 경우입니다.
    else:
        print(0)