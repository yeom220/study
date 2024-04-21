# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
from typing import Optional

from chap_8.my_utils import ListNode, toLinkedList, toList

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
input = [1, 2, 3, 4]
expected = [2, 1, 4, 3]
# # Example 2:
# # Input: head = []
# # Output: []
# input = []
# expected = []
# # Example 3:
# # Input: head = [1]
# # Output: [1]
# input = [1]
# expected[1]


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # #1 값만 교환
        # cur = head
        # while cur and cur.next:
        #     # 값만 교환
        #     cur.val, cur.next.val = cur.next.val, cur.val
        #     cur = cur.next.next
        # return head

        # #2. 반복 구조로 스왑
        # root = prev = ListNode(None)
        # prev.next = head
        # while head and head.next:
        #     # b가 a(head)를 가리키도록 할당
        #     b = head.next
        #     head.next = b.next
        #     b.next = head
        #
        #     # prev가 b를 가리키도록 할당
        #     prev.next = b
        #
        #     # 다음번 비교를 위해 이동
        #     head = head.next
        #     prev = prev.next.next
        # return root.next

        # 3. 재귀 구조로 스왑
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

s = Solution()
result = toList(s.swapPairs(toLinkedList(input)))
print(expected == result, result)
