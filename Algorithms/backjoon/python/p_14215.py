lines = list(map(int, input().split()))
max_idx = lines.index(max(lines))
max = lines.pop(max_idx)
if max >= sum(lines):
    diff = max - sum(lines) + 1
    max -= diff

print(max + sum(lines))
