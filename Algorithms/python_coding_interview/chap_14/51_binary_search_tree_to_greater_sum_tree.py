# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# Output: [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
input = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
expected = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]


# # Example 2:
# # Input: root = [0,None,1]
# # Output: [1,None,1]
# input = [0, None, 1]
# expected = [1, None, 1]

class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 1. 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root


s = Solution()
result = my_utils.binary_tree_to_list(s.bstToGst(my_utils.list_to_binary_tree(input)))
print(expected == result, result)
