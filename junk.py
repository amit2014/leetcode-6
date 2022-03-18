import re
from bisect import *  # type:ignore
from collections import *  # type:ignore
from functools import *  # type:ignore
from heapq import *  # type:ignore
from itertools import *  # type:ignore
from math import *  # type:ignore
from typing import *  # type:ignore

from structures import ListNode
from structures import LinkedList

class _:
    def _(self, head: Optional[ListNode]) -> bool:
        """Maintain list method: O(n) time O(1) space"""

        def middleNode(head: ListNode) -> ListNode:
            slow = fast = head
            while fast.next and fast.next.next: # in a->b->c->d, want b
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(head: ListNode) -> ListNode:
            prev, curr = None, head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        mid = middleNode(head)
        tail = reverseList(mid.next) # reverse second half
        _head, _tail = head, tail
        ans = True
        while ans and _tail is not None:
            if _head.val != _tail.val:
                ans = False # don't early out so we can restore list
            _head = _head.next
            _tail = _tail.next
        mid.next = reverseList(tail) # restore list
        return ans

ll = LinkedList([0,1,2,1,0])
args = ll.head,
print(_()._(*args))
print(ll)
