"""leetcode-MySQL-Schema-loader
"""

import os
import time
import sys
from typing import List, Dict
from selenium import webdriver
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

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


def read_db_config(filename: str = 'config.ini',
                   section: str = 'mysql') -> Dict[str, str]:
    """Read database .ini config file, and returns a config dictionary.

    Args:
        filename:
            name of the configuration file
        section:
            section of database configuration
    Returns:
        A dict of database parameters.
    Raises:
        Exception: If mysql section not found in config.ini file.
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f'{section} not found in the {filename}')

    return db


def get_SQL_schema_from_leetcode(link: str) -> str:
    """Extract the SQL schema from leetcode's website given a link.

    Args:
        link: Full link to leetcode database problem.
    Returns:
        The SQL schema for that leetcode database problem from the given link.
    """

    #  https://sites.google.com/a/chromium.org/chromedriver/downloads
    #  You need to download and extract the right one and put it in your
    #  home directory, I used 92.

    #  TODO(yrom1) Make this platform neutral.
    path = os.path.expanduser(r'~/chromedriver')
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)
    #  TODO(yrom1) Automate login.
    input('Please login to your leetcode account if prompted, then press enter.')
    driver.minimize_window()
    sql_schema_button_link = driver.find_element_by_link_text('SQL Schema')
    sql_schema_button_link.click()
    time.sleep(1)
    #  This is the div on leetcode containing the actualy SQL schema text.
    sql_schema_div = driver.find_element_by_class_name('lc-modal-body__jO0c')
    return sql_schema_div.text


def remove_white_space(query: str) -> str:
    """Remove unnecessary white space from scrapped schema, if exists.
    
    Args:
        query: The SQL Schema for the leetcode problem as one string. 
    Returns:
        The SQL Schema with unnecessary space removed.
    """
    query_lines = query.split('\n')
    query_lines = [x.strip() for x in query_lines if x.strip() != '']
    return '\n'.join(query_lines)


def execute(command: str) -> None:
    """Execute an SQL command.

    Args:
        command: A string that contains a single SQL statement
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
    """Get a list of tables in the currently connected to database.

    Returns:
        A list of tables in the currently connected to database.
    """
    #  This actually requires the leetcode database to exist
    #  because of how we create the conn.
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


def delete_tables(table_list: List[str]) -> None:
    """Delete the tables in the leetcode database to reset it.

    Args:
        table_list: A list of tables in the leetcode database. 
    """
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


def main() -> None:
    """Pass a leetcode database problem link to this script as the first
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
    print(dash, 'succesfully loaded schema!')


if __name__ == '__main__':
    main()
