y = int(input())
t1 = y % 4 == 0
t2 = y % 100 != 0
t3 = (y % 4 == 0) & (y % 100 != 0)
t4 = y % 400 == 0
print(y, t1, t2, t3, t4)
if (y % 4 == 0) & (y % 100 != 0) | (y % 400 == 0):
    print(1)
else:
    print(0)

# if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#     print(1)
# else:
#     print(0)
