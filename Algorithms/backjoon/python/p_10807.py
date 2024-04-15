import sys

N: int = int(sys.stdin.readline())
arr: [] = sys.stdin.readline().split()
v: int = int(sys.stdin.readline())
count: int = 0
for i in range(N):
    num: int = int(arr[i])
    if v == num:
        count += 1
print(count)