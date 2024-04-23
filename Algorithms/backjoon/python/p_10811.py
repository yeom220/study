n, m = map(int, input().split())
baskets = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    p1, p2 = i, j
    while p1 < p2:
        baskets[p1], baskets[p2] = baskets[p2], baskets[p1]
        p1 += 1
        p2 -= 1

for i in range(1, len(baskets)):
    print(baskets[i], end=' ')