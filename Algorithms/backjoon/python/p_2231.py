n = int(input())
m = n
digit = 0
while m > 0:
    m = m // 10
    digit += 1

s = n - (digit * 9)
if s < 0:
    s = 0

result = 0
for i in range(s, n):
    a = i
    sum = 0
    while a > 0:
        sum += a % 10
        a = a // 10
    sum += i
    if sum == n:
        result = i
        break

print(result)
