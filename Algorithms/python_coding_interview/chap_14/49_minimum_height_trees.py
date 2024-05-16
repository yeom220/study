# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
import collections
from typing import List

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
expected = [1]


# # Example 2:
# # Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# # Output: [3,4]
# n = 6
# edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
# expected = [3, 4]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. 단계별 리프 노드 제거
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


s = Solution()
result = s.findMinHeightTrees(n, edges)
print(expected == result, result)
