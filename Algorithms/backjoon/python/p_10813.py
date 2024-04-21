import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [i for i in range(0, N+1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    tmp = baskets[i]
    baskets[i] = baskets[j]
    baskets[j] = tmp

baskets.remove(0)
for ball in baskets:
    print(ball, end=' ')