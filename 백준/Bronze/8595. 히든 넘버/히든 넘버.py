n = int(input())
arr = input()
num = ''
result = 0

for i in arr:
  if '0' <= i and i <= '9':
    num += i
  elif num != '':
    result += int(num)
    num = ''
if num != '':
  result += int(num)
  
print(result)