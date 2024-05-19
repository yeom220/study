n = int(input())
result = 1
ranges = 1
while n > ranges:
    ranges += (6 * result)
    result += 1

print(result)
