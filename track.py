"""Track how many questions are left."""
import re
import tokenize

p = re.compile(r".*https://leetcode.com/.*")
with open("main.py") as f:
    count = 0
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        if token_type == tokenize.COMMENT and p.match(line):
            count += 1
print(f"{count=}/75")
