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

p = re.compile(r"\d{1,4} \|")
p2 = re.compile(r"https\:\/\/.*\/\)")
p3 = re.compile(r"(\[.*?\])")
for link in links:
    if p.match(link):
        # print(link)
        m = p2.search(link)
        print(link[m.start() : m.end() - 1])  # type:ignore
    if m := p3.search(link):
        print(m.group(1)[1:-1])
