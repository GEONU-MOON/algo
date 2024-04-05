import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n) : 
    dead, cup = map(int, input().split())
    arr.append((dead, cup))

arr.sort()

queue = []

for i in arr :
    heapq.heappush(queue, i[1])
    if i[0] < len(queue) :
        heapq.heappop(queue)
        
print(sum(queue)) 


# 정렬: 먼저, 모든 과제를 데드라인에 따라 오름차순으로 정렬. 이는 데드라인이 가까운 과제부터 처리할 수 있도록 하기 위함.

# 최소 힙 사용: 적은 컵라면을 주는 과제부터 제거할 수 있도록 최소 힙을 사용. 힙에는 각 과제에서 받을 수 있는 컵라면의 수가 저장.

# 과제 처리: 정렬된 과제 리스트를 순회하면서, 각 과제의 컵라면 수를 힙에 추가. 
# 이때, 현재 힙의 크기(즉, 현재까지 선택한 과제의 수)가 해당 과제의 데드라인보다 크다면, 데드라인을 초과하는 과제가 있다는 의미이므로, 
# 힙에서 가장 작은 요소(가장 적은 컵라면을 주는 과제)를 제거. 
# 이렇게 하면 데드라인 내에 수행할 수 있는 과제들 중에서 가장 많은 컵라면을 얻을 수 있는 과제들만 선택.

# 결과 출력: 모든 과제를 처리한 후, 힙에 남아 있는 요소들의 합(즉, 선택된 과제들로부터 받을 수 있는 컵라면의 총 수)을 출력.