# 메모리 초과로 실패
n = int(input())
answer = 1
sum_arr = [1] * (n + 1)
for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i - 1] + i
p1 = 0
p2 = 1
while p1 < p2 < n:
    tmp = sum_arr[p2] - sum_arr[p1]
    if tmp == n:
        answer += 1
        p2 += 1
    elif tmp > n:
        p1 += 1
    else:
        p2 += 1

print(answer)
