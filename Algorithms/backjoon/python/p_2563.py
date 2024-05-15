n = int(input())
width = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    index_y = y - 1
    while index_y < y + 9:
        index_x = x - 1
        while index_x < x + 9:
            width[index_y][index_x] = 1
            index_x += 1
        index_y += 1

result = 0
for arr in width:
    result += arr.count(1)

print(result)
