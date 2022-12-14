# load_schema.py
Load Leetcode's SQL Schema into your MySQL database in ~~one~~ two commands
(you may have to hit enter if there's a captcha):

    Typical usage example:

    $ py load_schema.py https://leetcode.com/problems/report-contiguous-dates
    in cache
    Create table If Not Exists Failed (fail_date date)
    [...]
    insert into Succeeded (success_date) values ('2019-01-06')
    Success ✨🍰✨

Requirements:
1) Have MySQL installed and create a database called `leetcode`.
2) Put your MySQL database connection and Leetcode details in `config.ini` (a
    lot of SQL questions are premium on Leetcode).
    NOTE:   I often forget to do this and see my password as `***` in Selenium.
            So update your password in config.ini!
            You can also use `git update-index --assume-unchanged config.ini` to
            have git not track the config with your passwords, etc...
3) Install the requirements.txt file
4) Because filling out captchas is really annoying (although it only happens
    every once in a while for me) they are cached in a folder called `schemas`.
    THIS FOLDER MUST EXIST!
5) Chrome must be up to date. You may need to manually update it.

The `config.ini` should look like this:

    [mysql]
    host = localhost
    database = leetcode
    user = root
    password = password

    [leetcode]
    user = yrom1
    password = ...


---

# testcase.py
Loads failed SQL testcase JSON into your MySQL database.

    Typical usage example:

    Step 0) Have the appropriate schema loaded for the failed testcase. I
    assume you already have the schema loaded, or else why would you have
    the testcase!
    Step 1) Save failed testcase JSON in a file named 'testcase.json'.
    Step 2) $ py testcase.py


---

# make_tree.py
Display a binary tree from a BFS serialized array (LeetCode style).

    Typical usage example:

    $ py make_tree.py [3,9,8,4,0,1,7,null,null,null,2,5]
                             3
                 9                       8
           4           0           1           7
                          2     5


---

# title_to_link.py
Turn leetcode title into leetcode link.

    Typical usage example:
        $ py title_to_link.py Median Employee Salary
        https://leetcode.com/problems/median-employee-salary/
