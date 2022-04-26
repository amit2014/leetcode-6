# load.py
Load Leetcode's SQL Schema into your MySQL database in ~~one~~ two commands
(you may have to hit enter if there's a captcha):

    Typical usage example:

    $ py load.py https://leetcode.com/problems/report-contiguous-dates
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
4) Because filling out captchas is really annoying (althought it only happens
    every once in a while for me) they are cached in a folder called `schemas`.

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

# make_tree.py
Display a binary tree from a BFS serialized array (LeetCode style).

    Typical usage example:

    $ py make_tree.py [3,9,8,4,0,1,7,null,null,null,2,5]
                             3
                 9                       8
           4           0           1           7
                          2     5
