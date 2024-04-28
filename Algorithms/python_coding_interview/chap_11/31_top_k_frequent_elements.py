# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
import collections
import heapq
from typing import List

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
input = [1, 1, 1, 2, 2, 3]
k = 2
expected = [1, 2]


# # Example 2:
# # Input: nums = [1], k = 1
# # Output: [1]
# input = [1]
# k = 1
# expected = [1]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #1. Couter를 이용한 음수 순 추출
        # freqs = collections.Counter(nums)
        # freqs_heap = []
        # # 힙에 음수로 삽입
        # for f in freqs:
        #     heapq.heappush(freqs_heap, (-freqs[f], f))
        #
        # topk = list()
        # # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        # for _ in range(k):
        #     topk.append(heapq.heappop(freqs_heap)[1])
        #
        # return topk

        # 2. 파이썬다운 방식
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


s = Solution()
result = list(s.topKFrequent(input, k))
print(expected == result, result)
