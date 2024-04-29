# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
from typing import List

# # Example 1:
# # Input: grid = [
# #   ["1","1","1","1","0"],
# #   ["1","1","0","1","0"],
# #   ["1","1","0","0","0"],
# #   ["0","0","0","0","0"]
# # ]
# # Output: 1
# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# expected = 1

# # Example 2:
# # Input: grid = [
# #   ["1","1","0","0","0"],
# #   ["1","1","0","0","0"],
# #   ["0","0","1","0","0"],
# #   ["0","0","0","1","1"]
# # ]
# # Output: 3
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
expected = 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return

            grid[i][j] = '0'
            # 동서남북 탐색
            dfs(i + 1, j) # 남
            dfs(i - 1, j) # 북
            dfs(i, j + 1) # 동
            dfs(i, j - 1) # 서

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1

        return count


s = Solution()
result = s.numIslands(grid)
print(expected == result, result)
