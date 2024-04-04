# 배열 파티션 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ...,
# (an, bn) such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.
from typing import List

nums = [1, 4, 3, 2]
expected = 4


def arrayPairSum(self, nums: List[int]) -> int:
    # nums.sort()
    # sum = 0

    # 1.오름차순 풀이
    # pair = []
    # for i in nums:
    #     pair.append(i)
    #     if len(pair) == 2:
    #         sum += min(pair)
    #         pair = []
    # return sum

    # 2.짝수 번째 값 계산
    # for i, n in enumerate(nums):
    #     if i % 2 == 0:
    #         sum += n
    # return sum

    # 3.파이썬다운 방식
    return sum(sorted(nums)[::2])

output = arrayPairSum(nums, nums)
print(output == expected, output)
