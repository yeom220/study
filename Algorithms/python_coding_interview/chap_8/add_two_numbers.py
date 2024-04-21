# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional, List

from chap_8.my_utils import ListNode, toLinkedList, toList

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
l1 = [2, 4, 3]
l2 = [5, 6, 4]
expected = [7, 0, 8]

# # Example 2:
# # Input: l1 = [0], l2 = [0]
# # Output: [0]
# l1 = [0]
# l2 = [0]
# expected = [0]

# # Example 3:
# # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# # Output: [8,9,9,9,0,0,0,1]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
# expected = [8, 9, 9, 9, 0, 0, 0, 1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # 1 자료형 반환
        # a = self.toList(self.reverseList(l1))
        # b = self.toList(self.reverseList(l2))
        # resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        #
        # return self.toReversedLinkedList(str(resultStr))

        #2 전가산기 구현
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # 몫(자리올림수)와 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next

    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node


instance = Solution()
result = toList(instance.addTwoNumbers(toLinkedList(l1), toLinkedList(l2)), 'int')
print(expected == result, result)
