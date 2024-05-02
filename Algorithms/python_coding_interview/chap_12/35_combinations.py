# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.
import itertools
from typing import List

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
n, k = 4, 2
expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


# # Example 2:
# # Input: n = 1, k = 1
# # Output: [[1]]
# # Explanation: There is 1 choose 1 = 1 total combination.
# n = k = 1
# expected = [[1]]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1. DFS로 k개 조합 생성
        # results = []
        #
        # def dfs(elements, start: int, k: int):
        #     print('start, k', start, k)
        #     print('elements', elements)
        #
        #     if k == 0:
        #         results.append(elements[:])
        #         print('results', results)
        #
        #     for i in range(start, n + 1):
        #         print('i, k', i, k)
        #         elements.append(i)
        #         dfs(elements, i + 1, k - 1)
        #         print(elements.pop())
        #
        # dfs([], 1, k)
        # return results

        # 2. itertools 모듈 사용
        return list(map(list, itertools.combinations(range(1, n + 1), k)))


s = Solution()
result = s.combine(n, k)
print(expected == result, result)
