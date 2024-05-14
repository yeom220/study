# Given the root of a binary tree, invert the tree, and return its root.
import collections
from typing import Optional

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
input = [4, 2, 7, 1, 3, 6, 9]
expected = [4, 7, 2, 9, 6, 3, 1]

# # Example 2:
# # Input: root = [2,1,3]
# # Output: [2,3,1]
# input = [2, 1, 3]
# expected = [2, 3, 1]

# # Example 3:
# # Input: root = []
# # Output: []
# input = []
# expected = []

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #1. 파이썬 다운 방식(재귀)
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

        # #2. 반복 구조로 BFS
        # queue = collections.deque([root])
        #
        # while queue:
        #     node = queue.popleft()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)
        #
        # return root

        # #3. 반복 구조로 DFS
        # stack = collections.deque([root])
        #
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack.append(node.left)
        #         stack.append(node.right)
        #
        # return root

        # #4. 반복 구조로 DFS 후위 순회
        # stack = collections.deque([root])
        #
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         stack.append(node.left)
        #         stack.append(node.right)
        #         node.left, node.right = node.right, node.left
        #
        # return root


s = Solution()
result = my_utils.binary_tree_to_list(s.invertTree(my_utils.list_to_binary_tree(input)))
print(expected == result, result)