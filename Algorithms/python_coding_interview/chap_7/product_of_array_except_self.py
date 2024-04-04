# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List

nums = [1, 2, 3, 4]
expected = [24, 12, 8, 6]


def productExceptSelf(self, nums: List[int]) -> List[int]:
    # 1.왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 오른쪽 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


output = productExceptSelf(nums, nums)
print(output == expected, output)
