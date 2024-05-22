# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
from typing import Optional, List

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
expected = [3, 9, 20, None, None, 15, 7]


# # Example 2:
# # Input: preorder = [-1], inorder = [-1]
# # Output: [-1]
# preorder = [-1]
# inorder = [-1]
# expected = [-1]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node


s = Solution()
result = my_utils.binary_tree_to_list(s.buildTree(preorder, inorder))
print(expected == result, result)
