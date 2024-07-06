# Given the head of a linked list, return the list after sorting it in ascending order.
#
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# input = [4, 2, 1, 3]
# expected = [1, 2, 3, 4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
input = [-1, 5, 3, 4, 0]
expected = [-1, 0, 3, 4, 5]

# Example 3:
# Input: head = []
# Output: []
# input = []
# expected = []

from typing import Optional, List

from chap_17.common import ListNode, Util


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. 병합정렬
        # if not (head and head.next):
        #     return head
        #
        # half, slow, fast = None, head, head
        # while fast and fast.next:
        #     half, slow, fast = slow, slow.next, fast.next.next
        # half.next = None
        #
        # l1 = self.sortList(head)
        # l2 = self.sortList(slow)
        #
        # return self.mergeTwoLists(l1, l2)

        # 3. 내장함수 사용
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head


u = Util()
s = Solution()
result = u.to_list(s.sortList(u.to_linked_list(input)))
print(result == expected, result)
