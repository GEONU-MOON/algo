# import sys

# N, M = map(int, sys.stdin.readline().split())

# cards = list(map(int, sys.stdin.readline().split()))
    
# result = 0
# Max = 0

# for i in range(N-2): 
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             if cards[i]+cards[j]+cards[k] > M: 
#                 continue
#             else:
#                 result = cards[i]+ cards[j]+ cards[k]
#                 if Max <= result:
#                     Max = result

# print(Max)
n, m = map(int, input().split())
card_list = list(map(int, input().split()))
max_s = 0

def combination(card_list, idx, cards):
    global max_s
 
    if len(cards) == 3:
        s = sum(cards)
        if s <= m and s > max_s:
            max_s = s
    else:
        for i in range(idx, len(card_list)):
            cards.append(card_list[i])
            combination(card_list, i + 1, cards)
            cards.pop()  #선택한 카드를 다시 제거하여 다른 조합을 확인.
            
combination(card_list, 0, [])

print(max_s)