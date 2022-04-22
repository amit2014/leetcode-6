import re
from itertools import zip_longest
from typing import *


def chunker(iterable, n, fillvalue=None):
    """
    >>> [i for i in chunker(iter((1,2,3,4,5)), 2)]
    [(1, 2), (3, 4), (5, None)]
    """
    return zip_longest(*([iter(iterable)] * n), fillvalue=fillvalue)


with open("leetcode.sql", "r") as f:
    lines = f.readlines()

pa = re.compile(r"\/\*")
pb = re.compile(r"\d+\.[ \w-]+")
pc = re.compile(r"(https[\w\:\\\/\.-]*\b)")

for a, b, c in chunker(lines, 3):
    if (
        a is not None
        and b is not None
        and c is not None
        and not pa.search(a)
        and pb.search(b)
        and pc.search(c)
    ):
        print(c.strip()[3:])
