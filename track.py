"""Track how many questions are left."""
import re
import tokenize

p = re.compile(r".*https://leetcode.com/.*")
with open("leetcode.py") as f:
    count = 0
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        if token_type == tokenize.COMMENT and p.match(line):
            print(line.strip().replace("# - ", ""))
            count += 1

with open(".leetcode.py") as f:
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        if token_type == tokenize.COMMENT and len(token_type) > 50:  # type: ignore
            print(line)

# print(f"{count=}/75")
