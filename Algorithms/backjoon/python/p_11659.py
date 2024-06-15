import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = [arr[0]]
for i in range(1, n):
    sum_arr.append(sum_arr[i - 1] + arr[i])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    j_sum = sum_arr[j - 1]
    i_sum = sum_arr[i - 2]
    if i < 2:
        i_sum = 0
    print(j_sum - i_sum)
