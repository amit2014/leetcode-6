"""Track how many questions are left."""
import re
import tokenize
docs = []
with open("leetcode.py") as f:
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        # print(token_type, _, line)
        if token_type == 3 and len(line) > 100:
            print(line)
            docs.append(line)

doc_lines = [doc.splitlines() for doc in docs]

title_doc = {}
for doc_line in doc_lines:
    if (title := doc_line[1].strip()).startswith('#'):
        title_doc[title[4:-2]] = '\n'.join(doc_line)

for title in title_doc.values():
    print(title)
