# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of the path between two nodes is represented by the number of edges between them.
from typing import Optional

from chap_14.my_utils import TreeNode, list_to_binary_tree

# Example 1:
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).
input = [5, 4, 5, 1, 1, None, 5]
expected = 2


# # Example 2:
# # Input: root = [1,4,5,4,4,null,5]
# # Output: 2
# # Explanation: The shown image shows that the longest path of the same value (i.e. 4).
# input = [1,4,5,4,4,None,5]
# expected = 2

class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result


s = Solution()
result = s.longestUnivaluePath(list_to_binary_tree(input))
print(expected == result, result)
