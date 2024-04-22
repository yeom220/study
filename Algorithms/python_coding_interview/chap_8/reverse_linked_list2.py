# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
from typing import Optional

from chap_8.my_utils import ListNode, toList, toLinkedList

# # Example 1:
# # Input: head = [1,2,3,4,5], left = 2, right = 4
# # Output: [1,4,3,2,5]
# input = [1, 2, 3, 4, 5]
# left = 2
# right = 4
# expected = [1, 4, 3, 2, 5]


# # Example 2:
# # Input: head = [5], left = 1, right = 1
# # Output: [5]
# input = [5]
# left = 1
# right = 1
# expected = [5]

# Example 3:
# Input: head = [1,2,3,4,5,6], left = 2, right = 5
# Output: [1,5,4,3,2,6]
input = [1, 2, 3, 4, 5, 6]
left = 2
right = 5
expected = [1, 5, 4, 3, 2, 6]

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # 1. 반복 구조로 노드 뒤집기
        root = start = ListNode(None)
        root.next = head
        # 뒤집기 바로 전 노드까지 start노드 이동
        for _ in range(left - 1):
            start = start.next
        # 뒤집을 첫번째 노드를 end노드로 지정
        end = start.next
        # 인덱스 범위 만큼 뒤집기 반복
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


s = Solution()
result = toList(s.reverseBetween(toLinkedList(input), left, right))
print(expected == result, result)