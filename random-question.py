"""Get a random question's docstring, should work 95% of the time ;^)."""
import random
import tokenize

with open("leetcode.py") as f:
    questions = []
    for info in tokenize.generate_tokens(f.readline):
        a, b, c, d, e = info
        if a == tokenize.STRING and len(b) > 30:  # ;^)
            questions.append(b)

print(random.choice(questions))
