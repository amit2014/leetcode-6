"""Loads failed SQL testcase JSON into your MySQL database.

    Typical usage example:

    Step 0) Have the appropriate schema loaded for the failed testcase. I
    assume you already have the schema loaded, or else why would you have
    the testcase!
    Step 1) Save failed testcase JSON in a file named 'testcase.json'.
    Step 2) $ py testcase.py
"""

import json

with open("testcase.json", "r") as f:
    input = f.read()
    input = input.rstrip()
    input = json.loads(input)

command = ""
for table in list(input["headers"].keys()):
    rows = input["rows"][table]
    command += f"truncate table {table};\n"
    for row in rows:
        row = repr(row)
        row = row.replace("None", "null")
        row = row.replace("[", "(")
        row = row.replace("]", ")")
        command += f"insert into {table} values {row};\n"  # TODO column names
# print(command)

from load_schema import execute

# with open('testoutput.txt', 'r') as f:
#     cmds = f.read()
# commands = cmds.splitlines()

commands = command.splitlines()
execute(commands)
