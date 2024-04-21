# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional, List

from chap_8.my_utils import *

Input = [1, 2, 3, 4, 5]
Output = [5, 4, 3, 2, 1]


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. 재귀 구조로 뒤집기
        # def reverse(node: ListNode, prev: ListNode = None):
        #     if not node:
        #         return prev
        #     next, node.next = node.next, prev
        #     return reverse(next, node)
        #
        # return reverse(head)

        # 2. 반복 구조로 뒤집기
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev


instance = Solution()
result = toList(instance.reverseList(toLinkedList(Input)))
print(result == Output, result)
