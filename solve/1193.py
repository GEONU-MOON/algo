import sys

n = int(sys.stdin.readline())

line = 0
end = 0

while n > end:
    line += 1
    end += line
    
K = end - n

if line % 2 == 0 :
    a = line - K
    b = K + 1
else : 
    a = K + 1
    b = line - K
    
print(f'{a}/{b}')