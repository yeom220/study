# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
from typing import Optional

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
input1 = [1, 3, 2, 5]
input2 = [2, 1, 3, None, 4, None, 7]
expected = [3, 4, 5, 5, 4, None, 7]


# # Example 2:
# # Input: root1 = [1], root2 = [1,2]
# # Output: [2,2]
# input1 = [1]
# input2[1, 2]
# expected = [2, 2]

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2


s = Solution()
result = my_utils.binary_tree_to_list(
    s.mergeTrees(my_utils.list_to_binary_tree(input1), my_utils.list_to_binary_tree(input2))
)
print(expected == result, result)
