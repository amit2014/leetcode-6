def addSemicolonsToSchema(query):
    """
    This program takes the SQL Schema as input and adds semicolons to the end of the lines.
    This lets your run the commands in terminal in one go.
    """
    query_lines = query.split('\n')
    for line in query_lines:
        if line == '':
            query_lines.remove('')
    i = 0
    for line in query_lines:    
        query_lines[i] = line + ';' + '\n'
        i += 1
    return ''.join(query_lines)

query = """
Create table If Not Exists Failed (fail_date date)
Create table If Not Exists Succeeded (success_date date)
Truncate table Failed
insert into Failed (fail_date) values ('2018-12-28')
Truncate table Succeeded
insert into Succeeded (success_date) values ('2018-12-30')
"""
print(addSemicolonsToSchema(query))