a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
n1 = n0 + 1

result_n0 = (c - a1) * n0 - a0
result_n1 = (c - a1) * n1 - a0

if result_n0 < 0:
    print(0)
elif result_n0 <= result_n1:
    print(1)
else:
    print(0)
