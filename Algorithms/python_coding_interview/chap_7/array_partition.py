# 배열 파티션 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ...,
# (an, bn) such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.
from typing import List

nums = [1,4,3,2]
expected = 4

def arrayPairSum(self, nums: List[int]) -> int:
