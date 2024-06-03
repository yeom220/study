while True:
    lines = list(map(int, input().split()))
    sorted(lines)
    if sum(lines) == 0:
        break
    if lines.count(lines[0]) == 3:
        print('Equilateral')
    elif lines[2] >= lines[0] + lines[1]:
        print('Invalid')
    elif lines.count(lines[0]) == 2 or lines.count(lines[1]) == 2:
        print('Isosceles')
    else:
        print('Scalene')
