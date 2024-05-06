n = int(input())
count = 1

for i in range(1, n * 2):
    printed = 0
    blank = abs(n - i)
    for j in range(n * 2):
        if blank > 0:
            print(' ', end='')
            blank -= 1
        elif count > printed:
            print('*', end='')
            printed += 1
        else:
            break
    if n > i:
        count += 2
    else:
        count -= 2
    print()
