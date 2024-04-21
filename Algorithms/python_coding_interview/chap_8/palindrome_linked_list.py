# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
import collections
from typing import Optional, List, Deque

from chap_8.my_utils import *

input = [1, 2, 2, 1]
expected = True


# input = [1, 2]
# expected = False


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # 1. 리스트 변환
        # q: List = []
        #
        # if not head:
        #     return True
        #
        # # 리스트 변환
        # node = head
        # while node is not None:
        #     q.append(node.val)
        #     node = node.next
        #
        # # 팰린드롬 판별
        # while len(q) > 1:
        #     if q.pop(0) != q.pop():
        #         return False
        # return True

        # # 2. 데크를 이용한 최적화
        # q: Deque = collections.deque()
        #
        # if not head:
        #     return True
        #
        # node = head
        # while node is not None:
        #     q.append(node.val)
        #     node = node.next
        # while len(q) > 1:
        #     if q.popleft() != q.pop():
        #         return False
        #     return True

        # 3. 런너를 이용한 우아한 풀이
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


instance = Solution()
result = instance.isPalindrome(toLinkedList(input))
print(expected == result, result)
