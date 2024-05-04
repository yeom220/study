# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
from typing import List

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
input = [1, 2, 3]
expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# # Example 2:
# # Input: nums = [0]
# # Output: [[],[0]]
# input = [0]
# expected = [[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # def dfs(elements, index):
        #     result.append(elements[:])
        #
        #     for i in range(index, len(nums)):
        #         print('num: ', nums[i])
        #         elements.append(nums[i])
        #         print('elements', elements)
        #         dfs(elements, i + 1)
        #         print(elements.pop())
        #
        # dfs([], 0)
        # return result

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)
            print('index', index)
            print('path', path, id(path))

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                print('path in for', path, id(path), i, end=', ')
                id(path)
                dfs(i + 1, path + [nums[i]])
                print('path in after dfs', path, id(path))

        dfs(0, [])
        return result


s = Solution()
result = s.subsets(input)
print(expected == result, result)
