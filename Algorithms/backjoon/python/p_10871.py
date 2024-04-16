N, X = map(int, input().split())
A: [] = list(map(int, input().split()))
result: [] = list()
for n in A:
    if n < X:
        result.append(n)
for n in result:
    print(n, end=" ")
