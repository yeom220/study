import queue

s = []

msg = input('입력: ')
for c in msg:
    s.append(c)

print('출력: ', end='')
while len(s) > 0:
    print(s.pop(), end='')
print()

q = queue.LifoQueue(maxsize=20)
msg = input('입력: ')
for c in msg:
    q.put(c)

print('출력: ', end='')
while not q.empty():
    print(q.get(), end='')
print()