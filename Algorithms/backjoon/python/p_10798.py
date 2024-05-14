arr = []
for _ in range(5):
    arr.append(list(input()))

loop = 0
for i in range(5):
    loop = max(loop, len(arr[i]))

word = ''
for i in range(loop):
    for j in range(5):
        if len(arr[j]) > i:
            word += arr[j][i]

print(word)
