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
        row = row.replace("[", "(")
        row = row.replace("]", ")")
        command += f"insert into {table} values {row};\n"  # TODO column names
# print(command)

from main import list_execute

commands = command.splitlines()
list_execute(commands)
