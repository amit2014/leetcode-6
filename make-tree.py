from __future__ import annotations

from collections import deque
import sys
from typing import *


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


class Printer:
    def print_tree(self, root: Optional[TreeNode]) -> List[List[str]]:
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

if __name__ == '__main__':
    c = Codec()
    assert (
        c.serialize(c.deserialize("1,2,5,3,4,None,None,None,None,None,None"))
        == "1,2,5,3,4,None,None,None,None,None,None"
    )
    tree_layers = Printer().print_tree(c.deserialize(sys.argv[1]))
    tree = '\n'.join(['  '.join(layer) for layer in tree_layers])
    print(tree)
    # TODO leetcode posts trees like [1,2] when it should be [1,2,None]
    # NOTE assuming max two digit inputs
