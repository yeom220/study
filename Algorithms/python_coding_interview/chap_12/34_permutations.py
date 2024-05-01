# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
from typing import List

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
input = [1,2,3]
expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# # Example 2:
# # Input: nums = [0,1]
# # Output: [[0,1],[1,0]]
# input = [0,1]
# expected = [[0,1],[1,0]]

# # Example 3:
# # Input: nums = [1]
# # Output: [[1]]
# input = [1]
# expected = [[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            print('elements', elements)
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
                print('results', results)

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                print('next_elements', next_elements)
                next_elements.remove(e)
                print('next_elements', next_elements)

                print('prev_elements', prev_elements)
                prev_elements.append(e)
                print('prev_elements', prev_elements)
                dfs(next_elements)
                print(prev_elements.pop())

        dfs(nums)
        return results


s = Solution()
result = s.permute(input)
print(expected == result, result)

