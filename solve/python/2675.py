a = int(input())
for i in range(a):
  R, S = input().split()
  for c in S:
    print(int(R) * c, end='')
  print()