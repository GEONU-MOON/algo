import sys
input = sys.stdin.readline

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
    
print(arr)