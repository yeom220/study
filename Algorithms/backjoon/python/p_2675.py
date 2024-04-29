n = int(input())
for _ in range(n):
    r, str = input().split()
    new_str = [c * int(r) for c in str]
    print(''.join(new_str))
