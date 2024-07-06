# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Util:
    def to_linked_list(self, list: List) -> ListNode:
        li = []
        for i in range(len(list)):
            node = ListNode(list[i])
            li.append(node)

        for i in range(len(li) - 1):
            li[i].next = li[i + 1]

        return li[0]

    def to_list(self, node: ListNode, type: str = None) -> List:
        list: List = []
        while node:
            if type == 'int':
                list.append(int(node.val))
            elif type == 'str':
                list.append(str(node.val))
            else:
                list.append(node.val)
            node = node.next
        return list
