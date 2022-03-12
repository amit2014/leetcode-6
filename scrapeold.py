"""Track how many questions are left."""
import re
import tokenize
docs = []
with open("leetcode.py") as f:
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        # print(token_type, _, line)
        if token_type == 3 and len(line) > 100:
            docs.append(line)

doc_lines = [doc.splitlines() for doc in docs]

titles = []
for doc_line in doc_lines:
    if (title := doc_line[1].strip()).startswith('#'):
        titles.append(title)

