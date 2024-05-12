n, m = map(int, input().split())

result = []
for _ in range(n):
    inner = list(map(int, input().split()))
    result.append(inner)

for i in range(n):
    inner = list(map(int, input().split()))
    for j in range(m):
        result[i][j] = result[i][j] + inner[j]

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()
