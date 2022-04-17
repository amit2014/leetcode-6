# Schema Loader

Load Leetcode's SQL Schema into your MySQL database in one command:

# Example

```
$ py load.py https://leetcode.com/problems/report-contiguous-dates
in cache
Create table If Not Exists Failed (fail_date date)
Create table If Not Exists Succeeded (success_date date)
Truncate table Failed
insert into Failed (fail_date) values ('2018-12-28')
insert into Failed (fail_date) values ('2018-12-29')
insert into Failed (fail_date) values ('2019-01-04')
insert into Failed (fail_date) values ('2019-01-05')
Truncate table Succeeded
insert into Succeeded (success_date) values ('2018-12-30')
insert into Succeeded (success_date) values ('2018-12-31')
insert into Succeeded (success_date) values ('2019-01-01')
insert into Succeeded (success_date) values ('2019-01-02')
insert into Succeeded (success_date) values ('2019-01-03')
insert into Succeeded (success_date) values ('2019-01-06')
Success ✨🍰✨
```

# Requirements
1) Have MySQL installed and create a database called `leetcode`.
2) Put your MySQL database connection and Leetcode details in `config.ini` (a lot of SQL questions are premium on Leetcode).
3) Download the appropriate zip for `chromedriver` from [here](https://sites.google.com/chromium.org/driver/), and put the extracted `chromedriver` file in your home path (if you download the wrong version, Selenium will tell you which to download use instead).

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