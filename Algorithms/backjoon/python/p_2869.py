a, b, v = map(int, input().split())

move = a - b
print('move=', move)
day = v // move
print('day=', day)

c1 = v % move + move
print('c1=', c1)
c2 = v % move
print('c2=', c2)

if c1 <= a:
    day -= a // move
    day += 1
    print(day)
elif c2 == 0:
    print(day)
else:
    day += 1
    print(day)
