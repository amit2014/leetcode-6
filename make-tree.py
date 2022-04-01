"""Display a binary tree from a BFS serialized array (LeetCode style).

Typical usage example:

$ py make-tree.py [1,2]
      1
    2
"""

from __future__ import annotations

import sys
from collections import deque
from typing import *  # type:ignore


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root: Optional[TreeNode]) -> List[List[str]]:
    def get_depth(node):
        if not node:
            return 0
        return max(get_depth(node.left), get_depth(node.right)) + 1

    def insert_value(node, lo, hi, depth=0):
        if not node:
            return
        mid = (lo + hi) // 2
        output[depth][mid] = str(node.val)
        insert_value(node.left, lo, mid, depth + 1)
        insert_value(node.right, mid, hi, depth + 1)

    depth = get_depth(root)
    output = [[""] * (2**depth - 1) for _ in range(depth)]

    insert_value(root, 0, 2**depth - 1)
    return output


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue: Deque[TreeNode] = deque()
        queue.append(root)
        ans = ""
        while queue:
            node = queue.popleft()
            if not node:
                ans += "None,"
                continue
            ans += str(node.val) + ","
            queue.append(node.left)  # type: ignore
            queue.append(node.right)  # type: ignore
        return ans[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        ls: Final = data.split(",")
        root = TreeNode(int(ls[0]))
        queue: Deque[TreeNode] = deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != "None":
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != "None":
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root


def clean_leetcode(tree: str) -> str:
    """
    >>> clean_leetcode("[1,2,3,null,4]")
    '1,2,3,None,4,None,None'
    """
    arr = tree[1:-1].replace("null", "None").split(",")
    height, max_nodes = 0, 1
    while len(arr) > max_nodes:
        height += 1
        max_nodes = 2 ** (height + 1) - 1

    while len(arr) < max_nodes:
        arr.append("None")

    return ",".join(arr)


if __name__ == "__main__":
    # NOTE assuming max two digit inputs
    import doctest

    doctest.testmod()
    c = Codec()
    assert (
        c.serialize(c.deserialize("1,2,5,3,4,None,None,None,None,None,None"))
        == "1,2,5,3,4,None,None,None,None,None,None"
    )

    clean_tree = clean_leetcode(sys.argv[1])
    tree_layers = print_tree(c.deserialize(clean_tree))
    tree = "\n".join(
        [(" " * 4) + " ".join([f"{x:2}" for x in layer]) for layer in tree_layers]
    )
    print(tree)
