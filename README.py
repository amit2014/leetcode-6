import os
import subprocess


def file_contents(filename: str) -> str:
    with open(filename, "r") as f:
        ans = f.read()
    return ans.strip()

def shell_output(cmd: str, dir='.') -> str:
    cwd = os.getcwd()
    os.chdir(dir)
    try:
        subprocess.run(["rm", "TEMP"])
    except:
        pass
    subprocess.run(["touch", "TEMP"])
    with open("TEMP.sh", "w") as f:
        f.write(cmd + " >> TEMP 2>&1")
    subprocess.run(["bash", "TEMP.sh"])
    ans = file_contents("TEMP")
    #print("\n\n\n\n", ans)
    subprocess.run(["rm", "TEMP", "TEMP.sh"])
    os.chdir(cwd)
    return ans

EXAMPLE_LOAD_CMD = "py load.py https://leetcode.com/problems/report-contiguous-dates"
EXAMPLE_LOAD_OUTPUT = shell_output(EXAMPLE_LOAD_CMD)

README = f"""\
# Schema Loader

Load Leetcode's SQL Schema into your MySQL database in one command:

# Example

```
$ {EXAMPLE_LOAD_CMD}
{EXAMPLE_LOAD_OUTPUT}
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
```"""

with open('README.md', 'w') as f:
    f.write(README)
