A, B, C = map(int, input().split())

def function(A, B, C) :
    if B == 1 :
        return A % C

    mod = function(A, B // 2, C)

    if B % 2 == 1 :
        return ((mod * mod) % C) * A % C
    else:
        return (mod * mod) % C

print(function(A, B, C))