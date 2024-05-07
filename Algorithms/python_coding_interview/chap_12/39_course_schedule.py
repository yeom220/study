# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
import collections
from typing import List

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
numCourses = 2
prerequisites = [[1, 0]]
expected = True


# # Example 2:
# # Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# # Output: false
# # Explanation: There are a total of 2 courses to take.
# # To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# numCourses = 2
# prerequisites = [[1,0],[0,1]]
# Expected = False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # 1. DFS로 순환 구조 판별
        # graph = collections.defaultdict(list)
        # # 그래프 구성
        # for x, y in prerequisites:
        #     graph[x].append(y)
        #
        # print('graph', graph)
        # traced = set()
        #
        # def dfs(i):
        #     # 순환 구조이면 False
        #     if i in traced:
        #         return False
        #     traced.add(i)
        #     for y in graph[i]:
        #         if not dfs(y):
        #             return False
        #     # 탐색 종료 후 순환 노드 삭제
        #     traced.remove(i)
        #     return True
        #
        # # 순환구조 판별
        # for x in list(graph):
        #     print('x=', x)
        #     if not dfs(x):
        #         return False
        #
        # return True

        # 2. 가지치기를 이용한 최적화
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            # 이미 방문했던 노드이면 스킵
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


s = Solution()
result = s.canFinish(numCourses, prerequisites)
print(expected == result, result)
