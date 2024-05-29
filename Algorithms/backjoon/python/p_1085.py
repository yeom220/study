x, y, w, h = map(int, input().split())
x_min = min((w - x), x)
y_min = min((h - y), y)
print(min(x_min, y_min))
