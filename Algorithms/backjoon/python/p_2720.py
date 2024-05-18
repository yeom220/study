t = int(input())

result = [0, 0, 0, 0]

for _ in range(t):
    c = int(input())
    result[0] = str(c // 25)
    c = c % 25
    result[1] = str(c // 10)
    c = c % 10
    result[2] = str(c // 5)
    c = c % 5
    result[3] = str(c)
    print(' '.join(result))
