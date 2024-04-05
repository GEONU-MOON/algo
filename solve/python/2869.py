''' a,b,v = map(int,input().split())
d = 0	#올라가는 데 걸리는 일수
h = 0	#올라간 높이
while 1:
    d+=1
    if a*d-b*(d-1)>=v:
        break
print(d)
-> 타임에러 '''  

import math
a,b,v = map(int, input().split())
print((math.ceil((v-a)/(a-b))+1))