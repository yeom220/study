T = int(input())
for i in range(1, T + 1):
    for j in range(T):
        if j < T - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
