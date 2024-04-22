mod_num = 42
nums = []
for _ in range(10):
    n = int(input())
    r = n % mod_num
    if nums.count(r) == 0:
        nums.append(r)

print(len(nums))