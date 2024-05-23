# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
import heapq
from typing import List

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
nums = [3, 2, 1, 5, 6, 4]
k = 2
expected = 5


# # Example 2:
# # Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# # Output: 4
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# expected = 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # 1. heapq 모듈 이용
        # heap = list()
        # for n in nums:
        #     heapq.heappush(heap, -n)
        #
        # for _ in range(1, k):
        #     heapq.heappop(heap)
        #
        # return -heapq.heappop(heap)

        # # 2. heapq 모듈의 heapify 이용
        # heapq.heapify(nums)
        #
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        #
        # return heapq.heappop(nums)

        # # 3. heapq 모듈의 nlargest 이용
        # return heapq.nlargest(k, nums)[-1]

        # 4. 정렬을 이용한 풀이
        return sorted(nums, reverse=True)[k - 1]


s = Solution()
result = s.findKthLargest(nums, k)
print(expected == result, result)
