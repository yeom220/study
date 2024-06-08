n = int(input())
count = 0
mul = n - 2
for i in range(1, n - 1):
    count += (i * mul)
    mul -= 1

print(count)
print(3)
