# Given the head of a singly linked list, group all the nodes
# with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
from typing import Optional

from chap_8.my_utils import ListNode, toLinkedList, toList

# # Example 1:
# # Input: head = [1,2,3,4,5]
# # Output: [1,3,5,2,4]
# input = [1, 2, 3, 4, 5]
# expected = [1, 3, 5, 2, 4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
input = [2, 1, 3, 5, 6, 4, 7]
expected = [2, 3, 6, 7, 1, 5, 4]


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None

        # 1. 반복 구조로 홀짝 노드 처리
        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀, 짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # odd 마지막 노드를 even 헤드 노드로 연결
        odd.next = even_head
        return head


s = Solution()
result = toList(s.oddEvenList(toLinkedList(input)))
print(expected == result, result)
