# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
import collections
from typing import Optional, List

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
input = root = [3, 9, 20, None, None, 15, 7]
expected = 3


# # Example 2:
# # Input: root = [1,null,2]
# # Output: 2
# input = [1,None,2]
# expected = 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Utils:
    def __init__(self):
        return

    def list_to_binary_tree(self, list: List) -> TreeNode:
        if not list:
            return None

        root = TreeNode(list[0])
        queue = [root]
        i = 1

        while queue and i < len(list):
            node = queue.pop(0)

            if i < len(list) and list[i] is not None:
                node.left = TreeNode(list[i])
                queue.append(node.left)
            i += 1

            if i < len(list) and list[i] is not None:
                node.right = TreeNode(list[i])
                queue.append(node.right)
            i += 1

        return root


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. 반복 구조로 BFS 풀이
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth


s = Solution()
u = Utils()
result = s.maxDepth(u.list_to_binary_tree(input))
print(expected == result, result)
