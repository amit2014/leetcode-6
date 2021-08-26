"""leetcode-MySQL-Schema-loader
"""

import os
import time
import sys
from typing import List
from selenium import webdriver
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

TEST_LINK_1 = 'https://leetcode.com/problems/second-highest-salary/'
TEST_LINK_2 = 'https://leetcode.com/problems/combine-two-tables/'
TEST_SCHEMA_1 = """
Create table If Not Exists UserActivity (username varchar(30), activity varchar(30), startDate date, endDate date)
Truncate table UserActivity
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-12', '2020-02-20')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Dancing', '2020-02-21', '2020-02-23')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-24', '2020-02-28')
insert into UserActivity (username, activity, startDate, endDate) values ('Bob', 'Travel', '2020-02-11', '2020-02-18')
"""

def get_SQL_schema_from_leetcode(link: str) -> str:
    """Extract the SQL schema from leetcode's website given a link.
    """

    #  https://sites.google.com/a/chromium.org/chromedriver/downloads
    #  You need to download and extract the right one and put it in your
    #  home directory, I used 92.
    path = os.path.expanduser(r'~/chromedriver')
    driver = webdriver.Chrome(executable_path = path)
    driver.get(link)
    driver.minimize_window()
    #  TODO(yrom1) A more elegant solution than time.sleep(n) involves checking
    #  if div is available repeatedly but this is good enough for now.  
    time.sleep(3)
    #  Finds the 'SQL Schema' button.
    sql_schema_button_wrapper = driver.find_element_by_class_name('sql-schema-wrapper__3VBi')
    #  Clicks it!
    sql_schema_button_link = driver.find_element_by_class_name('sql-schema-link__3cEg')
    sql_schema_button_link.click()
    time.sleep(2)
    #  This is the div on leetcode containing the actualy SQL schema text.
    sql_schema_div = driver.find_element_by_class_name('lc-modal-body__jO0c')
    return sql_schema_div.text


def remove_white_space(query):
    """Remove unnecessary white space from scrapped schema, if exists.
    """
    query_lines = query.split('\n')
    query_lines = [x.strip() for x in query_lines if x.strip() != '']
    return '\n'.join(query_lines)

def execute(command: str):
    """Execute an SQL command.
    """
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

def get_show_tables() -> List[str]:
    """
    """
    #  TODO(yrom1) this actually requires the leetcode database to exist
    #  because of how we create the conn
    tableList = []
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(f'show tables')
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

def delete_tables(table_list):
    for table in table_list:
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

def main() -> None:
    """
    Pass a leetcode database problem link to this script as the first
    argument. The SQL schema for this problem will be loaded into MySQL
    in an *already existing* database called leetcode. Anything already
    in the leetcode database will be purged so it's a clean playground.
    """
    #  TODO(yrom1) Redo this with argparse.
    try:
        link = sys.argv[1]
    except IndexError:
        print('Pass link to this script as the first argument.')
    dash = '-' * 10
    print(dash, 'loading link')
    schema = get_SQL_schema_from_leetcode(link)
    execute('use leetcode')
    print(dash, 'successfully connected to MySQL leetcode db!')
    delete_tables(get_show_tables())
    schema = remove_white_space(schema)
    print(dash, 'successfully downloaded SQL Schema!')
    print(dash, 'recreating schema in MySQL\'s leetcode database')
    for cmd in schema.split('\n'):
        print('Executing:', cmd)
        execute(cmd)
    print(dash, 'finished without errors!')

if __name__ == '__main__':
    main()
