import sys
from collections import deque

br = sys.stdin

N, L = map(int, br.readline().split())
P = list(map(int, br.readline().split()))


class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

# TODO: 시간 초과...
mydeque = deque()
for i, v in enumerate(P):
    now = v
    while mydeque and mydeque[-1].val >= now:
        mydeque.pop()

    mydeque.append(Node(val=v, idx=i))

    if mydeque and mydeque[0].idx <= i - L:
        mydeque.popleft()

    sys.stdout.write(str(mydeque[0].val) + ' ')

sys.stdout.close()
