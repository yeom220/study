# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
from typing import Optional

from chap_14 import my_utils
from chap_14.my_utils import TreeNode

# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
root = [10, 5, 15, 3, 7, None, 18]
low = 7
high = 15
expected = 32


# # Example 2:
# # Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# # Output: 23
# # Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
# root = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
# low = 6
# high = 10
# expected = 23

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # #1. 재귀 구조 DFS로 브루트포스 탐색
        # if not root:
        #     return 0
        #
        # return (root.val if low <= root.val <= high else 0) + \
        #     self.rangeSumBST(root.left, low, high) + \
        #     self.rangeSumBST(root.right, low, high)

        # #2. DFS 가지치기로 필요한 노드 탐색
        # def dfs(node: TreeNode):
        #     if not node:
        #         return 0
        #
        #     if node.val < low:
        #         return dfs(node.right)
        #     elif node.val > high:
        #         return dfs(node.left)
        #     return node.val + dfs(node.left) + dfs(node.right)
        #
        # return dfs(root)

        # # 3. 반복 구조 DFS로 필요한 노드 탐색
        # stack, sum = [root], 0
        # # 스택 이용 필요한 노드 DFS 반복
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         if node.val > low:
        #             stack.append(node.left)
        #         if node.val < high:
        #             stack.append(node.right)
        #         if low <= node.val <= high:
        #             sum += node.val
        #
        # return sum

        # 4. 반복 구조 BFS로 필요한 노드 탐색
        queue, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum


s = Solution()
result = s.rangeSumBST(my_utils.list_to_binary_tree(root), low, high)
print(expected == result, result)
