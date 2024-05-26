arr = [0 for _ in range(10001)]
m = int(input())
n = int(input())
for cur in range(m, n + 1):
    if arr[cur] == 2:
        continue
    count = 0
    mul = 2
    for i in range(2, cur):
        if cur % i == 0:
            count += 1
            break
    if count == 0:
        arr[cur] = 1
    else:
        while cur * mul < n:
            arr[cur * mul] = 2
            mul += 1
sum = 0
answer = []
for i in range(m, n + 1):
    if i == 1:
        continue
    if arr[i] == 1:
        sum += i
        answer.append(i)

if len(answer) > 0:
    print(sum)
    print(answer[0])
else:
    print(-1)
