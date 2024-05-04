units = list(map(int, input().split()))
arr = [1, 1, 2, 2, 2, 8]
result = [0] * len(units)
for i in range(len(units)):
    while units[i] != arr[i]:
        if units[i] > arr[i]:
            units[i] -= 1
            result[i] -= 1
        else:
            units[i] += 1
            result[i] += 1

for i in result:
    print(i, end=' ')