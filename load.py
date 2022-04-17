#!/usr/bin/env -S python3 -W ignore::DeprecationWarning
"""leetcode-MySQL-Schema-loader"""

import os
import re
import sys
import time
from configparser import ConfigParser
from pathlib import Path
from typing import Dict, List, Union

import selenium
from mysql.connector import Error, MySQLConnection
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

TEST_LINK_1 = "https://leetcode.com/problems/second-highest-salary/"
TEST_LINK_2 = "https://leetcode.com/problems/combine-two-tables/"
TEST_SCHEMA_1 = """
Create table If Not Exists UserActivity (username varchar(30), activity varchar(30), startDate date, endDate date)
Truncate table UserActivity
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-12', '2020-02-20')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Dancing', '2020-02-21', '2020-02-23')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-24', '2020-02-28')
insert into UserActivity (username, activity, startDate, endDate) values ('Bob', 'Travel', '2020-02-11', '2020-02-18')
"""


def read_config(filename: str = "config.ini", section: str = "mysql") -> Dict[str, str]:
    """Read .ini config file, and returns a config dictionary.

    Args:
        filename:
            name of the configuration file
        section:
            which part of ini file to parse
    Returns:
        A dict of parameters.
    Raises:
        Exception: If section not found in config.ini file.
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f"{section} not found in the {filename}")

    return db


def get_SQL_schema_from_leetcode(link: str, username: str, password: str) -> str:
    """Extract the SQL schema from leetcode's website given a link.

    Args:
        link: Full link to leetcode database problem.
    Returns:
        The SQL schema for that leetcode database problem from the given link.
    """

    #  https://sites.google.com/a/chromium.org/chromedriver/downloads
    #  You need to download and extract the right one and put it on your path

    # TODO remove sleeps with waits for elements
    path = os.path.expanduser(r"~/chromedriver")
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)
    # driver.minimize_window()
    try:
        WebDriverWait(driver, 10).until(
            lambda s: s.find_element_by_id("id_login").is_displayed()
        )
        textUserName = driver.find_element_by_id("id_login")
        textUserName.clear()
        textUserName.send_keys(username)
        WebDriverWait(driver, 10).until(
            lambda s: s.find_element_by_id("id_password").is_displayed()
        )
        textPassword = driver.find_element_by_id("id_password")
        textPassword.clear()
        textPassword.send_keys(password)
        textPassword.send_keys(Keys.RETURN)
        input("do captcha then hit ENTER")
        textPassword = driver.find_element_by_id("id_password")
        textPassword.send_keys(Keys.RETURN)
        time.sleep(3)
    except selenium.common.exceptions.TimeoutException:
        pass
    sql_schema_button_link = driver.find_element_by_link_text("SQL Schema")
    sql_schema_button_link.click()
    time.sleep(3)
    sql_schema_div = driver.find_element_by_class_name("lc-modal-body__jO0c")
    return sql_schema_div.text


def remove_white_space(query: str) -> str:
    """Remove unnecessary white space from scrapped schema, if exists.

    Args:
        query: The SQL Schema for the leetcode problem as one string.
    Returns:
        The SQL Schema with unnecessary space removed.
    """
    query_lines = query.split("\n")
    query_lines = [x.strip() for x in query_lines if x.strip() != ""]
    return "\n".join(query_lines)


def execute(command: Union[str, List[str]]) -> None:
    """Execute one or many SQL non parameterized command(s).

    Args:
        command: A string or list of strings that contains a single SQL statement(s)
    """

    def swap_None_to_null(command: str) -> str:
        """For some reason leetcode put null as 'None' in multiple questions
        so here is the hotfix."""
        null_command = re.sub("'None'", "null", command)
        if null_command != command:
            print(" " * 11 + "FOUND 'None' in Schema, replacing with null:")
            print("Executing:", null_command)
        return null_command

    try:
        dbconfig = read_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        if isinstance(command, str):
            null_command = swap_None_to_null(command)
            cursor.execute(null_command)
            conn.commit()

        elif isinstance(command, list):
            for cmd in command:
                null_command = swap_None_to_null(cmd)
                cursor.execute(null_command)
            conn.commit()
        else:
            raise ValueError("Expected str or list[str].")

    except Error as e:
        if not None:
            print(f"{command=}")
        raise e

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
        dbconfig = read_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(f"show tables")
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
            dbconfig = read_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute(f"drop table {table[0]}")
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

    link = sys.argv[1]

    execute("use leetcode")
    delete_tables(get_show_tables())

    name = link[link.find("problems") + len("problems") + 1 :]

    if name in [file.stem for file in list((Path(".") / "schemas").glob("*"))]:
        print("in cache")
        with open(f"./schemas/{name}", "r") as f:
            schema = f.read()
    else:
        print("not in cache")
        login_info = read_config("config.ini", "leetcode")
        schema = get_SQL_schema_from_leetcode(
            link, login_info["user"], login_info["password"]
        )
        schema = remove_white_space(schema)
        with open(f"./schemas/{name}", "w") as f:
            f.write(schema)

    for cmd in schema.split("\n"):
        print(cmd)
        execute(cmd)


if __name__ == "__main__":
    try:
        main()
        print("Success ✨🍰✨")
    except IndexError:
        print("Pass link to this script as the first argument")
