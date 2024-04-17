n = int(input())
min = 1000001
max = -1000001
list = list(map(int, input().split(' ')))
for i in list:
    if max < i:
        max = i
    if i < min:
        min = i
print(min, max)
