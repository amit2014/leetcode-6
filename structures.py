from __future__ import annotations

from typing import *  # type:ignore


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional[ListNode] = None,
    ):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, arr: List[int]):
        self.head = ListNode(arr[0])
        node = self.head
        for x in arr[1:]:
            node.next = ListNode(x)
            node = node.next

    def __str__(self) -> str:
        arr: List[int] = []
        node = self.head
        while node is not None:
            arr.append(node.val)
            node = node.next
        return "->".join([str(x) for x in arr])


# print(LinkedList([0, 1, 2]))
