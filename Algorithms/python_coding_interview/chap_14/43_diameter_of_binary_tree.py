# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional

from chap_14.my_utils import TreeNode, list_to_binary_tree

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
input = [1, 2, 3, 4, 5]
expected = 3


# # Example 2:
# # Input: root = [1,2]
# # Output: 1
# input = [1,2]
# expected = 3


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest


s = Solution()
result = s.diameterOfBinaryTree(list_to_binary_tree(input))
print(expected == result, result)
