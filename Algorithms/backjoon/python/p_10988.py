s = input()
p1 = 0
p2 = len(s) - 1
isPal = 1
for _ in range(len(s)):
    if p1 >= p2:
        break
    if s[p1] != s[p2]:
        isPal = 0
        break
    p1 += 1
    p2 -= 1

print(isPal)
