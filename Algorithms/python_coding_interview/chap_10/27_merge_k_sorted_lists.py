# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
import heapq
from typing import List, Optional

from chap_8.my_utils import ListNode

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
input = [[1, 4, 5], [1, 3, 4], [2, 6]]
expected = [1, 1, 2, 3, 4, 4, 5, 6]


# # Example 2:
# # Input: lists = []
# # Output: []
# input = []
# expected = []

# # Example 3:
# # Input: lists = [[]]
# # Output: []
# input = [[]]
# expected = []

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            print('idx', idx, 'result', result, 'result.next', result, next)
            result.next = node[2]
            print('result.next', result.next)

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
