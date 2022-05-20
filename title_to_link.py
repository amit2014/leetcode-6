"""Turn leetcode title into leetcode link.

    Typical usage example:
        $ py title_to_link.py Median Employee Salary
        https://leetcode.com/problems/median-employee-salary/
"""

import sys
from typing import List


def title_to_link(input: List[str]) -> str:
    return f"https://leetcode.com/problems/{'-'.join([x.lower() for x in input])}/"


if __name__ == "__main__":
    assert (
        title_to_link("Median Employee Salary".split())
        == "https://leetcode.com/problems/median-employee-salary/"
    )
    print(title_to_link(sys.argv[1:]))
