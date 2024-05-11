# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
import collections
from typing import Optional

from chap_14.my_utils import TreeNode, list_to_binary_tree

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
result = s.maxDepth(list_to_binary_tree(input))
print(expected == result, result)
