# leetcode-MySQL-Schema-loader

Load Leetcode's SQL Schema into your MySQL database in one command!

# Example

```
$ chmod +x main.py
$ ./main.py https://leetcode.com/problems/second-highest-salary/
---------- loading link
---------- successfully connected to MySQL leetcode db!
---------- successfully downloaded SQL Schema!
---------- recreating schema in MySQL's leetcode database
Executing: Create table If Not Exists Employee (Id int, Salary int)
Executing: Truncate table Employee
Executing: insert into Employee (Id, Salary) values ('1', '100')
Executing: insert into Employee (Id, Salary) values ('2', '200')
Executing: insert into Employee (Id, Salary) values ('3', '300')
---------- finished without errors!
```

# Requirements
1) Have MySQL installed and create a database called `leetcode`.
2) Put your MySQL database connection and Leetcode details in `config.ini` (a lot of SQL questions are premium on Leetcode).
3) Download the appropriate zip for `chromedriver` from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads), and put the extracted `chromedriver` file in your home path (if you download the wrong version, Selenium will tell you which to download use instead).  

The `config.ini` should look like this:
```
[mysql]
host = localhost
database = leetcode
user = root
password = password

[leetcode]
user = yrom1
password = ...
```
