x = int(input())
y = int(input())
quadrant1 = x > 0 and y > 0
quadrant2 = x < 0 < y
quadrant3 = x < 0 and y < 0
quadrant4 = x > 0 > y

if quadrant1:
    print(1)
elif quadrant2:
    print(2)
elif quadrant3:
    print(3)
elif quadrant4:
    print(4)
