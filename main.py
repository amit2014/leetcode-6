schema = """
Create table If Not Exists Employee (Id int, Company varchar(255), Salary int)
Truncate table Employee
insert into Employee (Id, Company, Salary) values ('1', 'A', '2341')
insert into Employee (Id, Company, Salary) values ('2', 'A', '341')
insert into Employee (Id, Company, Salary) values ('3', 'A', '15')
insert into Employee (Id, Company, Salary) values ('4', 'A', '15314')
insert into Employee (Id, Company, Salary) values ('5', 'A', '451')
insert into Employee (Id, Company, Salary) values ('6', 'A', '513')
insert into Employee (Id, Company, Salary) values ('7', 'B', '15')
insert into Employee (Id, Company, Salary) values ('8', 'B', '13')
insert into Employee (Id, Company, Salary) values ('9', 'B', '1154')
insert into Employee (Id, Company, Salary) values ('10', 'B', '1345')
insert into Employee (Id, Company, Salary) values ('11', 'B', '1221')
insert into Employee (Id, Company, Salary) values ('12', 'B', '234')
insert into Employee (Id, Company, Salary) values ('13', 'C', '2345')
insert into Employee (Id, Company, Salary) values ('14', 'C', '2645')
insert into Employee (Id, Company, Salary) values ('15', 'C', '2645')
insert into Employee (Id, Company, Salary) values ('16', 'C', '2652')
insert into Employee (Id, Company, Salary) values ('17', 'C', '65')
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def removeWhiteSpace(query):
    query_lines = query.split('\n')
    query_lines = [x.strip() for x in query_lines if x.strip() != '']
    return '\n'.join(query_lines)

def execute(command: str):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()
        
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def executeNoCommit(command: str):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(command)
        #conn.commit()
        
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def getTables():
    tableList = []
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute('show tables')
        row = cursor.fetchone()
        
        while row is not None:
            tableList.append(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
    
    return tableList

def deleteTables(tableList):
    for table in tableList:
        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute(f'drop table {table[0]}')
            conn.commit()
            
        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

def dash(func):
    def inner(*args, **kwargs):
        print('+' + "-" * (len(args[0]) - 2) + '+')
        func(*args, **kwargs)
        print('+' + "-" * (len(args[0]) - 2) + '+')
    return inner

@dash
def printer(input):
    print(input)

if __name__ == '__main__':
    # the database leetcode needs to exist before running the script
    execute('use leetcode')
    deleteTables(getTables())
    schema = removeWhiteSpace(schema)
    for cmd in schema.split('\n'):
        printer(cmd)
        execute(cmd)