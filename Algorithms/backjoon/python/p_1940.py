# 시간초과 다시 풀어야 함
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        s = arr[i] + arr[j]
        if s == m:
            answer += 1
            break
        elif s > m:
            break
print(answer)
