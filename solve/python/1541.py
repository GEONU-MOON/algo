import sys
input = sys.stdin.readline

example = input().rstrip().split('-')

answer = sum(map(int, example[0].split('+'))) - sum(sum(map(int, x.split('+'))) for x in example[1:])

print(answer)