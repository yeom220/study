n = int(input())

count = 0
for _ in range(n):
    s = input()
    checked = []
    prev = ''
    is_group = True
    for c in s:
        if prev != c and checked.count(c) == 0:
            checked.append(c)
            prev = c
        elif prev == c:
            continue
        else:
            is_group = False
            break
    if is_group:
        count += 1

print(count)
