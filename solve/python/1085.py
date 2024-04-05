x, y, w, h = map(int, input().split())
best = min(x, y, w-x, h-y)
print(best)