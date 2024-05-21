# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
import sys
from typing import Optional

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1
input = [4, 2, 6, 1, 3]
expected = 1


# # Example 2:
# # Input: root = [1,0,48,null,null,12,49]
# # Output: 1
# input = [1, 0, 48, None, None, 12, 49]
# expected = 1

class Solution:
    # # 1. 재귀 구조 중위 순회 비교 결과
    # prev = -sys.maxsize
    # result = sys.maxsize
    #
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    #     if root.left:
    #         self.minDiffInBST(root.left)
    #
    #     self.result = min(self.result, root.val - self.prev)
    #     self.prev = root.val
    #
    #     if root.right:
    #         self.minDiffInBST(root.right)
    #
    #     return self.result

    # 2. 반복 구조로 중위 순회
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result


s = Solution()
result = s.minDiffInBST(my_utils.list_to_binary_tree(input))
print(expected == result, result)
