# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(list: List) -> TreeNode:
    if not list:
        return None

    root = TreeNode(list[0])
    queue = [root]
    i = 1

    while queue and i < len(list):
        node = queue.pop(0)

        if i < len(list) and list[i] is not None:
            node.left = TreeNode(list[i])
            queue.append(node.left)
        i += 1

        if i < len(list) and list[i] is not None:
            node.right = TreeNode(list[i])
            queue.append(node.right)
        i += 1

    return root
