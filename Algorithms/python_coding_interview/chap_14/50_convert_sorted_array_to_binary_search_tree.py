# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.
from typing import Optional, List

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
input = [-10, -3, 0, 5, 9]
expected = [0, -3, 9, -10, None, 5]


# # Example 2:
# # Input: nums = [1,3]
# # Output: [3,1]
# # Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
# input = [1, 3]
# expected = [3, 1]

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node


s = Solution()
result = my_utils.binary_tree_to_list(s.sortedArrayToBST(input))
print(expected == result, result)
