from datetime import datetime
from math import ceil

PYTHON_QUESTIONS_SOLVED = (
    162  # automate this if you're feeling cheeky and *extremely* bored
)
PYTHON_QUESTIONS_GOAL = 300
PYTHON_QUESTIONS_LEFT = PYTHON_QUESTIONS_GOAL - PYTHON_QUESTIONS_SOLVED
TODAY = datetime.now()
GOAL_DATE = datetime(year=2022, month=12, day=31) # EOY
DAYS_LEFT = (GOAL_DATE - TODAY).days
WEEKS_LEFT = DAYS_LEFT / 7
QUESTIONS_PER_WEEK = ceil(PYTHON_QUESTIONS_LEFT / WEEKS_LEFT)
print(f"{DAYS_LEFT=}, {WEEKS_LEFT=}, {PYTHON_QUESTIONS_LEFT=}, {QUESTIONS_PER_WEEK=}")
