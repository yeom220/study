n = int(input())
x_min = y_min = 100001
x_max = y_max = -100001
for _ in range(n):
    x, y = map(int, input().split())
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    x_max = max(x_max, x)
    y_max = max(y_max, y)

x_line = x_max - x_min
y_line = y_max - y_min
print(x_line * y_line)
