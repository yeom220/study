# Given a binary tree, determine if it is height-balanced
from typing import Optional

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
input = [3, 9, 20, None, None, 15, 7]
expected = True

# # Example 2:
# # Input: root = [1,2,2,3,3,null,null,4,4]
# # Output: false
# input = [1, 2, 2, 3, 3, None, None, 4, 4]
# expected = False

# # Example 3:
# # Input: root = []
# # Output: true
# input = []
# expected = True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


s = Solution()
result = s.isBalanced(my_utils.list_to_binary_tree(input))
print(expected == result, result)
