n = int(input())
sum, max = 0, 0
list = list(map(int, input().split()))
for e in list:
    if e > max:
        max = e
    sum += e
print((sum / max) * 100 / n)
