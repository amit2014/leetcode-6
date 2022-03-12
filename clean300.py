from itertools import zip_longest


def chunked(it, n, fillvalue=None):
    return zip_longest(*([iter(it)] * n), fillvalue=fillvalue)


with open("top300.txt") as f:
    lines = f.readlines()

new = [line.strip() for line in lines if line.strip() != ""]


questions = list(chunked(new, 3))

questions_no_percent = [(question[0], question[2]) for question in questions]

with open("someREADME.md.txt", "r") as f:
    somereadme = f.readlines()

import re
p = re.compile("(\[[34\w \-\`\\(\)\\'\,]+\])(\(https\:\/\/leetcode\.com\/problems\/.*?\))")

q_links = {}
for line in somereadme:
    if (m := p.search(line)) != None:
        # print(line)
        q_links[m.group(1)[1:-1].strip()] = m.group(2)[1:-1].strip()


import tokenize
docs = []
with open("leetcode.py") as f:
    for token_type, *_, line in tokenize.generate_tokens(f.readline):
        # print(token_type, _, line)
        if token_type == 3 and len(line) > 100:
            docs.append(line)


count = 0
#print(question_links)
with open('new-leetcode.py', 'w')  as f:
    for q in questions_no_percent:
        num, title = q[0].split('.')
        try:
            link = q_links[title.strip()]
        except:
            print(title.strip())
            count += 1
            link = ''
        # print(num)
        tab = " " * 4
        f.write(f'class _{num}:\n')
        f.write(f'{tab}"""\n')
        f.write(f'{tab}# - {title.strip()} -\n')
        f.write(f'{tab}# {link}\n')
        f.write(f'{tab}"""\n')
        f.write(f'{tab}...\n')

print(count)
