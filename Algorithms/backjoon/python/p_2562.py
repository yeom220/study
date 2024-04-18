nums = []
for _ in range(9):
    nums.append(int(input()))
max = 0
for n in nums:
    if n > max:
        max = n

index = nums.index(max)
print(max, index + 1)
