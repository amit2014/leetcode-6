from itertools import zip_longest


def chunked(it, n, fillvalue=None):
    return zip_longest(*([iter(it)] * n), fillvalue=fillvalue)


with open("top300.txt") as f:
    lines = f.readlines()

new = [line.strip() for line in lines if line.strip() != ""]


questions = list(chunked(new, 3))

questions_no_percent = [(question[0], question[2]) for question in questions]

with open("someREADME.md.txt", "r") as f:
    links = f.readlines()

import re

question_links = {}
p = re.compile(r"\d{1,4} \|")
p2 = re.compile(r"https\:\/\/.*\/\)")
p3 = re.compile(r"(\[.*?\])")
for link in links:
    item = []
    if p.match(link):
        # print(link)
        m = p2.search(link)
        item.append(link[m.start() : m.end() - 1])
    if m := p3.search(link):
        item.append(m.group(1)[1:-1])
    if len(item) == 2:
        question_links[item[1].strip()] = item[0].strip()

count = 0
#print(question_links)
with open('new-leetcode.py', 'w')  as f:
    for q in questions_no_percent:
        num, title = q[0].split('.')
        try:
            link = question_links[title.strip()]
        except:
            count += 1
            link = ''
        # print(num)
        tab = " " * 4
        f.write(f'class _{num}:\n')
        f.write(f'{tab}"""\n')
        f.write(f'{tab}# - {title.strip()} -\n')
        f.write(f'{tab}# {link}\n')
        f.write(f'{tab}"""\n')

print(count)
