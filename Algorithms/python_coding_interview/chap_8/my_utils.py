from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toLinkedList(arr: List) -> ListNode:
    if not arr:
        return ListNode()

    prev: ListNode = None
    for e in reversed(arr):
        node = ListNode(e)
        node.next = prev
        prev = node

    return node


def toList(node: ListNode, type: str = None) -> List:
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
