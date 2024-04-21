# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from typing import Optional

from chap_8.my_utils import *

# INPUT
list1 = [1, 2, 4]
list2 = [1, 3, 4]
expected = [1, 1, 2, 3, 4, 4]


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 재귀 구조로 연결
        if (not list1) or (list2 and (list1.val > list2.val)):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


instance = Solution()
result = toList(instance.mergeTwoLists(toLinkedList(list1), toLinkedList(list2)))
print(result == expected, result)
