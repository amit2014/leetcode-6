"""Paste testcase json into testcase.json and then run this script.
I assume you already have the schema loaded, or else why would you have the testcase!"""
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
