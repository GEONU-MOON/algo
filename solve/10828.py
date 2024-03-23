n = int(input())

s = [input().split() for _ in range(n)]
a = []

for i in s :
    if i[0] == 'push' :
        a.append(i[1])
    elif i[0] == 'top' :
        if len(a) == 0 :
            print('-1')
        else : 
            print(a[-1])
    elif i[0] == 'pop' :
        if len(a) == 0 :
            print('-1')
        else :
            b = a.pop()
            print(b)
    elif i[0] == 'size' :
        print(len(a))
    elif i[0] == 'empty' :
        if len(a) == 0 :
            print('1')
        else :
            print('0')