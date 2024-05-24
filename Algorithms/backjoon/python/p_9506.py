from typing import List


def print_result(input, nums: List[int]):
    result = str(input) + ' = ' + str(nums.pop(0))
    while nums:
        result += ' + ' + str(nums.pop(0))
    print(result)


while True:
    n = int(input())
    if n == -1:
        break
    nums = []
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)

    if n == sum(nums):
        print_result(n, nums)
    else:
        print('{0} is NOT perfect.'.format(n))
