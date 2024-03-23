import sys

N = int(sys.stdin.readline())

input_words = []

for i in range(N) :
    input_words.append(sys.stdin.readline())
    
list_words = list(set(input_words))

sorted_words = []

for i in list_words :
    sorted_words.append((len(i),i))
    
result = sorted(sorted_words)

for i,j in result :
    print(j.strip())