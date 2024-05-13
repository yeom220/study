max_num = -1
index_x = -1
index_y = -1
for i in range(9):
    nums = list(map(int, input().split()))
    if max(nums) > max_num:
        max_num = max(nums)
        index_y = i
        index_x = nums.index(max_num)

print(max_num)
print(index_y + 1, index_x + 1)
