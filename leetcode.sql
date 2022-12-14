/*
176. Second Highest Salary (Easy)
-- https://leetcode.com/problems/second-highest-salary/
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/

SELECT (
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1, 1
) SecondHighestSalary;

/*
177. Nth Highest Salary (Medium)
-- https://leetcode.com/problems/nth-highest-salary/
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
RETURN (
    SELECT (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1)
);
END;

-- This is an example that actually runs in MySQL:
/*
DELIMITER $$
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
READS SQL DATA
BEGIN
DECLARE M INT;
SET M = N - 1;
RETURN (
    SELECT (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1)
);
END$$
DELIMITER ;
*/

/*
175. Combine Two Tables (Easy)
-- https://leetcode.com/problems/combine-two-tables/
Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output:
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation:
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.
*/

SELECT FirstName
    , LastName
    , City
    , State
FROM Person p
    LEFT JOIN Address a
        ON p.PersonId = a.PersonId;

/*
181. Employees Earning More Than Their Managers (Easy)
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
*/

SELECT e1.Name Employee
FROM Employee e1
    LEFT JOIN Employee e2
        ON e1.ManagerId = e2.Id
WHERE e1.Salary > e2.Salary;

SELECT Name Employee
FROM Employee e
WHERE e.ManagerId IS NOT NULL
    AND e.Salary > (
        SELECT Salary
        FROM Employee
        WHERE e.ManagerId = id
    );

/*
185. Department Top Three Salaries (Hard)
-- https://leetcode.com/problems/department-top-three-salaries/
A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write an SQL query to find the employees who are high earners in each of the departments.

Return the result table in any order.

The query result format is in the following example:

Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| Id | Name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Result table:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees
*/

SELECT d.Name Department
    , e1.Name Employee
    , e1.Salary
FROM Department d
    INNER JOIN Employee e1
        ON d.Id = e1.DepartmentId
WHERE (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary
        AND e1.DepartmentId = e2.DepartmentId
) < 3;

/*
1757. Recyclable and Low Fat Products (Easy)
-- https://leetcode.com/problems/recyclable-and-low-fat-products/
Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The query result format is in the following example:

Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Result table:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Only products 1 and 3 are both low fat and recyclable.
*/


SELECT product_id
FROM Products
WHERE low_fats = 'Y'
    AND recyclable = 'Y';

/*
184. Department Highest Salary (Medium)
-- https://leetcode.com/problems/department-highest-salary/
Write an SQL query to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
*/

SELECT d.name Department
    , e.name Employee
    , e.salary
FROM Employee e
    INNER JOIN Department d
        ON e.departmentId = d.Id
WHERE (departmentId, salary) IN (
    SELECT departmentId
        , MAX(salary)
    FROM Employee
    GROUP BY departmentId
    );

/*
180. Consecutive Numbers (Medium)
-- https://leetcode.com/problems/consecutive-numbers/
Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example:

Logs table:
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Result table:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
1 is the only number that appears consecutively for at least three times.
*/

SELECT DISTINCT L1.Num ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE L1.Id = L2.Id - 1
    AND L2.Id = L3.Id - 1
    AND L1.Num = L2.Num
    AND L2.Num = L3.Num;

-- NOTE A user-defined variable can hold a single value only. If the SELECT
--      statement returns multiple values, the variable will take the value
--      of the last row in the result.

SELECT DISTINCT Num ConsecutiveNums
FROM (
    SELECT Num
    , @counter := IF(@prev = Num, @counter + 1, 1) how_many_cnt_in_a_row
    , @prev := Num
    FROM Logs y, (SELECT @counter := 1, @prev := NULL) vars
) temp
WHERE how_many_cnt_in_a_row >= 3;

/*
178. Rank Scores (Medium)
-- https://leetcode.com/problems/rank-scores/
Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:
* The scores should be ranked from the highest to the lowest.
* If there is a tie between two scores, both should have the same ranking.
* After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by score in descending order.

The query result format is in the following example.

Example 1:

Input:
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output:
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/

SELECT Score
    , DENSE_RANK() OVER (ORDER BY Score DESC) Rank
FROM Scores;

/*
1412. Find the Quiet Students in All Exams (Hard)
-- https://leetcode.com/problems/find-the-quiet-students-in-all-exams/
A "quite" student is the one who took at least one exam and didn't score neither the high score nor the low score.

Write an SQL query to report the students (student_id, student_name) being "quiet" in ALL exams.

Don't return the student who has never taken any exam. Return the result table ordered by student_id.

The query result format is in the following example.

Student table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
| 3           | Stella        |
| 4           | Jonathan      |
| 5           | Will          |
+-------------+---------------+

Exam table:
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
| 20         |     1        |    80     |
| 30         |     1        |    70     |
| 30         |     3        |    80     |
| 30         |     4        |    90     |
| 40         |     1        |    60     |
| 40         |     2        |    70     |
| 40         |     4        |    80     |
+------------+--------------+-----------+

Result table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+

For exam 1: Student 1 and 3 hold the lowest and high score respectively.
For exam 2: Student 1 hold both highest and lowest score.
For exam 3 and 4: Studnet 1 and 4 hold the lowest and high score respectively.
Student 2 and 5 have never got the highest or lowest in any of the exam.
Since student 5 is not taking any exam, he is excluded from the result.
So, we only return the information of Student 2.
*/
/* query student_id student_name
students took at least one exam
did not score highest
did not score lowest
order by student_id */

WITH cte as (
SELECT s.student_id
    , student_name
    , RANK() OVER (PARTITION BY exam_id ORDER BY SCORE) low
    , RANK() OVER (PARTITION BY exam_id ORDER BY SCORE DESC) high
FROM Exam e
    INNER JOIN Student s
        ON s.student_id = e.student_id
)
SELECT student_id
    , any_value(student_name)
FROM cte
GROUP BY 1
HAVING MIN(low) > 1
    AND MIN(high) > 1
ORDER BY 1;

/*
610. Triangle Judgement (Easy)
-- https://leetcode.com/problems/triangle-judgement/
A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.

However, this assignment is very heavy because there are hundreds of records to calculate.

Could you help Tim by writing a query to judge whether these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.

| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |
For the sample data above, your query should return the follow result:
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
*/

SELECT x
    , y
    , z
    /* triangle inequality, assuming area_triangle > 0 */
    , CASE WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes' ELSE 'No' END AS triangle
FROM triangle;

/*
262. Trips and Users (Hard)
-- https://leetcode.com/problems/trips-and-users/
Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03".

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Return the result table in any order. Round Cancellation Rate to two decimal points.

The query result format is in the following example:

Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| Id | Client_Id | Driver_Id | City_Id | Status              | Request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+

Users table:
+----------+--------+--------+
| Users_Id | Banned | Role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+

Result table:
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+

On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50
*/

SELECT Request_at Day
    , ROUND(COUNT(IF(Status REGEXP '^cancelled', TRUE, NULL)) / COUNT(*), 2) `Cancellation Rate`
FROM Trips
WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND Driver_Id NOT IN (
        SELECT Users_Id
        FROM Users
        WHERE Banned = 'Yes'
    )
    AND Client_Id NOT IN (
        SELECT Users_Id
        FROM Users
        WHERE Banned = 'Yes'
    )
GROUP BY Request_at;

/*
597. Friend Requests I: Overall Acceptance Rate (Easy)
-- https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/

Write an SQL query to find the overall acceptance rate of requests, which is the number of acceptance divided by the number of requests. Return the answer rounded to 2 decimals places.

Note that:

The accepted requests are not necessarily from the table friend_request. In this case, Count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ???duplicated??? requests or acceptances are only counted once.
If there are no requests at all, you should return 0.00 as the accept_rate.
The query result format is in the following example.

Example 1:

Input:
FriendRequest table:
+-----------+------------+--------------+
| sender_id | send_to_id | request_date |
+-----------+------------+--------------+
| 1         | 2          | 2016/06/01   |
| 1         | 3          | 2016/06/01   |
| 1         | 4          | 2016/06/01   |
| 2         | 3          | 2016/06/02   |
| 3         | 4          | 2016/06/09   |
+-----------+------------+--------------+
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
| 3            | 4           | 2016/06/10  |
+--------------+-------------+-------------+
Output:
+-------------+
| accept_rate |
+-------------+
| 0.8         |
+-------------+
Explanation:
There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.

Follow up:
Could you write a query to return the acceptance rate for every month?
Could you write a query to return the cumulative acceptance rate for every day?
*/
SELECT ROUND(IFNULL(
    (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) temp)
    /
    (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) temp)
    , 0)
    , 2) accept_rate;

/*
1270. All People Report to the Given Manager (Medium)
-- https://leetcode.com/problems/all-people-report-to-the-given-manager

Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.

The indirect relation between managers will not exceed three managers as the company is small.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employees table:
+-------------+---------------+------------+
| employee_id | employee_name | manager_id |
+-------------+---------------+------------+
| 1           | Boss          | 1          |
| 3           | Alice         | 3          |
| 2           | Bob           | 1          |
| 4           | Daniel        | 2          |
| 7           | Luis          | 4          |
| 8           | Jhon          | 3          |
| 9           | Angela        | 8          |
| 77          | Robert        | 1          |
+-------------+---------------+------------+
Output:
+-------------+
| employee_id |
+-------------+
| 2           |
| 77          |
| 4           |
| 7           |
+-------------+
Explanation:
The head of the company is the employee with employee_id 1.
The employees with employee_id 2 and 77 report their work directly to the head of the company.
The employee with employee_id 4 reports their work indirectly to the head of the company 4 --> 2 --> 1.
The employee with employee_id 7 reports their work indirectly to the head of the company 7 --> 4 --> 2 --> 1.
The employees with employee_id 3, 8, and 9 do not report their work to the head of the company directly or indirectly.
*/
SELECT a.employee_id
FROM Employees a
    INNER JOIN Employees b
    INNER JOIN Employees c
        ON a.manager_id = b.employee_id
            AND b.manager_id = c.employee_id
WHERE c.manager_id = 1
    AND a.employee_id != 1;

/*
1179. Reformat Department Table (Easy)
-- https://leetcode.com/problems/reformat-department-table
Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
Output:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
Explanation: The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months).
*/

select id
    , sum(case when month = 'jan' then revenue else null end) as Jan_Revenue
	, sum(case when month = 'feb' then revenue else null end) as Feb_Revenue
	, sum(case when month = 'mar' then revenue else null end) as Mar_Revenue
	, sum(case when month = 'apr' then revenue else null end) as Apr_Revenue
	, sum(case when month = 'may' then revenue else null end) as May_Revenue
	, sum(case when month = 'jun' then revenue else null end) as Jun_Revenue
	, sum(case when month = 'jul' then revenue else null end) as Jul_Revenue
	, sum(case when month = 'aug' then revenue else null end) as Aug_Revenue
	, sum(case when month = 'sep' then revenue else null end) as Sep_Revenue
	, sum(case when month = 'oct' then revenue else null end) as Oct_Revenue
	, sum(case when month = 'nov' then revenue else null end) as Nov_Revenue
	, sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from department
group by id
order by id;

/*
196. Delete Duplicate Emails (Easy)
-- https://leetcode.com/problems/delete-duplicate-emails

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
*/
-- the goal is to avoid an error where you delete based on yourself while deleting
-- ERROR 1093 (HY000): You can't specify target table 'Person' for update in FROM clause

delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id;

delete from Person where id not in (
    select t.id from ( -- sauce, explicit temp table creation
        select min(id) as id
        from Person
        group by email
    ) t
);

/*
626. Exchange Seats (Medium)
-- https://leetcode.com/problems/exchange-seats/
Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation:
Note that if the number of students is odd, there is no need to change the last one's seat.
*/

SELECT
    CASE
        WHEN id mod 2 != 0 AND records != id THEN id + 1
        WHEN id mod 2 != 0 AND records = id THEN id
        ELSE id - 1
    END id
    , student
FROM seat, (SELECT COUNT(*) records FROM seat) seat_records
ORDER BY id ASC;

/*
1225. Report Contiguous Dates (Hard)
-- https://leetcode.com/problems/report-contiguous-dates
A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

Return the result table ordered by start_date.

The query result format is in the following example.

Example 1:

Input:
Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+
Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+
Output:
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+
Explanation:
The report ignored the system state in 2018 as we care about the system in the period 2019-01-01 to 2019-12-31.
From 2019-01-01 to 2019-01-03 all tasks succeeded and the system state was "succeeded".
From 2019-01-04 to 2019-01-05 all tasks failed and the system state was "failed".
From 2019-01-06 to 2019-01-06 all tasks succeeded and the system state was "succeeded".
*/
/*
query
| period_state | start_date   | end_date     |
every continuous interval (grouped days by success/failure)
    between 2019-01-01 to 2019-12-31
*/

WITH t AS (
SELECT fail_date day
    , 'failed' status
    , RANK() OVER (ORDER BY fail_date) rank_date
FROM Failed
WHERE fail_date BETWEEN '2019-01-01'
    AND '2019-12-31'
UNION -- WHY NOT UNION ALL
SELECT success_date day
    , 'succeeded' status
    , RANK() OVER (ORDER BY success_date) rank_date
FROM Succeeded
WHERE success_date BETWEEN '2019-01-01'
    AND '2019-12-31'
), q as (
SELECT *
    , RANK() OVER (ORDER BY day) - rank_date delta_increase_rate
FROM t
)
SELECT status period_state
    , MIN(day) start_date
    , MAX(day) end_date
FROM q
GROUP BY delta_increase_rate, status
ORDER BY start_date;

/*
615. Average Salary: Departments VS Company (Hard)
-- https://leetcode.com/problems/average-salary-departments-vs-company/
Write an SQL query to report the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Salary table:
+----+-------------+--------+------------+
| id | employee_id | amount | pay_date   |
+----+-------------+--------+------------+
| 1  | 1           | 9000   | 2017/03/31 |
| 2  | 2           | 6000   | 2017/03/31 |
| 3  | 3           | 10000  | 2017/03/31 |
| 4  | 1           | 7000   | 2017/02/28 |
| 5  | 2           | 6000   | 2017/02/28 |
| 6  | 3           | 8000   | 2017/02/28 |
+----+-------------+--------+------------+
Employee table:
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
+-------------+---------------+
Output:
+-----------+---------------+------------+
| pay_month | department_id | comparison |
+-----------+---------------+------------+
| 2017-02   | 1             | same       |
| 2017-03   | 1             | higher     |
| 2017-02   | 2             | same       |
| 2017-03   | 2             | lower      |
+-----------+---------------+------------+
Explanation:
In March, the company's average salary is (9000+6000+10000)/3 = 8333.33...
The average salary for department '1' is 9000, which is the salary of employee_id '1' since there is only one employee in this department. So the comparison result is 'higher' since 9000 > 8333.33 obviously.
The average salary of department '2' is (6000 + 10000)/2 = 8000, which is the average of employee_id '2' and '3'. So the comparison result is 'lower' since 8000 < 8333.33.

With he same formula for the average salary comparison in February, the result is 'same' since both the department '1' and '2' have the same average salary with the company, which is 7000.
*/

/*
query
| pay_month | department_id | comparison  |
    compare avg sal of each department to company average
    each dept. each month
*/

-- TODO why can we partition by the pay_date, cant people be paid at different times

WITH cte AS(
SELECT s.employee_id,
    department_id,
    SUBSTRING(pay_date, 1, 7) AS pay_month,
    AVG(amount) OVER(PARTITION BY pay_date, department_id) AS avg_department_salary,
    AVG(amount) OVER(PARTITION BY pay_date) AS avg_company_salary
FROM salary s
    INNER JOIN employee e
        ON s.employee_id = e.employee_id
)
SELECT DISTINCT pay_month
    , department_id
    , CASE
        WHEN avg_department_salary > avg_company_salary THEN 'higher'
        WHEN avg_department_salary < avg_company_salary THEN 'lower'
        WHEN avg_department_salary = avg_company_salary THEN 'same'
    END comparison
FROM cte;

/*
1511. Customer Order Frequency (Easy)
-- https://leetcode.com/problems/customer-order-frequency
Write an SQL query to report the customer_id and customer_name of customers who have spent at least $100 in each month of June and July 2020.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+--------------+-----------+-------------+
| customer_id  | name      | country     |
+--------------+-----------+-------------+
| 1            | Winston   | USA         |
| 2            | Jonathan  | Peru        |
| 3            | Moustafa  | Egypt       |
+--------------+-----------+-------------+
Product table:
+--------------+-------------+-------------+
| product_id   | description | price       |
+--------------+-------------+-------------+
| 10           | LC Phone    | 300         |
| 20           | LC T-Shirt  | 10          |
| 30           | LC Book     | 45          |
| 40           | LC Keychain | 2           |
+--------------+-------------+-------------+
Orders table:
+--------------+-------------+-------------+-------------+-----------+
| order_id     | customer_id | product_id  | order_date  | quantity  |
+--------------+-------------+-------------+-------------+-----------+
| 1            | 1           | 10          | 2020-06-10  | 1         |
| 2            | 1           | 20          | 2020-07-01  | 1         |
| 3            | 1           | 30          | 2020-07-08  | 2         |
| 4            | 2           | 10          | 2020-06-15  | 2         |
| 5            | 2           | 40          | 2020-07-01  | 10        |
| 6            | 3           | 20          | 2020-06-24  | 2         |
| 7            | 3           | 30          | 2020-06-25  | 2         |
| 9            | 3           | 30          | 2020-05-08  | 3         |
+--------------+-------------+-------------+-------------+-----------+
Output:
+--------------+------------+
| customer_id  | name       |
+--------------+------------+
| 1            | Winston    |
+--------------+------------+
Explanation:
Winston spent $300 (300 * 1) in June and $100 ( 10 * 1 + 45 * 2) in July 2020.
Jonathan spent $600 (300 * 2) in June and $20 ( 2 * 10) in July 2020.
Moustafa spent $110 (10 * 2 + 45 * 2) in June and $0 in July 2020.
*/
SELECT customer_id
    , name
FROM Customers
    INNER JOIN Orders USING(customer_id)
    INNER JOIN Product USING(product_id)
GROUP BY customer_id
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0) * price) >= 100
    AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0) * price) >= 100

/*
627. Swap Salary (Easy)
-- https://leetcode.com/problems/swap-salary
Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

The query result format is in the following example.

Example 1:

Input:
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
Output:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
Explanation:
(1, A) and (3, C) were changed from 'm' to 'f'.
(2, B) and (4, D) were changed from 'f' to 'm'.
*/

UPDATE Salary SET sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;
UPDATE Salary SET sex = IF(sex='m', 'f', 'm');

/*
569. Median Employee Salary (Hard)
-- https://leetcode.com/problems/median-employee-salary/
Write an SQL query to find the median salary of each company.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+----+---------+--------+
| id | company | salary |
+----+---------+--------+
| 1  | A       | 2341   |
| 2  | A       | 341    |
| 3  | A       | 15     |
| 4  | A       | 15314  |
| 5  | A       | 451    |
| 6  | A       | 513    |
| 7  | B       | 15     |
| 8  | B       | 13     |
| 9  | B       | 1154   |
| 10 | B       | 1345   |
| 11 | B       | 1221   |
| 12 | B       | 234    |
| 13 | C       | 2345   |
| 14 | C       | 2645   |
| 15 | C       | 2645   |
| 16 | C       | 2652   |
| 17 | C       | 65     |
+----+---------+--------+
Output:
+----+---------+--------+
| id | company | salary |
+----+---------+--------+
| 5  | A       | 451    |
| 6  | A       | 513    |
| 12 | B       | 234    |
| 9  | B       | 1154   |
| 14 | C       | 2645   |
+----+---------+--------+

Follow up: Could you solve it without using any built-in or window functions?
*/

/*
query
|Id   | Company    | Salary |
median salary of each company
*/

WITH cte AS (
SELECT *
    , ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC
    , ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
FROM Employee
)
SELECT Id
    , Company
    , Salary
FROM cte
WHERE ABS(CAST(RN_ASC AS SIGNED) - CAST(RN_DESC AS SIGNED)) BETWEEN 0 AND 1
ORDER BY Company, Salary;

/*
+------+---------+--------+--------+---------+-------------------------------------------------------+
| Id   | Company | Salary | RN_ASC | RN_DESC | ABS(CAST(RN_ASC AS SIGNED) - CAST(RN_DESC AS SIGNED)) |
+------+---------+--------+--------+---------+-------------------------------------------------------+
|    4 | A       |  15314 |      6 |       1 |                                                     5 |
|    1 | A       |   2341 |      5 |       2 |                                                     3 |
|    6 | A       |    513 |      4 |       3 |                                                     1 |
|    5 | A       |    451 |      3 |       4 |                                                     1 |
|    2 | A       |    341 |      2 |       5 |                                                     3 |
|    3 | A       |     15 |      1 |       6 |                                                     5 |
|   10 | B       |   1345 |      6 |       1 |                                                     5 |
|   11 | B       |   1221 |      5 |       2 |                                                     3 |
|    9 | B       |   1154 |      4 |       3 |                                                     1 |
|   12 | B       |    234 |      3 |       4 |                                                     1 |
|    7 | B       |     15 |      2 |       5 |                                                     3 |
|    8 | B       |     13 |      1 |       6 |                                                     5 |
|   16 | C       |   2652 |      5 |       1 |                                                     4 |
|   15 | C       |   2645 |      4 |       2 |                                                     2 |
|   14 | C       |   2645 |      3 |       3 |                                                     0 |
|   13 | C       |   2345 |      2 |       4 |                                                     2 |
|   17 | C       |     65 |      1 |       5 |                                                     4 |
+------+---------+--------+--------+---------+-------------------------------------------------------+
*/

/*
1164. Product Price at a Given Date (Medium)
-- https://leetcode.com/problems/product-price-at-a-given-date
Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
*/

SELECT product_id
    , new_price price
FROM Products
WHERE (product_id, change_date) IN (
    /* we are finding the latest change date for each product <= given date */
    SELECT product_id
        , MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION
SELECT product_id
    , 10 price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';

/*
1699. Number of Calls Between Two Persons (Medium)
-- https://leetcode.com/problems/number-of-calls-between-two-persons
Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Calls table:
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
Output:
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+
Explanation:
Users 1 and 2 had 2 calls and the total duration is 70 (59 + 11).
Users 1 and 3 had 1 call and the total duration is 20.
Users 3 and 4 had 4 calls and the total duration is 999 (100 + 200 + 200 + 499).
*/

SELECT IF(from_id < to_id, from_id, to_id) AS person1
    , IF(from_id < to_id, to_id, from_id) AS person2
    , COUNT(*) AS call_count
    , SUM(duration) AS total_duration
FROM Calls
GROUP BY person1, person2;

/*
1398. Customers Who Bought Products A and B but Not C (Medium)
-- https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c
Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+
Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
Output:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
Explanation: Only the customer_id with id 3 bought the product A and B but not the product C.
*/

/*
a few tricks, when chaining WHERE IN, do:
WHERE x IN (...) *AND* y IN (...)...
*/

SELECT customer_id
    , customer_name
FROM Customers
WHERE customer_id IN (
        SELECT customer_id
        FROM Orders
        WHERE product_name='A'
    )
    AND customer_id IN (
        SELECT customer_id
        FROM Orders
        WHERE product_name='B'
    )
    AND customer_id NOT IN (
        SELECT customer_id
        FROM Orders
        WHERE product_name='C'
    )
ORDER BY customer_id;

/*
1384. Total Sales Amount by Year (Hard)
-- https://leetcode.com/problems/total-sales-amount-by-year
Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

Return the result table ordered by product_id and report_year.

The query result format is in the following example.

Example 1:

Input:
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | LC Phone     |
| 2          | LC T-Shirt   |
| 3          | LC Keychain  |
+------------+--------------+
Sales table:
+------------+--------------+-------------+---------------------+
| product_id | period_start | period_end  | average_daily_sales |
+------------+--------------+-------------+---------------------+
| 1          | 2019-01-25   | 2019-02-28  | 100                 |
| 2          | 2018-12-01   | 2020-01-01  | 10                  |
| 3          | 2019-12-01   | 2020-01-31  | 1                   |
+------------+--------------+-------------+---------------------+
Output:
+------------+--------------+-------------+--------------+
| product_id | product_name | report_year | total_amount |
+------------+--------------+-------------+--------------+
| 1          | LC Phone     |    2019     | 3500         |
| 2          | LC T-Shirt   |    2018     | 310          |
| 2          | LC T-Shirt   |    2019     | 3650         |
| 2          | LC T-Shirt   |    2020     | 10           |
| 3          | LC Keychain  |    2019     | 31           |
| 3          | LC Keychain  |    2020     | 31           |
+------------+--------------+-------------+--------------+
Explanation:
LC Phone was sold for the period of 2019-01-25 to 2019-02-28, and there are 35 days for this period. Total amount 35*100 = 3500.
LC T-shirt was sold for the period of 2018-12-01 to 2020-01-01, and there are 31, 365, 1 days for years 2018, 2019 and 2020 respectively.
LC Keychain was sold for the period of 2019-12-01 to 2020-01-31, and there are 31, 31 days for years 2019 and 2020 respectively.
*/

-- TODO need to review this question

with recursive cte as(
select product_id
    , average_daily_sales
    , period_start
    , period_end
from Sales
UNION ALL
select product_id
    , average_daily_sales
    , date_add(period_start, interval 1 day) period_start
    , period_end
from cte
where period_start < period_end
)
select cte.product_id
    , p.product_name
    , date_format(cte.period_start, "%Y") report_year
    , count(cte.period_start) * any_value(cte.average_daily_sales) total_amount
from cte
    join Product p
        on p.product_id = cte.product_id
group by 1, 2, 3
order by 1, 3;

1336. Number of Transactions per Visit (Hard)
-- https://leetcode.com/problems/number-of-transactions-per-visit

/*
197. Rising Temperature (Easy)
-- https://leetcode.com/problems/rising-temperature
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation:
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
*/

SELECT w1.id Id
FROM weather w1
    INNER JOIN weather w2
        ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 -- do not use abs here
        AND w1.temperature > w2.temperature;

/*
1596. The Most Frequently Ordered Products for Each Customer (Medium)
-- https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer

Write an SQL query to find the most frequently ordered product(s) for each customer.

The result table should have the product_id and product_name for each customer_id who ordered at least one order.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+-------------+-------+
| customer_id | name  |
+-------------+-------+
| 1           | Alice |
| 2           | Bob   |
| 3           | Tom   |
| 4           | Jerry |
| 5           | John  |
+-------------+-------+
Orders table:
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | product_id |
+----------+------------+-------------+------------+
| 1        | 2020-07-31 | 1           | 1          |
| 2        | 2020-07-30 | 2           | 2          |
| 3        | 2020-08-29 | 3           | 3          |
| 4        | 2020-07-29 | 4           | 1          |
| 5        | 2020-06-10 | 1           | 2          |
| 6        | 2020-08-01 | 2           | 1          |
| 7        | 2020-08-01 | 3           | 3          |
| 8        | 2020-08-03 | 1           | 2          |
| 9        | 2020-08-07 | 2           | 3          |
| 10       | 2020-07-15 | 1           | 2          |
+----------+------------+-------------+------------+
Products table:
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
| 1          | keyboard     | 120   |
| 2          | mouse        | 80    |
| 3          | screen       | 600   |
| 4          | hard disk    | 450   |
+------------+--------------+-------+
Output:
+-------------+------------+--------------+
| customer_id | product_id | product_name |
+-------------+------------+--------------+
| 1           | 2          | mouse        |
| 2           | 1          | keyboard     |
| 2           | 2          | mouse        |
| 2           | 3          | screen       |
| 3           | 3          | screen       |
| 4           | 1          | keyboard     |
+-------------+------------+--------------+
Explanation:
Alice (customer 1) ordered the mouse three times and the keyboard one time, so the mouse is the most frequently ordered product for them.
Bob (customer 2) ordered the keyboard, the mouse, and the screen one time, so those are the most frequently ordered products for them.
Tom (customer 3) only ordered the screen (two times), so that is the most frequently ordered product for them.
Jerry (customer 4) only ordered the keyboard (one time), so that is the most frequently ordered product for them.
John (customer 5) did not order anything, so we do not include them in the result table.
*/
/*
query
| customer_id | product_id | product_name |
    most frequently ordered product for each customer
    who have >= 1 order
any order
*/

WITH cte AS (
SELECT o.customer_id
    , product_id
    , any_value(p.product_name) product_name -- THIS IS SUBTLE!
    , RANK () OVER (PARTITION BY customer_id ORDER BY COUNT(o.product_id) DESC) AS rnk
FROM Orders o
    INNER JOIN Products p
        USING (product_id)
GROUP BY customer_id, product_id
)
SELECT customer_id, product_id, product_name
FROM cte
WHERE rnk = 1;

-- this is unneeded to pass:
-- GROUP BY customer_id, product_id;

/*
601. Human Traffic of Stadium (Hard)
-- https://leetcode.com/problems/human-traffic-of-stadium/
Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

The query result format is in the following example.

Example 1:

Input:
Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
Output:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
Explanation:
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.
*/

/*
query
| id   | visit_date | people    |
where
    3+ consecutive id's
    >100 ppl for each
visit_date ASC
*/

-- NOTE: this solution makes me want to vomit

SELECT DISTINCT S1.*
FROM stadium S1
    JOIN stadium S2
    JOIN stadium S3
    ON ((S1.id = S2.id - 1 AND S1.id = S3.id -2)
    OR (S3.id = S1.id - 1 AND S3.id = S2.id -2)
    OR (S3.id = S2.id - 1 AND S3.id = S1.id -2))
WHERE S1.people >= 100
    AND S2.people >= 100
    AND S3.people >= 100
ORDER BY S1.id;

-- NOTE: the genius that wrote this also uses leading commas
-- notice the correlation between leading commas, and genius.

WITH cte AS (
SELECT id
    , visit_date
    , people
    , LEAD(people, 1) OVER w nxt
    , LEAD(people, 2) OVER w nxt2
    , LAG(people, 1) OVER w pre
    , LAG(people, 2) OVER w pre2
FROM Stadium
WINDOW w AS (ORDER BY id)
)
SELECT id
    , visit_date
    , people
FROM cte
WHERE (cte.people >= 100 AND cte.nxt >= 100 AND cte.nxt2 >= 100)
    OR (cte.people >= 100 AND cte.nxt >= 100 AND cte.pre >= 100)
    OR (cte.people >= 100 AND cte.pre >= 100 AND cte.pre2 >= 100);

/*
183. Customers Who Never Order (Easy)
-- https://leetcode.com/problems/customers-who-never-order
Write an SQL query to report all customers who never order anything.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

SELECT c.name Customers
FROM Customers c
WHERE c.id NOT IN (SELECT customerId from Orders);

SELECT name Customers
FROM Customers c
    LEFT JOIN Orders o
        ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL;

/*
1159. Market Analysis II (Hard)
-- https://leetcode.com/problems/market-analysis-ii
Write an SQL query to find for each user whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no. It is guaranteed that no seller sold more than one item on a day.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2019-01-01 | Lenovo         |
| 2       | 2019-02-09 | Samsung        |
| 3       | 2019-01-19 | LG             |
| 4       | 2019-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2019-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2019-08-04 | 1       | 4        | 2         |
| 5        | 2019-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
Output:
+-----------+--------------------+
| seller_id | 2nd_item_fav_brand |
+-----------+--------------------+
| 1         | no                 |
| 2         | yes                |
| 3         | yes                |
| 4         | no                 |
+-----------+--------------------+
Explanation:
The answer for the user with id 1 is no because they sold nothing.
The answer for the users with id 2 and 3 is yes because the brands of their second sold items are their favorite brands.
The answer for the user with id 4 is no because the brand of their second sold item is not their favorite brand.
*/

/*
query
| seller_id | 2nd_item_fav_brand |
'yes'/'no' for each seller_id if the second item they sold is their favorite_brand
    if they have no sold two items, report 'no'
*/

WITH cte AS (
SELECT seller_id
    , item_id
    , RANK() OVER (PARTITION BY seller_id ORDER BY order_date) `rank`
FROM Orders
), cte2 as (
SELECT seller_id
    , item_id
FROM cte
WHERE `rank` = 2
)
/* SELECT * FROM cte2;
+-----------+---------+
| seller_id | item_id |
+-----------+---------+
|         2 |       1 |
|         3 |       3 |
|         4 |       2 |
+-----------+---------+
*/
SELECT DISTINCT U.user_id seller_id
    , CASE WHEN I.item_brand = U.favorite_brand THEN 'yes' ELSE 'no' END '2nd_item_fav_brand'
FROM cte2
    RIGHT JOIN Users U
        ON cte2.seller_id = U.user_id
    LEFT JOIN Items I
        ON cte2.item_id = I.item_id;
/* SELECT * FROM cte2 RIGHT JOIN......;
+-----------+---------+---------+------------+----------------+---------+------------+
| seller_id | item_id | user_id | join_date  | favorite_brand | item_id | item_brand |
+-----------+---------+---------+------------+----------------+---------+------------+
|      NULL |    NULL |       1 | 2019-01-01 | Lenovo         |    NULL | NULL       |
|         2 |       1 |       2 | 2019-02-09 | Samsung        |       1 | Samsung    |
|         3 |       3 |       3 | 2019-01-19 | LG             |       3 | LG         |
|         4 |       2 |       4 | 2019-05-21 | HP             |       2 | Lenovo     |
+-----------+---------+---------+------------+----------------+---------+------------+
*/

/*
1369. Get the Second Most Recent Activity (Hard)
-- https://leetcode.com/problems/get-the-second-most-recent-activity
Write an SQL query to show the second most recent activity of each user.

If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
UserActivity table:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Travel       | 2020-02-12  | 2020-02-20  |
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Alice      | Travel       | 2020-02-24  | 2020-02-28  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
Output:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
Explanation:
The most recent activity of Alice is Travel from 2020-02-24 to 2020-02-28, before that she was dancing from 2020-02-21 to 2020-02-23.
Bob only has one record, we just take that one.
*/

/*
query
| username   | activity     | startDate   | endDate     |
    second most recent activity
    if only one activity for a user, return that
any order
*/
with cte as (
select *
    , COUNT(activity) over(partition by username) `count`
    , ROW_NUMBER() over(partition by username order by startdate desc) n
from UserActivity
)
select username
    , activity
    , startDate
    , endDate
from cte
where `count` < 2 or n = 2;

/*
1741. Find Total Time Spent by Each Employee (Easy)
-- https://leetcode.com/problems/find-total-time-spent-by-each-employee
Write an SQL query to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
Output:
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
Explanation:
Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.
*/

SELECT event_day day
    , emp_id
    , SUM(out_time - in_time) total_time
FROM Employees
GROUP BY event_day, emp_id

/*
182. Duplicate Emails (Easy)
-- https://leetcode.com/problems/duplicate-emails
Write an SQL query to report all the duplicate emails.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
*/

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

/*
612. Shortest Distance in a Plane (Medium)
-- https://leetcode.com/problems/shortest-distance-in-a-plane/
The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).

Write an SQL query to report the shortest distance between any two points from the Point2D table. Round the distance to two decimal points.

The query result format is in the following example.

Example 1:

Input:
Point2D table:
+----+----+
| x  | y  |
+----+----+
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
+----+----+
Output:
+----------+
| shortest |
+----------+
| 1.00     |
+----------+
Explanation: The shortest distance is 1.00 from point (-1, -1) to (-1, 2).
*/

WITH cte AS (
SELECT SQRT(POWER(t1.x - t2.x, 2) + POWER(t1.y - t2.y, 2)) AS path
FROM Point2D t1, Point2D t2
)
SELECT ROUND(MIN(path), 2) AS shortest
FROM cte
WHERE path != 0;

/*
1571. Warehouse Manager (Easy)
-- https://leetcode.com/problems/warehouse-manager
Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Warehouse table:
+------------+--------------+-------------+
| name       | product_id   | units       |
+------------+--------------+-------------+
| LCHouse1   | 1            | 1           |
| LCHouse1   | 2            | 10          |
| LCHouse1   | 3            | 5           |
| LCHouse2   | 1            | 2           |
| LCHouse2   | 2            | 2           |
| LCHouse3   | 4            | 1           |
+------------+--------------+-------------+
Products table:
+------------+--------------+------------+----------+-----------+
| product_id | product_name | Width      | Length   | Height    |
+------------+--------------+------------+----------+-----------+
| 1          | LC-TV        | 5          | 50       | 40        |
| 2          | LC-KeyChain  | 5          | 5        | 5         |
| 3          | LC-Phone     | 2          | 10       | 10        |
| 4          | LC-T-Shirt   | 4          | 10       | 20        |
+------------+--------------+------------+----------+-----------+
Output:
+----------------+------------+
| warehouse_name | volume     |
+----------------+------------+
| LCHouse1       | 12250      |
| LCHouse2       | 20250      |
| LCHouse3       | 800        |
+----------------+------------+
Explanation:
Volume of product_id = 1 (LC-TV), 5x50x40 = 10000
Volume of product_id = 2 (LC-KeyChain), 5x5x5 = 125
Volume of product_id = 3 (LC-Phone), 2x10x10 = 200
Volume of product_id = 4 (LC-T-Shirt), 4x10x20 = 800
LCHouse1: 1 unit of LC-TV + 10 units of LC-KeyChain + 5 units of LC-Phone.
          Total volume: 1*10000 + 10*125  + 5*200 = 12250 cubic feet
LCHouse2: 2 units of LC-TV + 2 units of LC-KeyChain.
          Total volume: 2*10000 + 2*125 = 20250 cubic feet
LCHouse3: 1 unit of LC-T-Shirt.
          Total volume: 1*800 = 800 cubic feet.
*/

select W.name warehouse_name
    , sum(W.units * P.Width * P.Length * P.Height) volume
from Warehouse W
    inner join Products P
        on W.product_id = P.product_id
group by W.name

/*
1083. Sales Analysis II (Easy)
-- https://leetcode.com/problems/product-sales-analysis-ii
Write an SQL query that reports the total quantity sold for every product id.

Return the resulting table in any order.

The query result format is in the following example.

Example 1:

Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output:
+--------------+----------------+
| product_id   | total_quantity |
+--------------+----------------+
| 100          | 22             |
| 200          | 15             |
+--------------+----------------+
*/

select product_id
    , sum(quantity) total_quantity
from Sales
group by product_id;

/*
1651. Hopper Company Queries III (Hard)
-- https://leetcode.com/problems/hopper-company-queries-iii
Write an SQL query to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.

The average_ride_distance is calculated by summing up the total ride_distance values from the three months and dividing it by 3. The average_ride_duration is calculated in a similar way.

Return the result table ordered by month in ascending order, where month is the starting month's number (January is 1, February is 2, etc.).

The query result format is in the following example.

Example 1:

Input:
Drivers table:
+-----------+------------+
| driver_id | join_date  |
+-----------+------------+
| 10        | 2019-12-10 |
| 8         | 2020-1-13  |
| 5         | 2020-2-16  |
| 7         | 2020-3-8   |
| 4         | 2020-5-17  |
| 1         | 2020-10-24 |
| 6         | 2021-1-5   |
+-----------+------------+
Rides table:
+---------+---------+--------------+
| ride_id | user_id | requested_at |
+---------+---------+--------------+
| 6       | 75      | 2019-12-9    |
| 1       | 54      | 2020-2-9     |
| 10      | 63      | 2020-3-4     |
| 19      | 39      | 2020-4-6     |
| 3       | 41      | 2020-6-3     |
| 13      | 52      | 2020-6-22    |
| 7       | 69      | 2020-7-16    |
| 17      | 70      | 2020-8-25    |
| 20      | 81      | 2020-11-2    |
| 5       | 57      | 2020-11-9    |
| 2       | 42      | 2020-12-9    |
| 11      | 68      | 2021-1-11    |
| 15      | 32      | 2021-1-17    |
| 12      | 11      | 2021-1-19    |
| 14      | 18      | 2021-1-27    |
+---------+---------+--------------+
AcceptedRides table:
+---------+-----------+---------------+---------------+
| ride_id | driver_id | ride_distance | ride_duration |
+---------+-----------+---------------+---------------+
| 10      | 10        | 63            | 38            |
| 13      | 10        | 73            | 96            |
| 7       | 8         | 100           | 28            |
| 17      | 7         | 119           | 68            |
| 20      | 1         | 121           | 92            |
| 5       | 7         | 42            | 101           |
| 2       | 4         | 6             | 38            |
| 11      | 8         | 37            | 43            |
| 15      | 8         | 108           | 82            |
| 12      | 8         | 38            | 34            |
| 14      | 1         | 90            | 74            |
+---------+-----------+---------------+---------------+
Output:
+-------+-----------------------+-----------------------+
| month | average_ride_distance | average_ride_duration |
+-------+-----------------------+-----------------------+
| 1     | 21.00                 | 12.67                 |
| 2     | 21.00                 | 12.67                 |
| 3     | 21.00                 | 12.67                 |
| 4     | 24.33                 | 32.00                 |
| 5     | 57.67                 | 41.33                 |
| 6     | 97.33                 | 64.00                 |
| 7     | 73.00                 | 32.00                 |
| 8     | 39.67                 | 22.67                 |
| 9     | 54.33                 | 64.33                 |
| 10    | 56.33                 | 77.00                 |
+-------+-----------------------+-----------------------+
Explanation:
By the end of January --> average_ride_distance = (0+0+63)/3=21, average_ride_duration = (0+0+38)/3=12.67
By the end of February --> average_ride_distance = (0+63+0)/3=21, average_ride_duration = (0+38+0)/3=12.67
By the end of March --> average_ride_distance = (63+0+0)/3=21, average_ride_duration = (38+0+0)/3=12.67
By the end of April --> average_ride_distance = (0+0+73)/3=24.33, average_ride_duration = (0+0+96)/3=32.00
By the end of May --> average_ride_distance = (0+73+100)/3=57.67, average_ride_duration = (0+96+28)/3=41.33
By the end of June --> average_ride_distance = (73+100+119)/3=97.33, average_ride_duration = (96+28+68)/3=64.00
By the end of July --> average_ride_distance = (100+119+0)/3=73.00, average_ride_duration = (28+68+0)/3=32.00
By the end of August --> average_ride_distance = (119+0+0)/3=39.67, average_ride_duration = (68+0+0)/3=22.67
By the end of Septemeber --> average_ride_distance = (0+0+163)/3=54.33, average_ride_duration = (0+0+193)/3=64.33
By the end of October --> average_ride_distance = (0+163+6)/3=56.33, average_ride_duration = (0+193+38)/3=77.00
*/

-- TODO

/*
1479. Sales by Day of the Week (Hard)
-- https://leetcode.com/problems/sales-by-day-of-the-week
You are the business owner and would like to obtain a sales report for category items and the day of the week.

Write an SQL query to report how many units in each category have been ordered on each day of the week.

Return the result table ordered by category.

The query result format is in the following example.

Example 1:

Input:
Orders table:
+------------+--------------+-------------+--------------+-------------+
| order_id   | customer_id  | order_date  | item_id      | quantity    |
+------------+--------------+-------------+--------------+-------------+
| 1          | 1            | 2020-06-01  | 1            | 10          |
| 2          | 1            | 2020-06-08  | 2            | 10          |
| 3          | 2            | 2020-06-02  | 1            | 5           |
| 4          | 3            | 2020-06-03  | 3            | 5           |
| 5          | 4            | 2020-06-04  | 4            | 1           |
| 6          | 4            | 2020-06-05  | 5            | 5           |
| 7          | 5            | 2020-06-05  | 1            | 10          |
| 8          | 5            | 2020-06-14  | 4            | 5           |
| 9          | 5            | 2020-06-21  | 3            | 5           |
+------------+--------------+-------------+--------------+-------------+
Items table:
+------------+----------------+---------------+
| item_id    | item_name      | item_category |
+------------+----------------+---------------+
| 1          | LC Alg. Book   | Book          |
| 2          | LC DB. Book    | Book          |
| 3          | LC SmarthPhone | Phone         |
| 4          | LC Phone 2020  | Phone         |
| 5          | LC SmartGlass  | Glasses       |
| 6          | LC T-Shirt XL  | T-Shirt       |
+------------+----------------+---------------+
Output:
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Category   | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  | Sunday    |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Book       | 20        | 5         | 0         | 0         | 10        | 0         | 0         |
| Glasses    | 0         | 0         | 0         | 0         | 5         | 0         | 0         |
| Phone      | 0         | 0         | 5         | 1         | 0         | 0         | 10        |
| T-Shirt    | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
Explanation:
On Monday (2020-06-01, 2020-06-08) were sold a total of 20 units (10 + 10) in the category Book (ids: 1, 2).
On Tuesday (2020-06-02) were sold a total of 5 units in the category Book (ids: 1, 2).
On Wednesday (2020-06-03) were sold a total of 5 units in the category Phone (ids: 3, 4).
On Thursday (2020-06-04) were sold a total of 1 unit in the category Phone (ids: 3, 4).
On Friday (2020-06-05) were sold 10 units in the category Book (ids: 1, 2) and 5 units in Glasses (ids: 5).
On Saturday there are no items sold.
On Sunday (2020-06-14, 2020-06-21) were sold a total of 10 units (5 +5) in the category Phone (ids: 3, 4).
There are no sales of T-shirts.
*/

/*
query
| Category   | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  | Sunday    |
    units in each category have been ordered on each weekday
order by category
*/

SELECT i.item_category AS Category
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN quantity ELSE 0 END) AS Monday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN quantity ELSE 0 END) AS Tuesday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN quantity ELSE 0 END) AS Wednesday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN quantity ELSE 0 END) AS Thursday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN quantity ELSE 0 END) AS Friday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN quantity ELSE 0 END) AS Saturday
    , SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN quantity ELSE 0 END) AS Sunday
FROM Items i
    LEFT JOIN Orders o
        ON i.item_id = o.item_id
GROUP BY i.item_category
ORDER BY i.item_category;

/*
1811. Find Interview Candidates (Medium)
-- https://leetcode.com/problems/find-interview-candidates
Write an SQL query to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:
* The user won any medal in three or more consecutive contests.
* The user won the gold medal in three or more different contests (not necessarily consecutive).
* Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Contests table:
+------------+------------+--------------+--------------+
| contest_id | gold_medal | silver_medal | bronze_medal |
+------------+------------+--------------+--------------+
| 190        | 1          | 5            | 2            |
| 191        | 2          | 3            | 5            |
| 192        | 5          | 2            | 3            |
| 193        | 1          | 3            | 5            |
| 194        | 4          | 5            | 2            |
| 195        | 4          | 2            | 1            |
| 196        | 1          | 5            | 2            |
+------------+------------+--------------+--------------+
Users table:
+---------+--------------------+-------+
| user_id | mail               | name  |
+---------+--------------------+-------+
| 1       | sarah@leetcode.com | Sarah |
| 2       | bob@leetcode.com   | Bob   |
| 3       | alice@leetcode.com | Alice |
| 4       | hercy@leetcode.com | Hercy |
| 5       | quarz@leetcode.com | Quarz |
+---------+--------------------+-------+
Output:
+-------+--------------------+
| name  | mail               |
+-------+--------------------+
| Sarah | sarah@leetcode.com |
| Bob   | bob@leetcode.com   |
| Alice | alice@leetcode.com |
| Quarz | quarz@leetcode.com |
+-------+--------------------+
Explanation:
Sarah won 3 gold medals (190, 193, and 196), so we include her in the result table.
Bob won a medal in 3 consecutive contests (190, 191, and 192), so we include him in the result table.
    - Note that he also won a medal in 3 other consecutive contests (194, 195, and 196).
Alice won a medal in 3 consecutive contests (191, 192, and 193), so we include her in the result table.
Quarz won a medal in 5 consecutive contests (190, 191, 192, 193, and 194), so we include them in the result table.
*/

with cte as (
select user_id
    , name
    , mail
    , contest_id
    , user_id = gold_medal as gold
    , user_id = silver_medal as silver
    , user_id = bronze_medal as bronze
    , lag(contest_id, 2) over (partition by user_id order by contest_id) as prevprev
from Users
    left join Contests
        on user_id = gold_medal
        or user_id = silver_medal
        or user_id = bronze_medal
)
select name, mail
from cte
group by user_id, name, mail
having sum(gold) >= 3
    or sum(contest_id - prevprev = 2) > 0;

-- TODO redo below with ctes

WITH cte AS (
SELECT Users.user_id
    , Users.name
    , Users.mail
    , Contests.contest_id
    , CASE WHEN Users.user_id = Contests.gold_medal THEN 1 ELSE 0 END AS gold
    , CASE WHEN Users.user_id = Contests.silver_medal THEN 1 ELSE 0 END AS silver
    , CASE WHEN Users.user_id = Contests.bronze_medal THEN 1 ELSE 0 END AS bronze
    , LAG (Contests.contest_id, 2) OVER ( PARTITION BY Users.user_id ORDER BY Contests.contest_id ) AS prevprev
FROM Users
    LEFT JOIN Contests
        ON Users.user_id = Contests.gold_medal
        OR Users.user_id = Contests.silver_medal
        OR Users.user_id = Contests.bronze_medal
)
SELECT Candidates.name,
       Candidates.mail
FROM (
SELECT AggData.user_id ,
       AggData.name ,
       AggData.mail ,
       AggData.Golds ,
       AggData.Consecutives
FROM (
       SELECT cte.user_id ,
              cte.name ,
              cte.mail ,
              SUM(cte.gold) AS Golds ,
              SUM(CASE WHEN cte.contest_id - cte.prevprev = 2 THEN 1 ELSE 0 END) AS Consecutives
       FROM cte
       GROUP BY cte.user_id ,
                cte.name ,
                cte.mail
     ) AS AggData
WHERE AggData.Golds >= 3
      OR AggData.Consecutives >= 1
) AS Candidates;

/*
585. Investments in 2016 (Medium)
-- https://leetcode.com/problems/investments-in-2016/

-- NOTE
-- pid is the policyholder's policy ID.
-- tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
-- lat is the latitude of the policy holder's city.
-- lon is the longitude of the policy holder's city.

Write an SQL query to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
* have the same tiv_2015 value as one or more other policyholders, and
* are not located in the same city like any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).

Round tiv_2016 to two decimal places.

The query result format is in the following example.

Example 1:

Input:
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
Output:
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
Explanation:
The first record in the table, like the last record, meets both of the two criteria.
The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.

The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
So, the result is the sum of tiv_2016 of the first and last record, which is 45.
*/

WITH cte AS(
SELECT *
    , COUNT(*) OVER(PARTITION BY TIV_2015) AS COUNT1
    , COUNT(*) OVER(PARTITION BY LAT, LON) AS COUNT2
FROM Insurance
)
SELECT ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM cte
WHERE COUNT1 >= 2 AND COUNT2 = 1;

/*
596. Classes More Than 5 Students (Easy)
-- https://leetcode.com/problems/classes-more-than-5-students/
Write an SQL query to report all the classes that have at least five students.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output:
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation:
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
*/

SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;

/*
1112. Highest Grade For Each Student (Medium)
-- https://leetcode.com/problems/highest-grade-for-each-student
Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
Output:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
*/

WITH cte AS (
SELECT student_id
    , course_id
    , grade
    , MAX(grade) OVER (PARTITION BY student_id) AS max_grade
FROM Enrollments
)
SELECT ANY_VALUE(student_id) student_id
    , MIN(course_id) AS course_id
    , ANY_VALUE(grade) grade
FROM cte
WHERE max_grade = grade
GROUP BY student_id;

/*
1783. Grand Slam Titles (Medium)
-- https://leetcode.com/problems/grand-slam-titles
Write an SQL query to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Players table:
+-----------+-------------+
| player_id | player_name |
+-----------+-------------+
| 1         | Nadal       |
| 2         | Federer     |
| 3         | Novak       |
+-----------+-------------+
Championships table:
+------+-----------+---------+---------+---------+
| year | Wimbledon | Fr_open | US_open | Au_open |
+------+-----------+---------+---------+---------+
| 2018 | 1         | 1       | 1       | 1       |
| 2019 | 1         | 1       | 2       | 2       |
| 2020 | 2         | 1       | 2       | 2       |
+------+-----------+---------+---------+---------+
Output:
+-----------+-------------+-------------------+
| player_id | player_name | grand_slams_count |
+-----------+-------------+-------------------+
| 2         | Federer     | 5                 |
| 1         | Nadal       | 7                 |
+-----------+-------------+-------------------+
Explanation:
Player 1 (Nadal) won 7 titles: Wimbledon (2018, 2019), Fr_open (2018, 2019, 2020), US_open (2018), and Au_open (2018).
Player 2 (Federer) won 5 titles: Wimbledon (2020), US_open (2019, 2020), and Au_open (2019, 2020).
Player 3 (Novak) did not win anything, we did not include them in the result table.
*/

SELECT ANY_VALUE(player_id) player_id
    , ANY_VALUE(player_name) player_name
    , SUM(player_id = Wimbledon)
    + SUM(player_id = Fr_open)
    + SUM(player_id = US_open)
    + SUM(player_id = Au_open) AS grand_slams_count
FROM Players
    JOIN Championships
        ON player_id = Wimbledon
        OR player_id = Fr_open
        OR player_id = US_open
        OR player_id = Au_open
GROUP BY player_id;

/*
1241. Number of Comments per Post (Easy)
-- https://leetcode.com/problems/number-of-comments-per-post
Write an SQL query to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.

The Submissions table may contain duplicate comments. You should count the number of unique comments per post.

The Submissions table may contain duplicate posts. You should treat them as one post.

The result table should be ordered by post_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Submissions table:
+---------+------------+
| sub_id  | parent_id  |
+---------+------------+
| 1       | Null       |
| 2       | Null       |
| 1       | Null       |
| 12      | Null       |
| 3       | 1          |
| 5       | 2          |
| 3       | 1          |
| 4       | 1          |
| 9       | 1          |
| 10      | 2          |
| 6       | 7          |
+---------+------------+
Output:
+---------+--------------------+
| post_id | number_of_comments |
+---------+--------------------+
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |
+---------+--------------------+
Explanation:
The post with id 1 has three comments in the table with id 3, 4, and 9. The comment with id 3 is repeated in the table, we counted it only once.
The post with id 2 has two comments in the table with id 5 and 10.
The post with id 12 has no comments in the table.
The comment with id 6 is a comment on a deleted post with id 7 so we ignored it.
*/

SELECT sub_id AS post_id
    , (
    SELECT COUNT(DISTINCT(child.sub_id))
    FROM Submissions child
    WHERE child.parent_id = parent.sub_id
    ) AS number_of_comments
FROM Submissions parent
WHERE parent.parent_id IS NULL
GROUP BY parent.sub_id
ORDER BY 1;

/*
1285. Find the Start and End Number of Continuous Ranges (Medium)
-- https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges
Write an SQL query to find the start and end number of continuous ranges in the table Logs.

Return the result table ordered by start_id.

The query result format is in the following example.

Example 1:

Input:
Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+
Output:
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
Explanation:
The result table should contain all ranges in table Logs.
From 1 to 3 is contained in the table.
From 4 to 6 is missing in the table
From 7 to 8 is contained in the table.
Number 9 is missing from the table.
Number 10 is contained in the table.
*/

WITH cte AS (
SELECT log_id
    , ROW_NUMBER() OVER (ORDER BY log_id) as row_number_log_ig
FROM Logs
)
SELECT min(log_id) as start_id
    , max(log_id) as end_id
FROM cte
GROUP BY log_id - row_number_log_ig

/*
595. Big Countries (Easy)
-- https://leetcode.com/problems/big-countries/
A country is big if:
* it has an area of at least three million (i.e., 3000000 km2)
* or it has a population of at least twenty-five million (i.e., 25000000).

Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
*/

SELECT name
    , population
    , area
FROM World
WHERE area > 3000000 OR population > 25000000;

/*
603. Consecutive Available Seats (Easy)
-- https://leetcode.com/problems/consecutive-available-seats/
Write an SQL query to report all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.

The query result format is in the following example.

Example 1:

Input:
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
Output:
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+
*/

with cte as(
select seat_id
    , free
    , seat_id - row_number() over (order by seat_id) as grouper
from cinema
where free = 1
)
select seat_id
from cte
where grouper in (select grouper from cte group by grouper having count(*) >= 2)
order by seat_id;

SELECT DISTINCT a.seat_id
FROM cinema a
    INNER JOIN cinema b
        ON ABS(a.seat_id - b.seat_id) = 1
        AND a.free = true
        AND b.free = true
ORDER BY a.seat_id;

/*
620. Not Boring Movies (Easy)
-- https://leetcode.com/problems/not-boring-movies/
Write an SQL query to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

The query result format is in the following example.

Example 1:

Input:
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
Output:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
Explanation:
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
*/

SELECT *
FROM Cinema
WHERE id % 2 = 1
    AND description != 'boring'
ORDER BY rating DESC;

/*
1841. League Statistics (Medium)
-- https://leetcode.com/problems/league-statistics
Write an SQL query to report the statistics of the league. The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points. If a match ends with a draw, both teams get one point.

Each row of the result table should contain:

team_name - The name of the team in the Teams table.
matches_played - The number of matches played as either a home or away team.
points - The total points the team has so far.
goal_for - The total number of goals scored by the team across all matches.
goal_against - The total number of goals scored by opponent teams against this team across all matches.
goal_diff - The result of goal_for - goal_against.
Return the result table ordered by points in descending order. If two or more teams have the same points, order them by goal_diff in descending order. If there is still a tie, order them by team_name in lexicographical order.

The query result format is in the following example.

Example 1:

Input:
Teams table:
+---------+-----------+
| team_id | team_name |
+---------+-----------+
| 1       | Ajax      |
| 4       | Dortmund  |
| 6       | Arsenal   |
+---------+-----------+
Matches table:
+--------------+--------------+-----------------+-----------------+
| home_team_id | away_team_id | home_team_goals | away_team_goals |
+--------------+--------------+-----------------+-----------------+
| 1            | 4            | 0               | 1               |
| 1            | 6            | 3               | 3               |
| 4            | 1            | 5               | 2               |
| 6            | 1            | 0               | 0               |
+--------------+--------------+-----------------+-----------------+
Output:
+-----------+----------------+--------+----------+--------------+-----------+
| team_name | matches_played | points | goal_for | goal_against | goal_diff |
+-----------+----------------+--------+----------+--------------+-----------+
| Dortmund  | 2              | 6      | 6        | 2            | 4         |
| Arsenal   | 2              | 2      | 3        | 3            | 0         |
| Ajax      | 4              | 2      | 5        | 9            | -4        |
+-----------+----------------+--------+----------+--------------+-----------+
Explanation:
Ajax (team_id=1) played 4 matches: 2 losses and 2 draws. Total points = 0 + 0 + 1 + 1 = 2.
Dortmund (team_id=4) played 2 matches: 2 wins. Total points = 3 + 3 = 6.
Arsenal (team_id=6) played 2 matches: 2 draws. Total points = 1 + 1 = 2.
Dortmund is the first team in the table. Ajax and Arsenal have the same points, but since Arsenal has a higher goal_diff than Ajax, Arsenal comes before Ajax in the table.
*/

WITH cte AS (
SELECT *
FROM Matches M1
UNION ALL
SELECT away_team_id home_team_id
    , home_team_id away_team_id
    , away_team_goals home_team_goals
    , home_team_goals away_team_goals
FROM Matches M2
)
SELECT ANY_VALUE(T.team_name) team_name
    , COUNT(*) matches_played
    , SUM(CASE
        WHEN home_team_goals > away_team_goals THEN 3
        WHEN home_team_goals = away_team_goals THEN 1
        WHEN home_team_goals < away_team_goals THEN 0
    END) points
    , SUM(home_team_goals) goal_for
    , SUM(away_team_goals) goal_against
    , SUM(home_team_goals) - SUM(away_team_goals) goal_diff
FROM cte
    INNER JOIN Teams T
        ON cte.home_team_id = T.team_id
GROUP BY T.team_name
ORDER BY points DESC, goal_diff DESC, T.team_name;

/*
608. Tree Node (Medium)
-- https://leetcode.com/problems/tree-node/
Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.
Write an SQL query to report the type of each node in the tree.

Return the result table ordered by id in ascending order.

The query result format is in the following example.

Example 1:
    1
   / \
  2   3
 /\
4  5
Input:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
Explanation:
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.

Example 2:
  1

Input:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
+----+------+
Output:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
+----+-------+
Explanation: If there is only one node on the tree, you only need to output its root attributes.
*/

SELECT id AS `Id`
    , CASE
        WHEN tree.id = (SELECT temp.id FROM tree temp WHERE temp.p_id IS NULL) THEN 'Root'
        WHEN tree.id IN (SELECT temp.p_id FROM tree temp) THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM tree
ORDER BY `Id`;

/*
1142. User Activity for the Past 30 Days II (Easy)
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-ii
Write an SQL query to find the average number of sessions per user for a period of 30 days ending 2019-07-27 inclusively, rounded to 2 decimal places. The sessions we want to count for a user are those with at least one activity in that time period.

The query result format is in the following example.

Example 1:

Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 3       | 5          | 2019-07-21    | open_session  |
| 3       | 5          | 2019-07-21    | scroll_down   |
| 3       | 5          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
Output:
+---------------------------+
| average_sessions_per_user |
+---------------------------+
| 1.33                      |
+---------------------------+
Explanation: User 1 and 2 each had 1 session in the past 30 days while user 3 had 2 sessions so the average is (1 + 1 + 2) / 3 = 1.33.
*/

SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0.00) AS average_sessions_per_user
FROM Activity
WHERE activity_date >= ('2019-07-27' - INTERVAL 29 DAY)
    AND activity_date <= '2019-07-27';

/*
618. Students Report By Geography (Hard)
-- https://leetcode.com/problems/students-report-by-geography/
A school has students from Asia, Europe, and America.

Write an SQL query to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.

The test cases are generated so that the student number from America is not less than either Asia or Europe.

The query result format is in the following example.

Example 1:

Input:
Student table:
+--------+-----------+
| name   | continent |
+--------+-----------+
| Jane   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jack   | America   |
+--------+-----------+
Output:
+---------+------+--------+
| America | Asia | Europe |
+---------+------+--------+
| Jack    | Xi   | Pascal |
| Jane    | null | null   |
+---------+------+--------+

Follow up: If it is unknown which continent has the most students, could you write a query to generate the student report?
*/

-- TODO

/*
1113. Reported Posts (Easy)
-- https://leetcode.com/problems/reported-posts
Write an SQL query that reports the number of posts reported yesterday for each report reason. Assume today is 2019-07-05.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 4       | 2019-07-04  | view   | null   |
| 2       | 4       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-04  | view   | null   |
| 5       | 2       | 2019-07-04  | report | racism |
| 5       | 5       | 2019-07-04  | view   | null   |
| 5       | 5       | 2019-07-04  | report | racism |
+---------+---------+-------------+--------+--------+
Output:
+---------------+--------------+
| report_reason | report_count |
+---------------+--------------+
| spam          | 1            |
| racism        | 2            |
+---------------+--------------+
Explanation: Note that we only care about report reasons with non-zero number of reports.
*/

SELECT DISTINCT extra AS report_reason
    , COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action = 'report'
    AND action_date = '2019-07-04'
GROUP BY extra;

/*
1077. Project Employees III (Medium)
-- https://leetcode.com/problems/project-employees-iii
Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 3                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output:
+-------------+---------------+
| project_id  | employee_id   |
+-------------+---------------+
| 1           | 1             |
| 1           | 3             |
| 2           | 1             |
+-------------+---------------+
Explanation: Both employees with id 1 and 3 have the most experience among the employees of the first project. For the second project, the employee with id 1 has the most experience.
*/

SELECT p.project_id
    , e.employee_id
FROM project p
    INNER JOIN employee e
        ON e.employee_id = p.employee_id
WHERE (p.project_id, e.experience_years) IN (
    SELECT p.project_id
        , MAX(e.experience_years)
    FROM project p
        INNER JOIN employee e
            ON e.employee_id = p.employee_id
    GROUP BY project_id
);

/*
1322. Ads Performance (Easy)
-- https://leetcode.com/problems/ads-performance
A company is running Ads and wants to calculate the performance of each Ad.

Performance of the Ad is measured using Click-Through Rate (CTR) where:

CTR = if ad total clicks + ad total views = 0 -> 0
      otherwise -> ad total clicks / (ad total clicks + ad total views) * 100

NOTE if confused see https://assets.leetcode.com/uploads/2020/01/17/sql1.png

Write an SQL query to find the ctr of each Ad. Round ctr to two decimal points.

Return the result table ordered by ctr in descending order and by ad_id in ascending order in case of a tie.

The query result format is in the following example.

Example 1:

Input:
Ads table:
+-------+---------+---------+
| ad_id | user_id | action  |
+-------+---------+---------+
| 1     | 1       | Clicked |
| 2     | 2       | Clicked |
| 3     | 3       | Viewed  |
| 5     | 5       | Ignored |
| 1     | 7       | Ignored |
| 2     | 7       | Viewed  |
| 3     | 5       | Clicked |
| 1     | 4       | Viewed  |
| 2     | 11      | Viewed  |
| 1     | 2       | Clicked |
+-------+---------+---------+
Output:
+-------+-------+
| ad_id | ctr   |
+-------+-------+
| 1     | 66.67 |
| 3     | 50.00 |
| 2     | 33.33 |
| 5     | 0.00  |
+-------+-------+
Explanation:
for ad_id = 1, ctr = (2/(2+1)) * 100 = 66.67
for ad_id = 2, ctr = (1/(1+2)) * 100 = 33.33
for ad_id = 3, ctr = (1/(1+1)) * 100 = 50.00
for ad_id = 5, ctr = 0.00, Note that ad_id = 5 has no clicks or views.
Note that we do not care about Ignored Ads.
*/

select ad_id
    , round(ifnull((sum(action = 'Clicked') / (sum(action = 'Clicked') + sum(action = 'Viewed'))) * 100, 0), 2) as ctr
from Ads
group by ad_id
order by ctr desc, ad_id;

/*
586. Customer Placing the Largest Number of Orders (Easy)
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The query result format is in the following example.

Example 1:

Input:
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation:
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order.
So the result is customer_number 3.

Follow up: What if more than one customer has the largest number of orders, can you find all the customer_number in this case?
*/

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;

/*
1097. Game Play Analysis V (Hard)
-- https://leetcode.com/problems/game-play-analysis-v
The install date of a player is the first login day of that player.

We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, divided by the number of players whose install date is x, rounded to 2 decimal places.

Write an SQL query to report for each install date, the number of players that installed the game on that day, and the day one retention.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-01 | 0            |
| 3         | 4         | 2016-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+------------+----------+----------------+
| install_dt | installs | Day1_retention |
+------------+----------+----------------+
| 2016-03-01 | 2        | 0.50           |
| 2017-06-25 | 1        | 0.00           |
+------------+----------+----------------+
Explanation:
Player 1 and 3 installed the game on 2016-03-01 but only player 1 logged back in on 2016-03-02 so the day 1 retention of 2016-03-01 is 1 / 2 = 0.50
Player 2 installed the game on 2017-06-25 but didn't log back in on 2017-06-26 so the day 1 retention of 2017-06-25 is 0 / 1 = 0.00
*/

WITH i AS (
SELECT player_id
    , MIN(event_date) AS install_dt
FROM Activity
GROUP BY player_id
)
SELECT i.install_dt
    , COUNT(i.install_dt) AS installs
    , ROUND(SUM(IF(a.event_date, 1, 0)) / COUNT(i.install_dt), 2) AS Day1_retention
FROM i
    LEFT JOIN Activity AS a
        ON i.player_id = a.player_id
        AND DATEDIFF(a.event_date, i.install_dt) = 1
GROUP BY i.install_dt

/*
1613. Find the Missing IDs (Medium)
-- https://leetcode.com/problems/find-the-missing-ids
Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

Notice that the maximum customer_id will not exceed 100.

Return the result table ordered by ids in ascending order.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
Output:
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
Explanation:
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.
*/

WITH RECURSIVE cte AS (
SELECT 1 AS value
UNION ALL
SELECT value + 1
FROM cte
WHERE value < (select max(customer_id) from Customers)
)
SELECT cte.value AS ids
FROM cte
    LEFT JOIN Customers c
        ON cte.value = c.customer_id
WHERE c.customer_id IS NULL
ORDER BY ids;

/*
1549. The Most Recent Orders for Each Product (Medium)
-- https://leetcode.com/problems/the-most-recent-orders-for-each-product
Write an SQL query to find the most recent order(s) of each product.

Return the result table ordered by product_name in ascending order and in case of a tie
by the product_id in ascending order. If there still a tie, order them by order_id in
ascending order.

The query result format is in the following example.

Example 1:
Input:
Customers table:
+-------------+-----------+
| customer_id | name      |
+-------------+-----------+
| 1           | Winston   |
| 2           | Jonathan  |
| 3           | Annabelle |
| 4           | Marwan    |
| 5           | Khaled    |
+-------------+-----------+
Orders table:
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | product_id |
+----------+------------+-------------+------------+
| 1        | 2020-07-31 | 1           | 1          |
| 2        | 2020-07-30 | 2           | 2          |
| 3        | 2020-08-29 | 3           | 3          |
| 4        | 2020-07-29 | 4           | 1          |
| 5        | 2020-06-10 | 1           | 2          |
| 6        | 2020-08-01 | 2           | 1          |
| 7        | 2020-08-01 | 3           | 1          |
| 8        | 2020-08-03 | 1           | 2          |
| 9        | 2020-08-07 | 2           | 3          |
| 10       | 2020-07-15 | 1           | 2          |
+----------+------------+-------------+------------+
Products table:
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
| 1          | keyboard     | 120   |
| 2          | mouse        | 80    |
| 3          | screen       | 600   |
| 4          | hard disk    | 450   |
+------------+--------------+-------+
Output:
+--------------+------------+----------+------------+
| product_name | product_id | order_id | order_date |
+--------------+------------+----------+------------+
| keyboard     | 1          | 6        | 2020-08-01 |
| keyboard     | 1          | 7        | 2020-08-01 |
| mouse        | 2          | 8        | 2020-08-03 |
| screen       | 3          | 3        | 2020-08-29 |
+--------------+------------+----------+------------+
Explanation:
keyboard's most recent order is in 2020-08-01, it was ordered two times this day.
mouse's most recent order is in 2020-08-03, it was ordered only once this day.
screen's most recent order is in 2020-08-29, it was ordered only once this day.
The hard disk was never ordered and we do not include it in the result table.
*/

with T as (
select product_id
    , max(order_date) as order_date
from Orders
group by product_id
)
select P.product_name
    , O.product_id
    , O.order_id
    , O.order_date
from Orders O
    inner join Products P
        using (product_id)
where (O.product_id, O.order_date) in (select * from T)
order by P.product_name, O.product_id, O.order_id

/*
1867. Orders With Maximum Quantity Above Average (Medium)
-- https://leetcode.com/problems/orders-with-maximum-quantity-above-average
You are running an e-commerce site that is looking for imbalanced orders. An imbalanced order is one whose maximum quantity is strictly greater than the average quantity of every order (including itself).

The average quantity of an order is calculated as (total quantity of all products in the order) / (number of different products in the order). The maximum quantity of an order is the highest quantity of any single product in the order.

Write an SQL query to find the order_id of all imbalanced orders.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
OrdersDetails table:
+----------+------------+----------+
| order_id | product_id | quantity |
+----------+------------+----------+
| 1        | 1          | 12       |
| 1        | 2          | 10       |
| 1        | 3          | 15       |
| 2        | 1          | 8        |
| 2        | 4          | 4        |
| 2        | 5          | 6        |
| 3        | 3          | 5        |
| 3        | 4          | 18       |
| 4        | 5          | 2        |
| 4        | 6          | 8        |
| 5        | 7          | 9        |
| 5        | 8          | 9        |
| 3        | 9          | 20       |
| 2        | 9          | 4        |
+----------+------------+----------+
Output:
+----------+
| order_id |
+----------+
| 1        |
| 3        |
+----------+
Explanation:
The average quantity of each order is:
- order_id=1: (12+10+15)/3 = 12.3333333
- order_id=2: (8+4+6+4)/4 = 5.5
- order_id=3: (5+18+20)/3 = 14.333333
- order_id=4: (2+8)/2 = 5
- order_id=5: (9+9)/2 = 9

The maximum quantity of each order is:
- order_id=1: max(12, 10, 15) = 15
- order_id=2: max(8, 4, 6, 4) = 8
- order_id=3: max(5, 18, 20) = 20
- order_id=4: max(2, 8) = 8
- order_id=5: max(9, 9) = 9

Orders 1 and 3 are imbalanced because they have a maximum quantity that exceeds the average quantity of every order.
*/

with cte as (
select order_id
    , max(avg(quantity)) over() max_avg_quantity
    , max(quantity) max_quantity
from OrdersDetails
group by order_id
)
select order_id
from cte
where max_quantity > max_avg_quantity;

/*
1205. Monthly Transactions II (Medium)
-- https://leetcode.com/problems/monthly-transactions-ii
Write an SQL query to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

Note: In your query, given the month and country, ignore rows with all zeros.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Transactions table:
+-----+---------+----------+--------+------------+
| id  | country | state    | amount | trans_date |
+-----+---------+----------+--------+------------+
| 101 | US      | approved | 1000   | 2019-05-18 |
| 102 | US      | declined | 2000   | 2019-05-19 |
| 103 | US      | approved | 3000   | 2019-06-10 |
| 104 | US      | declined | 4000   | 2019-06-13 |
| 105 | US      | approved | 5000   | 2019-06-15 |
+-----+---------+----------+--------+------------+
Chargebacks table:
+----------+------------+
| trans_id | trans_date |
+----------+------------+
| 102      | 2019-05-29 |
| 101      | 2019-06-30 |
| 105      | 2019-09-18 |
+----------+------------+
Output:
+---------+---------+----------------+-----------------+------------------+-------------------+
| month   | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
+---------+---------+----------------+-----------------+------------------+-------------------+
| 2019-05 | US      | 1              | 1000            | 1                | 2000              |
| 2019-06 | US      | 2              | 8000            | 1                | 1000              |
| 2019-09 | US      | 0              | 0               | 1                | 5000              |
+---------+---------+----------------+-----------------+------------------+-------------------+
*/

WITH CTE AS (
SELECT id
    , country
    , state
    , amount
    , DATE_FORMAT(trans_date, '%Y-%m') AS month
FROM Transactions
WHERE state = 'approved'
UNION
SELECT c.trans_id
    , t.country
    , 'chargeback' AS state
    , t.amount
    , DATE_FORMAT(c.trans_date, '%Y-%m') AS month
FROM Chargebacks c
    LEFT JOIN Transactions t
        ON c.trans_id = t.id
)
SELECT month
    , country
    , SUM(IF(state = 'approved', 1, 0)) AS approved_count
    , SUM(IF(state = 'approved', amount, 0)) AS approved_amount
    , SUM(IF(state = 'chargeback', 1, 0)) AS chargeback_count
    , SUM(IF(state = 'chargeback', amount, 0)) AS chargeback_amount
FROM CTE
GROUP BY month, country
ORDER BY month, country;

/*
511. Game Play Analysis I (Easy)
-- https://leetcode.com/problems/game-play-analysis-i

*/

-- TODO

/*
1677. Products Worth Over Invoices (Easy)
-- https://leetcode.com/problems/products-worth-over-invoices/
Write an SQL query that will, for all products, return each product name with the total amount due, paid, canceled, and refunded across all invoices.

Return the result table ordered by product_name.

The query result format is in the following example.

Example 1:

Input:
Product table:
+------------+-------+
| product_id | name  |
+------------+-------+
| 0          | ham   |
| 1          | bacon |
+------------+-------+
Invoice table:
+------------+------------+------+------+----------+----------+
| invoice_id | product_id | rest | paid | canceled | refunded |
+------------+------------+------+------+----------+----------+
| 23         | 0          | 2    | 0    | 5        | 0        |
| 12         | 0          | 0    | 4    | 0        | 3        |
| 1          | 1          | 1    | 1    | 0        | 1        |
| 2          | 1          | 1    | 0    | 1        | 1        |
| 3          | 1          | 0    | 1    | 1        | 1        |
| 4          | 1          | 1    | 1    | 1        | 0        |
+------------+------------+------+------+----------+----------+
Output:
+-------+------+------+----------+----------+
| name  | rest | paid | canceled | refunded |
+-------+------+------+----------+----------+
| bacon | 3    | 3    | 3        | 3        |
| ham   | 2    | 4    | 5        | 3        |
+-------+------+------+----------+----------+
Explanation:
- The amount of money left to pay for bacon is 1 + 1 + 0 + 1 = 3
- The amount of money paid for bacon is 1 + 0 + 1 + 1 = 3
- The amount of money canceled for bacon is 0 + 1 + 1 + 1 = 3
- The amount of money refunded for bacon is 1 + 1 + 1 + 0 = 3
- The amount of money left to pay for ham is 2 + 0 = 2
- The amount of money paid for ham is 0 + 4 = 4
- The amount of money canceled for ham is 5 + 0 = 5
- The amount of money refunded for ham is 0 + 3 = 3
*/

-- NOTE you should be thinking "oh, i should handle null?" even if the
-- question doesn't mention it speicifcally

select P.name
    , coalesce(sum(I.rest), 0) rest
    , coalesce(sum(I.paid), 0) paid
    , coalesce(sum(I.canceled), 0) canceled
    , coalesce(sum(I.refunded), 0) refunded
from Product P
    left join Invoice I
        on I.product_id = P.product_id
group by P.name
order by P.name

/*
602. Friend Requests II: Who Has the Most Friends (Medium)
-- https://leetcode.com/problems/friend-requests-ii:-who-has-the-most-friends/

Write an SQL query to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The query result format is in the following example.

Example 1:

Input:
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output:
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation:
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.

Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?
*/
with cte as(
select requester_id id
from RequestAccepted
union all
select accepter_id id
from RequestAccepted
)
select id
    , count(*) as num
from cte
group by id
order by num desc limit 1; -- TODO how does this work for the general case?

607. Sales Person (Easy)
1068. Product Sales Analysis I (Easy)
-- https://leetcode.com/problems/product-sales-analysis-i
1517. Find Users With Valid E-Mails (Easy)
-- https://leetcode.com/problems/find-users-with-valid-e-mails
/*
574. Winning Candidate (Medium)
-- https://leetcode.com/problems/winning-candidate/
Write an SQL query to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).

The test cases are generated so that exactly one candidate wins the elections.

The query result format is in the following example.

Example 1:

Input:
Candidate table:
+----+------+
| id | name |
+----+------+
| 1  | A    |
| 2  | B    |
| 3  | C    |
| 4  | D    |
| 5  | E    |
+----+------+
Vote table:
+----+-------------+
| id | candidateId |
+----+-------------+
| 1  | 2           |
| 2  | 4           |
| 3  | 3           |
| 4  | 2           |
| 5  | 5           |
+----+-------------+
Output:
+------+
| name |
+------+
| B    |
+------+
Explanation:
Candidate B has 2 votes. Candidates C, D, and E have 1 vote each.
The winner is candidate B.
*/
select name from (
select c.name
    , count(v.candidateId) count_votes
from Candidate c
    inner join Vote v
        on c.id = v.candidateId
group by v.candidateId, c.name
order by count_votes desc
limit 1
) _;

/*
1212. Team Scores in Football Tournament (Medium)
-- https://leetcode.com/problems/team-scores-in-football-tournament
You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

The query result format is in the following example.

Example 1:

Input:
Teams table:
+-----------+--------------+
| team_id   | team_name    |
+-----------+--------------+
| 10        | Leetcode FC  |
| 20        | NewYork FC   |
| 30        | Atlanta FC   |
| 40        | Chicago FC   |
| 50        | Toronto FC   |
+-----------+--------------+
Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
+------------+--------------+---------------+-------------+--------------+
| 1          | 10           | 20            | 3           | 0            |
| 2          | 30           | 10            | 2           | 2            |
| 3          | 10           | 50            | 5           | 1            |
| 4          | 20           | 30            | 1           | 0            |
| 5          | 50           | 30            | 1           | 0            |
+------------+--------------+---------------+-------------+--------------+
Output:
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+
*/
SELECT team_id
    , team_name
    , SUM(
        CASE
            WHEN team_id = host_team AND host_goals > guest_goals THEN 3
            WHEN team_id = guest_team AND guest_goals > host_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END
    ) num_points
FROM Teams t
    LEFT JOIN Matches m
        ON t.team_id = m.host_team
        OR t.team_id = m.guest_team
GROUP BY team_id, team_name
ORDER BY num_points DESC, team_id;

/*
1795. Rearrange Products Table (Easy)
-- https://leetcode.com/problems/rearrange-products-table
Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation:
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
*/
-- sauce, wanna put something in every row, ez just do it Nike(R)!
select product_id, 'store1' store, store1 price from Products where store1 is not null
union all
select product_id, 'store2' store, store2 price from Products where store2 is not null
union all
select product_id, 'store3' store, store3 price from Products where store3 is not null

/*
1527. Patients With a Condition (Easy)
-- https://leetcode.com/problems/patients-with-a-condition
Write an SQL query to report the patient_id, patient_name all conditions of patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
+------------+--------------+--------------+
Explanation: Bob and George both have a condition that starts with DIAB1.
*/
select patient_id
    , patient_name
    , conditions
from Patients
where conditions rlike '^DIAB1| DIAB1'
-- where conditions LIKE 'DIAB1%' OR conditions like '% DIAB1%'
-- https://stackoverflow.com/a/67500315/13660563

/*
1532. The Most Recent Three Orders (Medium)
-- https://leetcode.com/problems/the-most-recent-three-orders
Write an SQL query to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. If there is still a tie, order them by order_date in descending order.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+-------------+-----------+
| customer_id | name      |
+-------------+-----------+
| 1           | Winston   |
| 2           | Jonathan  |
| 3           | Annabelle |
| 4           | Marwan    |
| 5           | Khaled    |
+-------------+-----------+
Orders table:
+----------+------------+-------------+------+
| order_id | order_date | customer_id | cost |
+----------+------------+-------------+------+
| 1        | 2020-07-31 | 1           | 30   |
| 2        | 2020-07-30 | 2           | 40   |
| 3        | 2020-07-31 | 3           | 70   |
| 4        | 2020-07-29 | 4           | 100  |
| 5        | 2020-06-10 | 1           | 1010 |
| 6        | 2020-08-01 | 2           | 102  |
| 7        | 2020-08-01 | 3           | 111  |
| 8        | 2020-08-03 | 1           | 99   |
| 9        | 2020-08-07 | 2           | 32   |
| 10       | 2020-07-15 | 1           | 2    |
+----------+------------+-------------+------+
Output:
+---------------+-------------+----------+------------+
| customer_name | customer_id | order_id | order_date |
+---------------+-------------+----------+------------+
| Annabelle     | 3           | 7        | 2020-08-01 |
| Annabelle     | 3           | 3        | 2020-07-31 |
| Jonathan      | 2           | 9        | 2020-08-07 |
| Jonathan      | 2           | 6        | 2020-08-01 |
| Jonathan      | 2           | 2        | 2020-07-30 |
| Marwan        | 4           | 4        | 2020-07-29 |
| Winston       | 1           | 8        | 2020-08-03 |
| Winston       | 1           | 1        | 2020-07-31 |
| Winston       | 1           | 10       | 2020-07-15 |
+---------------+-------------+----------+------------+
Explanation:
Winston has 4 orders, we discard the order of "2020-06-10" because it is the oldest order.
Annabelle has only 2 orders, we return them.
Jonathan has exactly 3 orders.
Marwan ordered only one time.
We sort the result table by customer_name in ascending order, by customer_id in ascending order, and by order_date in descending order in case of a tie.
*/
-- to get top n most recent dates
-- rank order by date desc -> rank <= 3
with temp as(
select name customer_name
    , c.customer_id
    , order_id
    , order_date
    , rank() over(partition by c.customer_id order by order_date desc) `rank` -- sauce
from Customers c
    inner join Orders o
        on c.customer_id = o.customer_id
)
select customer_name
    , customer_id
    , order_id
    , order_date
from temp
where `rank` <= 3
order by customer_name, customer_id, order_date desc

/*
1777. Products Price for Each Store (Easy)
-- https://leetcode.com/problems/products-price-for-each-store/
Write an SQL query to find the price of each product in each store.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
NOTE store is an ENUM of type ('store1', 'store2', 'store3') where each represents the store this product is available at.

Output:
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+

Explanation:
Product 0 price's are 95 for store1, 100 for store2 and, 105 for store3.
Product 1 price's are 70 for store1, 80 for store3 and, it's not sold in store2.
*/
select product_id
    , max(case when store = 'store1' then price else null end) store1
    , max(case when store = 'store2' then price else null end) store2
    , max(case when store = 'store3' then price else null end) store3
from Products
group by product_id

/*
1729. Find Followers Count (Easy)
-- https://leetcode.com/problems/find-followers-count
Write an SQL query that will, for each user, return the number of followers.

Return the result table ordered by user_id.

The query result format is in the following example.

Example 1:

Input:
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
Output:
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
Explanation:
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}
*/
select user_id
    , count(follower_id) followers_count
from Followers
group by user_id
order by user_id

/*
1204. Last Person to Fit in the Bus (Medium)
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/
There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

Write an SQL query to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

The query result format is in the following example.

Example 1:

Input:
Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+
Output:
+-------------+
| person_name |
+-------------+
| John Cena   |
+-------------+
Explanation: The folowing table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (last person to board)
| 4    | 2  | Marie     | 200    | 1200         | (cannot board)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+
*/
with cte as(
select *
    , sum(weight) over(order by turn range between unbounded preceding and current row) as running_total
from Queue
)
select person_name
from cte
where running_total <= 1000
order by running_total desc
limit 1;

/*
534. Game Play Analysis III (Medium)
-- https://leetcode.com/problems/game-play-analysis-iii
Write an SQL query to report for each player and date, how many games played so far by the player. That is, the total number of games played by the player until that date. Check the example for clarity.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 1         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+------------+---------------------+
| player_id | event_date | games_played_so_far |
+-----------+------------+---------------------+
| 1         | 2016-03-01 | 5                   |
| 1         | 2016-05-02 | 11                  |
| 1         | 2017-06-25 | 12                  |
| 3         | 2016-03-02 | 0                   |
| 3         | 2018-07-03 | 5                   |
+-----------+------------+---------------------+
Explanation:
For the player with id 1, 5 + 6 = 11 games played by 2016-05-02, and 5 + 6 + 1 = 12 games played by 2017-06-25.
For the player with id 3, 0 + 5 = 5 games played by 2018-07-03.
Note that for each player we only care about the days when the player logged in.
*/
select player_id
    , event_date
    , sum(games_played) over (partition by player_id order by event_date range between unbounded preceding and current row) as games_played_so_far
from Activity
order by player_id, event_date;

/*
1132. Reported Posts II (Medium)
-- https://leetcode.com/problems/reported-posts-ii
Write an SQL query to find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

The query result format is in the following example.

Example 1:

Input:
Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 2       | 2019-07-04  | view   | null   |
| 2       | 2       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-03  | view   | null   |
| 5       | 2       | 2019-07-03  | report | racism |
| 5       | 5       | 2019-07-03  | view   | null   |
| 5       | 5       | 2019-07-03  | report | racism |
+---------+---------+-------------+--------+--------+
Removals table:
+---------+-------------+
| post_id | remove_date |
+---------+-------------+
| 2       | 2019-07-20  |
| 3       | 2019-07-18  |
+---------+-------------+
Output:
+-----------------------+
| average_daily_percent |
+-----------------------+
| 75.00                 |
+-----------------------+
Explanation:
The percentage for 2019-07-04 is 50% because only one post of two spam reported posts were removed.
The percentage for 2019-07-02 is 100% because one post was reported as spam and it was removed.
The other days had no spam reports so the average is (50 + 100) / 2 = 75%
Note that the output is only one number and that we do not care about the remove dates.
*/
WITH cte AS(
SELECT (COUNT(DISTINCT r.post_id)/ COUNT(DISTINCT a.post_id)) * 100  AS `cnt`
FROM Actions a
    LEFT JOIN Removals r
        ON a.post_id = r.post_id
WHERE extra = 'spam'
GROUP BY action_date
)
SELECT ROUND(AVG(`cnt`), 2) AS `average_daily_percent`
FROM cte;

/*
1211. Queries Quality and Percentage (Easy)
-- https://leetcode.com/problems/queries-quality-and-percentage
We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
Output:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+
Explanation:
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33
*/
SELECT
	query_name,
	ROUND(AVG(rating / position), 2) AS quality,
	ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM
	Queries
GROUP BY
	query_name
;

/*
1149. Article Views II (Medium)
-- https://leetcode.com/problems/article-views-ii
Write an SQL query to find all the people who viewed more than one article on the same date.

Return the result table sorted by id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output:
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
*/
with cte as(
select distinct
    article_id
    , viewer_id
    , view_date
from Views
)
, cte2 as (
select
    viewer_id
    , view_date
from cte
group by view_date, viewer_id
having count(1) > 1
)
select distinct
    viewer_id id
from cte2
order by id
;

SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1 -- secret sauce
ORDER BY 1

/*
1350. Students With Invalid Departments (Easy)
-- https://leetcode.com/problems/students-with-invalid-departments
Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exist.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Departments table:
+------+--------------------------+
| id   | name                     |
+------+--------------------------+
| 1    | Electrical Engineering   |
| 7    | Computer Engineering     |
| 13   | Bussiness Administration |
+------+--------------------------+
Students table:
+------+----------+---------------+
| id   | name     | department_id |
+------+----------+---------------+
| 23   | Alice    | 1             |
| 1    | Bob      | 7             |
| 5    | Jennifer | 13            |
| 2    | John     | 14            |
| 4    | Jasmine  | 77            |
| 3    | Steve    | 74            |
| 6    | Luis     | 1             |
| 8    | Jonathan | 7             |
| 7    | Daiana   | 33            |
| 11   | Madelynn | 1             |
+------+----------+---------------+
Output:
+------+----------+
| id   | name     |
+------+----------+
| 2    | John     |
| 7    | Daiana   |
| 4    | Jasmine  |
| 3    | Steve    |
+------+----------+
Explanation:
John, Daiana, Steve, and Jasmine are enrolled in departments 14, 33, 74, and 77 respectively. department 14, 33, 74, and 77 do not exist in the Departments table.
*/
select
    S.id
    , S.name
from Students S
    left join Departments D
        on S.department_id = D.id
where D.name is null;


select
    S.id
    , S.name
from Students S
where not exists (select id from Departments D where S.department_id = D.id);


select
    S.id
    , S.name
from Students S
where (S.department_id) not in (select id from Departments);


/*
1303. Find the Team Size (Easy)
-- https://leetcode.com/problems/find-the-team-size
Write an SQL query to find the team size of each of the employees.

Return result table in any order.

The query result format is in the following example.



Example 1:

Input:
Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Output:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
Explanation:
Employees with Id 1,2,3 are part of a team with team_id = 8.
Employee with Id 4 is part of a team with team_id = 7.
Employees with Id 5,6 are part of a team with team_id = 9.
*/
select
    employee_id
    , count(employee_id) over(partition by team_id) team_size
from Employee
order by employee_id
;

/*
614. Second Degree Follower (Medium)
A second-degree follower is a user who:

follows at least one user, and
is followed by at least one user.
Write an SQL query to report the second-degree users and the number of their followers.

Return the result table ordered by follower in alphabetical order.

The query result format is in the following example.

Example 1:

Input:
Follow table:
+----------+----------+
| followee | follower |
+----------+----------+
| Alice    | Bob      |
| Bob      | Cena     |
| Bob      | Donald   |
| Donald   | Edward   |
+----------+----------+
Output:
+----------+-----+
| follower | num |
+----------+-----+
| Bob      | 2   |
| Donald   | 1   |
+----------+-----+
Explanation:
User Bob has 2 followers. Bob is a second-degree follower because he follows Alice, so we include him in the result table.
User Donald has 1 follower. Donald is a second-degree follower because he follows Bob, so we include him in the result table.
User Alice has 1 follower. Alice is not a second-degree follower because she does not follow anyone, so we don not include her in the result table.
*/
select
    f1.follower
    , count(distinct f2.follower) as num
from Follow f1
    inner join Follow f2
        on f1.follower = f2.followee
group by f1.follower
order by f1.follower
;

613. Shortest Distance in a Line (Easy)
/*
578. Get Highest Answer Rate Question (Medium)
-- THIS QUESTION IS TRASH, IGNORE IT!
The answer rate for a question is the number of times a user answered the question by
the number of times a user showed the question.

Write an SQL query to report the question that has the highest answer rate. If multiple
questions have the same maximum answer rate, report the question with the smallest
question_id.

Example 1:
Input:
SurveyLog table:
+----+--------+-------------+-----------+-------+-----------+
| id | action | question_id | answer_id | q_num | timestamp |
+----+--------+-------------+-----------+-------+-----------+
| 5  | show   | 285         | null      | 1     | 123       |
| 5  | answer | 285         | 124124    | 1     | 124       |
| 5  | show   | 369         | null      | 2     | 125       |
| 5  | skip   | 369         | null      | 2     | 126       |
+----+--------+-------------+-----------+-------+-----------+
Output:
+------------+
| survey_log |
+------------+
| 285        |
+------------+
Explanation:
Question 285 was showed 1 time and answered 1 time. The answer rate of question 285 is 1.0
Question 369 was showed 1 time and was not answered. The answer rate of question 369 is 0.0
Question 285 has the highest answer rate.
*/
-- THIS QUESTION IS TRASH, IGNORE IT!
select any_value(question_id) survey_log
from SurveyLog
group by question_id
order by sum(action = 'answer') / (sum(action = 'show') + sum(action = 'answer')) desc, question_id
limit 1


/*
1050. Actors and Directors Who Cooperated At Least Three Times (Easy)
-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times
Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
ActorDirector table:
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
Output:
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.
*/
select
    actor_id
    , director_id
from ActorDirector
group by actor_id, director_id
having count(*) >= 3


/*
1076. Project Employees II (Easy)
-- https://leetcode.com/problems/project-employees-ii
Write an SQL query that reports all the projects that have the most employees.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output:
+-------------+
| project_id  |
+-------------+
| 1           |
+-------------+
Explanation: The first project has 3 employees while the second one has 2.
*/
with cte as (
    select count(employee_id) empcount
    from Project
    group by project_id
    order by empcount desc limit 1
)
select project_id
from Project
group by project_id
having count(employee_id) = (select * from cte);

/*
550. Game Play Analysis IV (Medium)
-- https://leetcode.com/problems/game-play-analysis-iv
Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The query result format is in the following example.

Example 1:

Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation:
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
*/
with cte as (
select
    player_id
    , case
        when datediff(
            event_date
            , min(event_date) over(partition by player_id order by event_date)
        ) = 1 then 1 else 0 end case_1daydiff
from Activity
)
, cte2 as (
select
    player_id
    , sum(case_1daydiff) sum_1daydiff
from cte
group by player_id
)
select round(sum(sum_1daydiff)/count(1), 2) fraction
from cte2;

WITH cte AS(
SELECT
    player_id
    , MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
)
SELECT ROUND(COUNT(t2.player_id) / COUNT(t1.player_id), 2) AS fraction
FROM cte t1
    LEFT JOIN Activity t2
        ON t1.player_id = t2.player_id
        AND t1.first_login = t2.event_date - 1
;


570. Managers with at Least 5 Direct Reports (Medium)
577. Employee Bonus (Easy)
/*
571. Find Median Given Frequency of Numbers (Hard)
The median is the value separating the higher half from the lower half of a data sample.

Write an SQL query to report the median of all the numbers in the database after
decompressing the Numbers table. Round the median to one decimal point.

Example 1:
Input:
Numbers table:
+-----+-----------+
| num | frequency |
+-----+-----------+
| 0   | 7         |
| 1   | 1         |
| 2   | 3         |
| 3   | 1         |
+-----+-----------+
Output:
+--------+
| median |
+--------+
| 0.0    |
+--------+
Explanation:
If we decompress the Numbers table, we will get [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3],
so the median is (0 + 0) / 2 = 0.
*/
-- suppose number x has frequency of n, and total frequency of other numbers that are
-- on its left is l, on its right is r.
--
-- the equation above is (n+l) - (n+r) = l - r, x is median if l==r, of course.
--
-- When l != r, as long as n can cover the difference, x is the median.
select round(avg(N.num), 1) median
from Numbers N
where N.Frequency >= abs((select sum(frequency) from Numbers where num <= N.num) -
                         (select sum(frequency) from Numbers where num >= N.num))


/*
579. Find Cumulative Salary of an Employee (Hard)
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| month       | int  |
| salary      | int  |
+-------------+------+
(id, month) is the primary key for this table.
Each row in the table indicates the salary of an employee in one month during the year 2020.


Write an SQL query to calculate the cumulative salary summary for every employee in a single unified table.

The cumulative salary summary for an employee can be calculated as follows:

For each month that the employee worked, sum up the salaries in that month and the previous two months. This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
Do not include the 3-month sum for any month the employee did not work.
Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
| 1  | 7     | 90     |
| 1  | 8     | 90     |
+----+-------+--------+
Output:
+----+-------+--------+
| id | month | Salary |
+----+-------+--------+
| 1  | 4     | 130    |
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
+----+-------+--------+
Explanation:
Employee '1' has five salary records excluding their most recent month '8':
- 90 for month '7'.
- 60 for month '4'.
- 40 for month '3'.
- 30 for month '2'.
- 20 for month '1'.
So the cumulative salary summary for this employee is:
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 1  | 7     | 90     |  (90 + 0 + 0)
| 1  | 4     | 130    |  (60 + 40 + 30)
| 1  | 3     | 90     |  (40 + 30 + 20)
| 1  | 2     | 50     |  (30 + 20 + 0)
| 1  | 1     | 20     |  (20 + 0 + 0)
+----+-------+--------+
Note that the 3-month sum for month '7' is 90 because they did not work during month '6' or month '5'.

Employee '2' only has one salary record (month '1') excluding their most recent month '2'.
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 2  | 1     | 20     |  (20 + 0 + 0)
+----+-------+--------+

Employee '3' has two salary records excluding their most recent month '4':
- 60 for month '3'.
- 40 for month '2'.
So the cumulative salary summary for this employee is:
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 3  | 3     | 100    |  (60 + 40 + 0)
| 3  | 2     | 40     |  (40 + 0 + 0)
+----+-------+--------+
*/
select
    e1.id
    , e1.month month
    , sum(e2.salary) salary
from Employee e1
    inner join Employee e2
        on e1.id =  e2.id
        and (e1.Month - e2.Month) between 0 and 2 -- sauce
where (e1.id, e1.month) not in (select id,max(month) from Employee group by id)
group by e1.id, e1.month
order by e1.id, e1.month desc


/*
580. Count Student Number in Departments (Medium)
Write an SQL query to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

The query result format is in the following example.

Example 1:

Input:
Student table:
+------------+--------------+--------+---------+
| student_id | student_name | gender | dept_id |
+------------+--------------+--------+---------+
| 1          | Jack         | M      | 1       |
| 2          | Jane         | F      | 1       |
| 3          | Mark         | M      | 2       |
+------------+--------------+--------+---------+
Department table:
+---------+-------------+
| dept_id | dept_name   |
+---------+-------------+
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |
+---------+-------------+
Output:
+-------------+----------------+
| dept_name   | student_number |
+-------------+----------------+
| Engineering | 2              |
| Science     | 1              |
| Law         | 0              |
+-------------+----------------+
*/
with cte as (
select
    d.dept_name
    , count(student_name) over(partition by s.dept_id) as student_number
from Department d
    left join Student s
        on d.dept_id = s.dept_id
)
select distinct
    dept_name
    , student_number
from cte
order by student_number desc, dept_name
;

584. Find Customer Referee (Easy)
619. Biggest Single Number (Easy)
/*
1045. Customers Who Bought All Products (Medium)
-- https://leetcode.com/problems/customers-who-bought-all-products
Write an SQL query to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation:
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
*/
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from product)
;

/*
1069. Product Sales Analysis II (Easy)
-- https://leetcode.com/problems/product-sales-analysis-ii
Write an SQL query that reports the total quantity sold for every product id.

Return the resulting table in any order.

The query result format is in the following example.



Example 1:

Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output:
+--------------+----------------+
| product_id   | total_quantity |
+--------------+----------------+
| 100          | 22             |
| 200          | 15             |
+--------------+----------------+
*/
select
    -- *
    product_id
    , sum(quantity) as total_quantity
from Sales
group by product_id
;
/*
1070. Product Sales Analysis III (Medium)
-- https://leetcode.com/problems/product-sales-analysis-iii
Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The query result format is in the following example.

Example 1:

Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
*/
WITH cte AS(
SELECT
    product_id
    , MIN(year) as year
FROM Sales
GROUP BY product_id
)
SELECT
    product_id
    , year AS first_year
    , quantity
    , price
FROM Sales
WHERE (product_id, year) IN (select * from cte)
;

-- i like this one
with cte as (
select
    *
    , rank() over(partition by product_id order by year) year_rnk
from Sales
)
select
    product_id
    , year as first_year
    , quantity
    , price
from cte tbl
where year_rnk = 1


/*
1075. Project Employees I (Easy)
-- https://leetcode.com/problems/project-employees-i
Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output:
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50
*/

select
    project_id
    , round(avg(experience_years)/1, 2) as `average_years`
from Employee e
    inner join Project p on e.employee_id = p.employee_id
group by p.project_id
;

/*
1082. Sales Analysis I (Easy)
-- https://leetcode.com/problems/product-sales-analysis-i
Write an SQL query that reports the best seller by total sales price, If there is a tie, report them all.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
Output:
+-------------+
| seller_id   |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Both sellers with id 1 and 3 sold products with the most total price of 2800.
*/
with cte1 as (
    select
        seller_id
        , rank() over(order by sum(price) desc) as `seller_rank`
    from Sales s
    group by seller_id
)
select seller_id
from cte1
where `seller_rank` = 1
;

/*
1084. Sales Analysis III (Easy)
-- https://leetcode.com/problems/product-sales-analysis-iii
Write an SQL query that reports the products that were only sold in the spring of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
Output:
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
Explanation:
The product with id 1 was only sold in the spring of 2019.
The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
The product with id 3 was sold after spring 2019.
We return only product 1 as it is the product that was only sold in the spring of 2019.
*/
SELECT
    s.product_id
    , ANY_VALUE(product_name) product_name
FROM Sales s
    INNER JOIN Product p
        ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(sale_date) >= DATE '2019-01-01'
    AND MAX(sale_date) <=  DATE '2019-03-31'

512. Game Play Analysis II (Easy)
-- https://leetcode.com/problems/game-play-analysis-ii
/*
1098. Unpopular Books (Medium)
-- https://leetcode.com/problems/unpopular-books
Write an SQL query that reports the books that have sold less than 10 copies in the last year, excluding books that have been available for less than one month from today. Assume today is 2019-06-23.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Books table:
+---------+--------------------+----------------+
| book_id | name               | available_from |
+---------+--------------------+----------------+
| 1       | "Kalila And Demna" | 2010-01-01     |
| 2       | "28 Letters"       | 2012-05-12     |
| 3       | "The Hobbit"       | 2019-06-10     |
| 4       | "13 Reasons Why"   | 2019-06-01     |
| 5       | "The Hunger Games" | 2008-09-21     |
+---------+--------------------+----------------+
Orders table:
+----------+---------+----------+---------------+
| order_id | book_id | quantity | dispatch_date |
+----------+---------+----------+---------------+
| 1        | 1       | 2        | 2018-07-26    |
| 2        | 1       | 1        | 2018-11-05    |
| 3        | 3       | 8        | 2019-06-11    |
| 4        | 4       | 6        | 2019-06-05    |
| 5        | 4       | 5        | 2019-06-20    |
| 6        | 5       | 9        | 2009-02-02    |
| 7        | 5       | 8        | 2010-04-13    |
+----------+---------+----------+---------------+
Output:
+-----------+--------------------+
| book_id   | name               |
+-----------+--------------------+
| 1         | "Kalila And Demna" |
| 2         | "28 Letters"       |
| 5         | "The Hunger Games" |
+-----------+--------------------+
*/
WITH cte AS(
    SELECT book_id
    FROM Orders
    WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
    GROUP BY book_id
    HAVING SUM(quantity) >= 10
    )
SELECT book_id,
       name
FROM Books
WHERE available_from < '2019-05-23'
AND book_id NOT IN (SELECT book_id FROM cte);

/*
1107. New Users Daily Count (Medium)
-- https://leetcode.com/problems/new-users-daily-count
Write an SQL query to reports for every date within at most 90 days from today, the number of users that logged in for the first time on that date. Assume today is 2019-06-30.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Traffic table:
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+
Output:
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+
Explanation:
Note that we only care about dates with non zero user count.
The user with id 5 first logged in on 2019-03-01 so he's not counted on 2019-06-21.
*/
with cte as(
select
    user_id
    , min(activity_date) as first_login
from Traffic
where activity = 'login'
group by user_id
having datediff('2019-06-30', min(activity_date)) <= 90
)
select
    first_login as login_date
    , count(user_id) as user_count
from cte
group by first_login
;

1126. Active Businesses (Medium)
-- https://leetcode.com/problems/active-businesses
1127. User Purchase Platform (Hard)
-- https://leetcode.com/problems//user-purchase-platform
/*
1141. User Activity for the Past 30 Days I (Easy)
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i
Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
Output:
+------------+--------------+
| day        | active_users |
+------------+--------------+
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+
Explanation: Note that we do not care about days with zero active users.
*/
with T as (
select
    user_id
    , activity_date
from Activity
where datediff(date '2019-07-27', activity_date) < 30
group by user_id, activity_date
)
select
    activity_date day
    , count(user_id) active_users
from T
group by activity_date


/*
1148. Article Views I (Easy)
-- https://leetcode.com/problems/article-views-i
Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
*/
select distinct
    author_id id
from Views
where author_id = viewer_id
order by id


/*
1158. Market Analysis I (Medium)
-- https://leetcode.com/problems/market-analysis-i
Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
Output:
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
*/
with cte as(
select
    buyer_id
    , count(order_id) orders_in_2019
from Orders
where extract(year from order_date) = 2019
group by buyer_id
)
select
    u.user_id buyer_id
    , u.join_date
    , coalesce(cte.orders_in_2019, 0) orders_in_2019
from Users u
    left join cte
        on u.user_id = cte.buyer_id;

SELECT
    u.user_id AS buyer_id
    , join_date
    , COALESCE(COUNT(order_date), 0) AS orders_in_2019
FROM Users u
    LEFT JOIN Orders o
        ON u.user_id = o.buyer_id
        AND YEAR(order_date) = '2019' -- secret sauce
GROUP BY u.user_id, join_date;

/*
1173. Immediate Food Delivery I (Easy)
-- https://leetcode.com/problems/immediate-food-delivery-i
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

The query result format is in the following example.

Example 1:

Input:
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
Output:
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
Explanation: The orders with delivery id 2 and 3 are immediate while the others are scheduled.
*/
select round(sum(order_date = customer_pref_delivery_date) / count(1) * 100, 2) immediate_percentage
from Delivery


/*
1174. Immediate Food Delivery II (Medium)
-- https://leetcode.com/problems/immediate-food-delivery-ii
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write an SQL query to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The query result format is in the following example.

Example 1:

Input:
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
Output:
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
Explanation:
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.
*/
with cte as(
    select
        *
        , rank() over(partition by customer_id order by order_date) rank_order
        , order_date = customer_pref_delivery_date as case_immediate
    from Delivery
)
select round((sum(case_immediate = 1)/count(case_immediate)*100), 2)  immediate_percentage
from cte
where rank_order = 1
;

/*
1193. Monthly Transactions I (Medium)
-- https://leetcode.com/problems/monthly-transactions-i
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
*/
SELECT
    SUBSTRING(trans_date, 1, 7) month
    , country
    , COUNT(id) trans_count
    , SUM(state = 'approved') approved_count -- notice how this is SUM not COUNT, count counts both 0 and 1
    , SUM(amount) trans_total_amount
    , SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) approved_total_amount
FROM Transactions
GROUP BY month, country


1194. Tournament Winners (Hard)
-- https://leetcode.com/problems/tournament-winners
/*
1251. Average Selling Price (Easy)
-- https://leetcode.com/problems/average-selling-price
Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
Output:
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
Explanation:
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
*/
SELECT
    Prices.product_id
    , IF(SUM(UnitsSold.units) IS NOT NULL
        , ROUND(SUM(UnitsSold.units * Prices.price) / SUM(UnitsSold.units), 2)
        , 0) AS average_price
FROM Prices
    LEFT JOIN UnitsSold
        ON Prices.product_id = UnitsSold.product_id
        AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
GROUP BY Prices.product_id
;

/*
1264. Page Recommendations (Medium)
-- https://leetcode.com/problems/page-recommendations
Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

Return result table in any order without duplicates.

The query result format is in the following example.

Example 1:

Input:
Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
| 1        | 3        |
| 1        | 4        |
| 2        | 3        |
| 2        | 4        |
| 2        | 5        |
| 6        | 1        |
+----------+----------+
Likes table:
+---------+---------+
| user_id | page_id |
+---------+---------+
| 1       | 88      |
| 2       | 23      |
| 3       | 24      |
| 4       | 56      |
| 5       | 11      |
| 6       | 33      |
| 2       | 77      |
| 3       | 77      |
| 6       | 88      |
+---------+---------+
Output:
+------------------+
| recommended_page |
+------------------+
| 23               |
| 24               |
| 56               |
| 33               |
| 77               |
+------------------+
Explanation:
User one is friend with users 2, 3, 4 and 6.
Suggested pages are 23 from user 2, 24 from user 3, 56 from user 3 and 33 from user 6.
Page 77 is suggested from both user 2 and user 3.
Page 88 is not suggested because user 1 already likes it.
*/
with user_likes as(
select page_id
from Likes
where user_id = 1
)
, user_friends as (
select
    case
        when user1_id = 1 then user2_id
        when user2_id = 1 then user1_id
    end user_id
from Friendship
)
select distinct page_id recommended_page
from user_friends
    inner join Likes
        on user_friends.user_id = Likes.user_id
where page_id not in (select * from user_likes)

/*
1280. Students and Examinations (Easy)
-- https://leetcode.com/problems/students-and-examinations
Write an SQL query to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The query result format is in the following example.

Example 1:

Input:
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
Output:
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
Explanation:
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
*/
SELECT
    student_id
    , student_name
    , subject_name
    , count(E.subject_name)
FROM Students
    CROSS JOIN Subjects
    LEFT JOIN Examinations E
        USING (student_id, subject_name)
GROUP BY student_id, subject_name, student_name
ORDER BY student_id, subject_name, student_name


/*
1294. Weather Type in Each Country (Easy)
-- https://leetcode.com/problems/weather-type-in-each-country
Write an SQL query to find the type of weather in each country for November 2019.

The type of weather is:

Cold if the average weather_state is less than or equal 15,
Hot if the average weather_state is greater than or equal to 25, and
Warm otherwise.
Return result table in any order.

The query result format is in the following example.

Example 1:

Input:
Countries table:
+------------+--------------+
| country_id | country_name |
+------------+--------------+
| 2          | USA          |
| 3          | Australia    |
| 7          | Peru         |
| 5          | China        |
| 8          | Morocco      |
| 9          | Spain        |
+------------+--------------+
Weather table:
+------------+---------------+------------+
| country_id | weather_state | day        |
+------------+---------------+------------+
| 2          | 15            | 2019-11-01 |
| 2          | 12            | 2019-10-28 |
| 2          | 12            | 2019-10-27 |
| 3          | -2            | 2019-11-10 |
| 3          | 0             | 2019-11-11 |
| 3          | 3             | 2019-11-12 |
| 5          | 16            | 2019-11-07 |
| 5          | 18            | 2019-11-09 |
| 5          | 21            | 2019-11-23 |
| 7          | 25            | 2019-11-28 |
| 7          | 22            | 2019-12-01 |
| 7          | 20            | 2019-12-02 |
| 8          | 25            | 2019-11-05 |
| 8          | 27            | 2019-11-15 |
| 8          | 31            | 2019-11-25 |
| 9          | 7             | 2019-10-23 |
| 9          | 3             | 2019-12-23 |
+------------+---------------+------------+
Output:
+--------------+--------------+
| country_name | weather_type |
+--------------+--------------+
| USA          | Cold         |
| Australia    | Cold         |
| Peru         | Hot          |
| Morocco      | Hot          |
| China        | Warm         |
+--------------+--------------+
Explanation:
Average weather_state in USA in November is (15) / 1 = 15 so weather type is Cold.
Average weather_state in Austraila in November is (-2 + 0 + 3) / 3 = 0.333 so weather type is Cold.
Average weather_state in Peru in November is (25) / 1 = 25 so the weather type is Hot.
Average weather_state in China in November is (16 + 18 + 21) / 3 = 18.333 so weather type is Warm.
Average weather_state in Morocco in November is (25 + 27 + 31) / 3 = 27.667 so weather type is Hot.
We know nothing about the average weather_state in Spain in November so we do not include it in the result table.
*/
select
    c.country_name
    , case
        when avg(w.weather_state) <= 15 then 'Cold'
        when avg(w.weather_state) >= 25 then 'Hot'
        else 'Warm'
    end weather_type
from Weather w
    inner join Countries c
        on w.country_id = c.country_id
where left(day, 7) = '2019-11'
group by c.country_name


/*
1308. Running Total for Different Genders (Medium)
-- https://leetcode.com/problems/running-total-for-different-genders
Write an SQL query to find the total score for each gender on each day.

Return the result table ordered by gender and day in ascending order.

The query result format is in the following example.

Example 1:

Input:
Scores table:
+-------------+--------+------------+--------------+
| player_name | gender | day        | score_points |
+-------------+--------+------------+--------------+
| Aron        | F      | 2020-01-01 | 17           |
| Alice       | F      | 2020-01-07 | 23           |
| Bajrang     | M      | 2020-01-07 | 7            |
| Khali       | M      | 2019-12-25 | 11           |
| Slaman      | M      | 2019-12-30 | 13           |
| Joe         | M      | 2019-12-31 | 3            |
| Jose        | M      | 2019-12-18 | 2            |
| Priya       | F      | 2019-12-31 | 23           |
| Priyanka    | F      | 2019-12-30 | 17           |
+-------------+--------+------------+--------------+
Output:
+--------+------------+-------+
| gender | day        | total |
+--------+------------+-------+
| F      | 2019-12-30 | 17    |
| F      | 2019-12-31 | 40    |
| F      | 2020-01-01 | 57    |
| F      | 2020-01-07 | 80    |
| M      | 2019-12-18 | 2     |
| M      | 2019-12-25 | 13    |
| M      | 2019-12-30 | 26    |
| M      | 2019-12-31 | 29    |
| M      | 2020-01-07 | 36    |
+--------+------------+-------+
Explanation:
For the female team:
The first day is 2019-12-30, Priyanka scored 17 points and the total score for the team is 17.
The second day is 2019-12-31, Priya scored 23 points and the total score for the team is 40.
The third day is 2020-01-01, Aron scored 17 points and the total score for the team is 57.
The fourth day is 2020-01-07, Alice scored 23 points and the total score for the team is 80.

For the male team:
The first day is 2019-12-18, Jose scored 2 points and the total score for the team is 2.
The second day is 2019-12-25, Khali scored 11 points and the total score for the team is 13.
The third day is 2019-12-30, Slaman scored 13 points and the total score for the team is 26.
The fourth day is 2019-12-31, Joe scored 3 points and the total score for the team is 29.
The fifth day is 2020-01-07, Bajrang scored 7 points and the total score for the team is 36.
*/
select
    gender
    , day
    , sum(score_points) over(partition by gender order by day range between unbounded preceding and current row) as total
from Scores
order by gender, day
;

/*
1321. Restaurant Growth (Medium)
-- https://leetcode.com/problems/restaurant-growth
You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Write an SQL query to compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

Return result table ordered by visited_on in ascending order.

The query result format is in the following example.

Example 1:

Input:
Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         |
| 6           | Elvis        | 2019-01-06   | 140         |
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         |
| 1           | Jhon         | 2019-01-10   | 130         |
| 3           | Jade         | 2019-01-10   | 150         |
+-------------+--------------+--------------+-------------+
Output:
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+
Explanation:
1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86
*/
with cte as(
select
    *
    , sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as sum_amount
    , dense_rank() over(order by visited_on) as dr_days
from Customer
)
select distinct
    visited_on
    , sum_amount amount
    , round(sum_amount/7, 2) average_amount
from cte
where dr_days >= 7
;
/*
1327. List the Products Ordered in a Period (Easy)
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period
Write an SQL query to get the names of products that have at least 100 units ordered in February 2020 and their amount.

Return result table in any order.

The query result format is in the following example.

Example 1:

Input:
Products table:
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
Orders table:
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+
Output:
+--------------------+---------+
| product_name       | unit    |
+--------------------+---------+
| Leetcode Solutions | 130     |
| Leetcode Kit       | 100     |
+--------------------+---------+
Explanation:
Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
Products with product_id = 2 is ordered in February a total of 80.
Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
Products with product_id = 4 was not ordered in February 2020.
Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.
*/
select
    P.product_name
    , sum(O.unit) unit
from Orders O
    inner join Products P
        using (product_id)
where left(O.order_date, 7) = '2020-02'
group by product_name
having unit >= 100


/*
1341. Movie Rating (Medium)
-- https://leetcode.com/problems/movie-rating
Write an SQL query to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
The query result format is in the following example.

Example 1:

Input:
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  |
| 2           | 2            | 2            | 2020-02-01  |
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  |
| 3           | 2            | 4            | 2020-02-25  |
+-------------+--------------+--------------+-------------+
Output:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
Explanation:
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
*/
with cte_movie as (
    select title from(
    select distinct
        title
        , avg(rating) over(partition by mr.movie_id) avg_rating
    from MovieRating mr
        inner join Movies m
            on mr.movie_id = m.movie_id
    where extract(year from created_at) = 2020
        and extract(month from created_at) = 2
    order by avg_rating desc, title
    limit 1) _
    )
    , cte_rating as(
    select name from(
    select distinct
        mr.user_id
        , name
        , count(mr.rating) count_rating
    from MovieRating mr
        inner join Users u
            on mr.user_id = u.user_id
    group by u.name, mr.user_id
    order by count_rating desc, name
    limit 1) _
    )
select title as results from cte_movie
    union all
select name from cte_rating;

(
  SELECT u.name AS results
  FROM MovieRating r LEFT JOIN Users u
  ON (r.user_id = u.user_id)
  GROUP BY r.user_id, u.name
  ORDER BY COUNT(r.movie_id) DESC, u.name
  LIMIT 1
)
UNION ALL
(
  SELECT m.title AS results
  FROM MovieRating r LEFT JOIN Movies m
  ON (r.movie_id = m.movie_id)
  WHERE r.created_at LIKE '2020-02%'
  GROUP BY r.movie_id, m.title
  ORDER BY AVG(r.rating) DESC, m.title
  LIMIT 1
);

/*
1355. Activity Participants (Medium)
-- https://leetcode.com/problems/activity-participants
Write an SQL query to find the names of all the activities with neither the maximum nor the minimum number of participants.

Each activity in the Activities table is performed by any person in the table Friends.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Friends table:
+------+--------------+---------------+
| id   | name         | activity      |
+------+--------------+---------------+
| 1    | Jonathan D.  | Eating        |
| 2    | Jade W.      | Singing       |
| 3    | Victor J.    | Singing       |
| 4    | Elvis Q.     | Eating        |
| 5    | Daniel A.    | Eating        |
| 6    | Bob B.       | Horse Riding  |
+------+--------------+---------------+
Activities table:
+------+--------------+
| id   | name         |
+------+--------------+
| 1    | Eating       |
| 2    | Singing      |
| 3    | Horse Riding |
+------+--------------+
Output:
+--------------+
| activity     |
+--------------+
| Singing      |
+--------------+
Explanation:
Eating activity is performed by 3 friends, maximum number of participants, (Jonathan D. , Elvis Q. and Daniel A.)
Horse Riding activity is performed by 1 friend, minimum number of participants, (Bob B.)
Singing is performed by 2 friends (Victor J. and Jade W.)
*/
with cte as (
select distinct
    activity
    , count(activity) over(partition by activity) count_activity
from Friends
)
select activity
from cte
where count_activity <> (select max(count_activity) from cte)
    and count_activity <> (select min(count_activity) from cte)


/*
1364. Number of Trusted Contacts of a Customer (Medium)
-- https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer
Write an SQL query to find the following for each invoice_id:
    * customer_name: The name of the customer the invoice is related to.
    * price: The price of the invoice.
    * contacts_cnt: The number of contacts related to the customer.
    * trusted_contacts_cnt: The number of contacts related to the customer and at the same
    time they are customers to the shop. (i.e their email exists in the Customers table.)

Return the result table ordered by invoice_id.

The query result format is in the following example.

Example 1:

Input:
Customers table:
+-------------+---------------+--------------------+
| customer_id | customer_name | email              |
+-------------+---------------+--------------------+
| 1           | Alice         | alice@leetcode.com |
| 2           | Bob           | bob@leetcode.com   |
| 13          | John          | john@leetcode.com  |
| 6           | Alex          | alex@leetcode.com  |
+-------------+---------------+--------------------+
Contacts table:
+-------------+--------------+--------------------+
| user_id     | contact_name | contact_email      |
+-------------+--------------+--------------------+
| 1           | Bob          | bob@leetcode.com   |
| 1           | John         | john@leetcode.com  |
| 1           | Jal          | jal@leetcode.com   |
| 2           | Omar         | omar@leetcode.com  |
| 2           | Meir         | meir@leetcode.com  |
| 6           | Alice        | alice@leetcode.com |
+-------------+--------------+--------------------+
Invoices table:
+------------+-------+---------+
| invoice_id | price | user_id |
+------------+-------+---------+
| 77         | 100   | 1       |
| 88         | 200   | 1       |
| 99         | 300   | 2       |
| 66         | 400   | 2       |
| 55         | 500   | 13      |
| 44         | 60    | 6       |
+------------+-------+---------+
Output:
+------------+---------------+-------+--------------+----------------------+
| invoice_id | customer_name | price | contacts_cnt | trusted_contacts_cnt |
+------------+---------------+-------+--------------+----------------------+
| 44         | Alex          | 60    | 1            | 1                    |
| 55         | John          | 500   | 0            | 0                    |
| 66         | Bob           | 400   | 2            | 0                    |
| 77         | Alice         | 100   | 3            | 2                    |
| 88         | Alice         | 200   | 3            | 2                    |
| 99         | Bob           | 300   | 2            | 0                    |
+------------+---------------+-------+--------------+----------------------+
Explanation:
Alice has three contacts, two of them are trusted contacts (Bob and John).
Bob has two contacts, none of them is a trusted contact.
Alex has one contact and it is a trusted contact (Alice).
John doesn't have any contacts.
*/
WITH cte AS (
SELECT user_id
	, COUNT(contact_email) contacts_cnt
	, SUM(contact_email IN (SELECT email FROM Customers)) trusted_contacts_cnt
FROM Contacts
GROUP BY user_id
)
SELECT i.invoice_id
	, c.customer_name
	, i.price
	, IFNULL(contacts_cnt, 0) contacts_cnt
	, IFNULL(trusted_contacts_cnt, 0) trusted_contacts_cnt
FROM Invoices i
	LEFT JOIN Customers c
		ON i.user_id = c.customer_id
	LEFT JOIN cte
		ON i.user_id = cte.user_id
ORDER BY i.invoice_id;

/*
1378. Replace Employee ID With The Unique Identifier (Easy)
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

Write an SQL query to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation:
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
*/
select EUNI.unique_id
    , E.name
from Employees E
    left join EmployeeUNI EUNI
        on E.id = EUNI.id


/*
1393. Capital Gain/Loss (Medium)
-- https://leetcode.com/problems/capital-gainloss
Write an SQL query to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is total gain or loss after buying and selling the stock one or many times.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Stocks table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+
Output:
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+
Explanation:
Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$ and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$. Capital gain/loss is the sum of capital gains/losses for each ('Buy' --> 'Sell') operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.
*/
select
    stock_name
    , sum(case when operation='Buy' then -price else price end) capital_gain_loss
from Stocks
group by stock_name

/*
1407. Top Travellers (Easy)
-- https://leetcode.com/problems/top-travellers
Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 7    | Lee       |
| 13   | Jonathan  |
| 19   | Elvis     |
+------+-----------+
Rides table:
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 7        | 100      |
| 5    | 13       | 312      |
| 6    | 19       | 50       |
| 7    | 7        | 120      |
| 8    | 19       | 400      |
| 9    | 7        | 230      |
+------+----------+----------+
Output:
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+
Explanation:
Elvis and Lee traveled 450 miles, Elvis is the top traveler as his name is alphabetically smaller than Lee.
Bob, Jonathan, Alex, and Alice have only one ride and we just order them by the total distances of the ride.
Donald did not have any rides, the distance traveled by him is 0.
*/
with A as (
select
    u.id
    , u.name
    , coalesce(sum(r.distance) ,0) travelled_distance
from Users u
    left join Rides r
        on u.id = r.user_id
group by u.name, u.id
order by travelled_distance desc, u.name
)
select name, travelled_distance from A;

/*
1421. NPV Queries (Medium)
-- https://leetcode.com/problems/npv-queries
Write an SQL query to find the npv of each query of the Queries table.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
NPV table:
+------+--------+--------+
| id   | year   | npv    |
+------+--------+--------+
| 1    | 2018   | 100    |
| 7    | 2020   | 30     |
| 13   | 2019   | 40     |
| 1    | 2019   | 113    |
| 2    | 2008   | 121    |
| 3    | 2009   | 12     |
| 11   | 2020   | 99     |
| 7    | 2019   | 0      |
+------+--------+--------+
Queries table:
+------+--------+
| id   | year   |
+------+--------+
| 1    | 2019   |
| 2    | 2008   |
| 3    | 2009   |
| 7    | 2018   |
| 7    | 2019   |
| 7    | 2020   |
| 13   | 2019   |
+------+--------+
Output:
+------+--------+--------+
| id   | year   | npv    |
+------+--------+--------+
| 1    | 2019   | 113    |
| 2    | 2008   | 121    |
| 3    | 2009   | 12     |
| 7    | 2018   | 0      |
| 7    | 2019   | 0      |
| 7    | 2020   | 30     |
| 13   | 2019   | 40     |
+------+--------+--------+
Explanation:
The npv value of (7, 2018) is not present in the NPV table, we consider it 0.
The npv values of all other queries can be found in the NPV table.
*/
select
    Q.id
    , Q.year
    , coalesce(N.npv , 0) npv
from Queries Q
    left join NPV N
        on Q.id = N.id
        and Q.year = N.year


/*
1435. Create a Session Bar Chart (Easy)
-- https://leetcode.com/problems/create-a-session-bar-chart
You want to know how long a user visits your application. You decided to create bins of "[0-5>", "[5-10>", "[10-15>", and "15 minutes or more" and count the number of sessions on it.

Write an SQL query to report the (bin, total).

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Sessions table:
+-------------+---------------+
| session_id  | duration      |
+-------------+---------------+
| 1           | 30            |
| 2           | 199           |
| 3           | 299           |
| 4           | 580           |
| 5           | 1000          |
+-------------+---------------+
Output:
+--------------+--------------+
| bin          | total        |
+--------------+--------------+
| [0-5>        | 3            |
| [5-10>       | 1            |
| [10-15>      | 0            |
| 15 or more   | 1            |
+--------------+--------------+
Explanation:
For session_id 1, 2, and 3 have a duration greater or equal than 0 minutes and less than 5 minutes.
For session_id 4 has a duration greater or equal than 5 minutes and less than 10 minutes.
There is no session with a duration greater than or equal to 10 minutes and less than 15 minutes.
For session_id 5 has a duration greater than or equal to 15 minutes.
*/

with
  cte as(
    select
      session_id
      , duration/60 as durMin
    from Sessions)
  , bins as(
    select '[0-5>' as bin union
    select '[5-10>' union
    select '[10-15>' union
    select '15 or more'
  )
  , durations as(
    select
      case
        when durMin >= 0 and durMin < 5 then '[0-5>'
        when durMin >= 5 and durMin < 10 then '[5-10>'
        when durMin >= 10 and durMin < 15 then '[10-15>'
        else '15 or more'
      end as duration
    from cte
  )

select
  bin,
  count(durations.duration) as `total`
from bins
  left outer join durations on bins.bin = durations.duration
group by bin;

/*
1440. Evaluate Boolean Expression (Medium)
-- https://leetcode.com/problems/evaluate-boolean-expression
Write an SQL query to evaluate the boolean expressions in Expressions table.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Variables table:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+
Expressions table:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+
Output:
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
Explanation:
As shown, you need to find the value of each boolean expression in the table using the variables table.
*/
select
    e.left_operand
    , e.operator
    , e.right_operand
    , case
        when operator = '>' then if(v_left.value > v_right.value, 'true', 'false')
        when operator = '<' then if(v_left.value < v_right.value, 'true', 'false')
        else if(v_left.value = v_right.value, 'true', 'false')
    end value
from Expressions e
    inner join Variables v_left
        on left_operand = v_left.name
    inner join Variables v_right
        on right_operand = v_right.name


/*
1445. Apples & Oranges (Medium)
Write an SQL query to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.

The query result format is in the following example.

Example 1:

Input:
Sales table:
+------------+------------+-------------+
| sale_date  | fruit      | sold_num    |
+------------+------------+-------------+
| 2020-05-01 | apples     | 10          |
| 2020-05-01 | oranges    | 8           |
| 2020-05-02 | apples     | 15          |
| 2020-05-02 | oranges    | 15          |
| 2020-05-03 | apples     | 20          |
| 2020-05-03 | oranges    | 0           |
| 2020-05-04 | apples     | 15          |
| 2020-05-04 | oranges    | 16          |
+------------+------------+-------------+
Output:
+------------+--------------+
| sale_date  | diff         |
+------------+--------------+
| 2020-05-01 | 2            |
| 2020-05-02 | 0            |
| 2020-05-03 | 20           |
| 2020-05-04 | -1           |
+------------+--------------+
Explanation:
Day 2020-05-01, 10 apples and 8 oranges were sold (Difference  10 - 8 = 2).
Day 2020-05-02, 15 apples and 15 oranges were sold (Difference 15 - 15 = 0).
Day 2020-05-03, 20 apples and 0 oranges were sold (Difference 20 - 0 = 20).
Day 2020-05-04, 15 apples and 16 oranges were sold (Difference 15 - 16 = -1).
*/
with oranges as(
select *
from Sales
where fruit = 'oranges'
)
, apples as(
select *
from Sales
where fruit = 'apples'
)
select
    oranges.sale_date
    , apples.sold_num - oranges.sold_num as diff
from oranges
    inner join apples
        on oranges.sale_date = apples.sale_date;

select
    sale_date
    , sum(case when fruit='apples' then sold_num else -sold_num end) diff -- XD
from Sales
group by sale_date;

/*
1454. Active Users (Medium)
-- https://leetcode.com/problems/active-users
Active users are those who logged in to their accounts for five or more consecutive days.

Write an SQL query to find the id and the name of active users.

Return the result table ordered by id.

The query result format is in the following example.

Example 1:

Input:
Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+
Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+
Output:
+----+----------+
| id | name     |
+----+----------+
| 7  | Jonathan |
+----+----------+
Explanation:
User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.

Follow up: Could you write a general solution if the active users are those who logged in to their accounts for n or more consecutive days?
*/
SELECT DISTINCT
    l1.id
    , (SELECT name FROM Accounts WHERE id = l1.id) AS name
FROM Logins l1
    INNER JOIN Logins l2
        ON l1.id = l2.id
        AND DATEDIFF(l2.login_date, l1.login_date) BETWEEN 1 AND 4
GROUP BY l1.id, l1.login_date
HAVING COUNT(DISTINCT l2.login_date) = 4
;

/*
1459. Rectangles Area (Medium)
-- https://leetcode.com/problems/rectangles-area
Write an SQL query to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.

Each row in the result should contain three columns (p1, p2, area) where:

p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
area is the area of the rectangle and must be non-zero.
Return the result table ordered by area in descending order. If there is a tie, order them by p1 in ascending order. If there is still a tie, order them by p2 in ascending order.

The query result format is in the following table.

Example 1:

Input:
Points table:
+----------+-------------+-------------+
| id       | x_value     | y_value     |
+----------+-------------+-------------+
| 1        | 2           | 7           |
| 2        | 4           | 8           |
| 3        | 2           | 10          |
+----------+-------------+-------------+
Output:
+----------+-------------+-------------+
| p1       | p2          | area        |
+----------+-------------+-------------+
| 2        | 3           | 4           |
| 1        | 2           | 2           |
+----------+-------------+-------------+
Explanation:
The rectangle formed by p1 = 2 and p2 = 3 has an area equal to |4-2| * |8-10| = 4.
The rectangle formed by p1 = 1 and p2 = 2 has an area equal to |2-4| * |7-8| = 2.
Note that the rectangle formed by p1 = 1 and p2 = 3 is invalid because the area is 0.
*/
select
    P1.id p1
    , P2.id p2
    , (case
        when P1.x_value > P2.x_value then P1.x_value - P2.x_value
        else P2.x_value - P1.x_value
    end) * (case
        when P1.y_value > P2.y_value then P1.y_value - P2.y_value
        else P2.y_value - P1.y_value
    end) area
from Points P1, Points P2
where P1.id <> P2.id
    and P1.id < P2.id
group by 1, 2, area
having area <> 0
order by area desc, p1 asc, p2 asc;


SELECT
    pt1.id P1
    , pt2.id P2
    , ABS(pt2.x_value - pt1.x_value) * ABS(pt2.y_value - pt1.y_value) area
FROM Points pt1
    INNER JOIN Points pt2
        ON pt1.id < pt2.id
        AND pt1.x_value != pt2.x_value
        AND pt2.y_value != pt1.y_value
ORDER BY area DESC, p1, p2;


/*
1468. Calculate Salaries (Medium)
-- https://leetcode.com/problems/calculate-salaries
Write an SQL query to find the salaries of the employees after applying taxes. Round the salary to the nearest integer.

The tax rate is calculated for each company based on the following criteria:

0% If the max salary of any employee in the company is less than $1000.
24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
49% If the max salary of any employee in the company is greater than $10000.
Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Salaries table:
+------------+-------------+---------------+--------+
| company_id | employee_id | employee_name | salary |
+------------+-------------+---------------+--------+
| 1          | 1           | Tony          | 2000   |
| 1          | 2           | Pronub        | 21300  |
| 1          | 3           | Tyrrox        | 10800  |
| 2          | 1           | Pam           | 300    |
| 2          | 7           | Bassem        | 450    |
| 2          | 9           | Hermione      | 700    |
| 3          | 7           | Bocaben       | 100    |
| 3          | 2           | Ognjen        | 2200   |
| 3          | 13          | Nyancat       | 3300   |
| 3          | 15          | Morninngcat   | 7777   |
+------------+-------------+---------------+--------+
Output:
+------------+-------------+---------------+--------+
| company_id | employee_id | employee_name | salary |
+------------+-------------+---------------+--------+
| 1          | 1           | Tony          | 1020   |
| 1          | 2           | Pronub        | 10863  |
| 1          | 3           | Tyrrox        | 5508   |
| 2          | 1           | Pam           | 300    |
| 2          | 7           | Bassem        | 450    |
| 2          | 9           | Hermione      | 700    |
| 3          | 7           | Bocaben       | 76     |
| 3          | 2           | Ognjen        | 1672   |
| 3          | 13          | Nyancat       | 2508   |
| 3          | 15          | Morninngcat   | 5911   |
+------------+-------------+---------------+--------+
Explanation:
For company 1, Max salary is 21300. Employees in company 1 have taxes = 49%
For company 2, Max salary is 700. Employees in company 2 have taxes = 0%
For company 3, Max salary is 7777. Employees in company 3 have taxes = 24%
The salary after taxes = salary - (taxes percentage / 100) * salary
For example, Salary for Morninngcat (3, 15) after taxes = 7777 - 7777 * (24 / 100) = 7777 - 1866.48 = 5910.52, which is rounded to 5911.
*/
with cte as (
select
    *
    , max(salary) over(partition by company_id) max_salary_company
from Salaries
)
select
    company_id
    , employee_id
    , employee_name
    , round(salary -
        case
            when max_salary_company < 1000 then 0
            when max_salary_company >= 1000 and max_salary_company <= 10000 then 0.24 * salary
            else 0.49 * salary
        end, 0) as salary
from cte

/*
1484. Group Sold Products By The Date (Easy)
-- https://leetcode.com/problems/group-sold-products-by-the-date
Write an SQL query to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

The query result format is in the following example.

Example 1:

Input:
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
Output:
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
Explanation:
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.
*/
-- "different products" think -> DISTINCT
select sell_date
    , count(distinct product) num_sold
    , group_concat(distinct product order by product) products
from Activities
group by sell_date

-- btw there's a SEPERATOR clause if you need something like
-- col1|col2|col3
-- mysql> select group_concat(Email order by Email separator '|') from Person;
-- +--------------------------------------------------+
-- | group_concat(Email order by Email separator '|') |
-- +--------------------------------------------------+
-- | bob@example.com|john@example.com                 |
-- +--------------------------------------------------+


/*
1495. Friendly Movies Streamed Last Month (Easy)
-- https://leetcode.com/problems/friendly-movies-streamed-last-month
Write an SQL query to report the distinct titles of the kid-friendly movies streamed in June 2020.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
TVProgram table:
+--------------------+--------------+-------------+
| program_date       | content_id   | channel     |
+--------------------+--------------+-------------+
| 2020-06-10 08:00   | 1            | LC-Channel  |
| 2020-05-11 12:00   | 2            | LC-Channel  |
| 2020-05-12 12:00   | 3            | LC-Channel  |
| 2020-05-13 14:00   | 4            | Disney Ch   |
| 2020-06-18 14:00   | 4            | Disney Ch   |
| 2020-07-15 16:00   | 5            | Disney Ch   |
+--------------------+--------------+-------------+
Content table:
+------------+----------------+---------------+---------------+
| content_id | title          | Kids_content  | content_type  |
+------------+----------------+---------------+---------------+
| 1          | Leetcode Movie | N             | Movies        |
| 2          | Alg. for Kids  | Y             | Series        |
| 3          | Database Sols  | N             | Series        |
| 4          | Aladdin        | Y             | Movies        |
| 5          | Cinderella     | Y             | Movies        |
+------------+----------------+---------------+---------------+
Output:
+--------------+
| title        |
+--------------+
| Aladdin      |
+--------------+
Explanation:
"Leetcode Movie" is not a content for kids.
"Alg. for Kids" is not a movie.
"Database Sols" is not a movie
"Alladin" is a movie, content for kids and was streamed in June 2020.
"Cinderella" was not streamed in June 2020.
*/
select distinct C.title
from TVProgram TVP
    inner join Content C
        using (content_id)
where left(TVP.program_date, 7) = '2020-06'
    and C.Kids_content = 'Y'
    and C.content_type = 'Movies'


/*
1501. Countries You Can Safely Invest In (Medium)
-- https://leetcode.com/problems/countries-you-can-safely-invest-in
A telecommunications company wants to invest in new countries. The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.

Write an SQL query to find the countries where this company can invest.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Person table:
+----+----------+--------------+
| id | name     | phone_number |
+----+----------+--------------+
| 3  | Jonathan | 051-1234567  |
| 12 | Elvis    | 051-7654321  |
| 1  | Moncef   | 212-1234567  |
| 2  | Maroua   | 212-6523651  |
| 7  | Meir     | 972-1234567  |
| 9  | Rachel   | 972-0011100  |
+----+----------+--------------+
Country table:
+----------+--------------+
| name     | country_code |
+----------+--------------+
| Peru     | 051          |
| Israel   | 972          |
| Morocco  | 212          |
| Germany  | 049          |
| Ethiopia | 251          |
+----------+--------------+
Calls table:
+-----------+-----------+----------+
| caller_id | callee_id | duration |
+-----------+-----------+----------+
| 1         | 9         | 33       |
| 2         | 9         | 4        |
| 1         | 2         | 59       |
| 3         | 12        | 102      |
| 3         | 12        | 330      |
| 12        | 3         | 5        |
| 7         | 9         | 13       |
| 7         | 1         | 3        |
| 9         | 7         | 1        |
| 1         | 7         | 7        |
+-----------+-----------+----------+
Output:
+----------+
| country  |
+----------+
| Peru     |
+----------+
Explanation:
The average call duration for Peru is (102 + 102 + 330 + 330 + 5 + 5) / 6 = 145.666667
The average call duration for Israel is (33 + 4 + 13 + 13 + 3 + 1 + 1 + 7) / 8 = 9.37500
The average call duration for Morocco is (33 + 4 + 59 + 59 + 3 + 7) / 6 = 27.5000
Global call duration average = (2 * (33 + 4 + 59 + 102 + 330 + 5 + 13 + 3 + 1 + 7)) / 20 = 55.70000
Since Peru is the only country where the average call duration is greater than the global average, it is the only recommended country.
*/
SELECT co.name AS country
FROM Person p
    INNER JOIN Country co
        ON SUBSTRING(phone_number, 1, 3) = country_code
    INNER JOIN Calls c
        ON p.id IN (c.caller_id, c.callee_id)
GROUP BY co.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls)
;

/*
1543. Fix Product Name Format (Easy)
-- https://leetcode.com/problems/fix-product-name-format
Since table Sales was filled manually in the year 2000, product_name may contain leading and/or trailing white spaces, also they are case-insensitive.

Write an SQL query to report

product_name in lowercase without leading or trailing white spaces.
sale_date in the format ('YYYY-MM').
total the number of times the product was sold in this month.
Return the result table ordered by product_name in ascending order. In case of a tie, order it by sale_date in ascending order.

The query result format is in the following example.

Example 1:

Input:
Sales table:
+---------+--------------+------------+
| sale_id | product_name | sale_date  |
+---------+--------------+------------+
| 1       | LCPHONE      | 2000-01-16 |
| 2       | LCPhone      | 2000-01-17 |
| 3       | LcPhOnE      | 2000-02-18 |
| 4       | LCKeyCHAiN   | 2000-02-19 |
| 5       | LCKeyChain   | 2000-02-28 |
| 6       | Matryoshka   | 2000-03-31 |
+---------+--------------+------------+
Output:
+--------------+-----------+-------+
| product_name | sale_date | total |
+--------------+-----------+-------+
| lckeychain   | 2000-02   | 2     |
| lcphone      | 2000-01   | 2     |
| lcphone      | 2000-02   | 1     |
| matryoshka   | 2000-03   | 1     |
+--------------+-----------+-------+
Explanation:
In January, 2 LcPhones were sold. Please note that the product names are not case sensitive and may contain spaces.
In February, 2 LCKeychains and 1 LCPhone were sold.
In March, one matryoshka was sold.
*/
select lower(trim(product_name)) product_name
    , left(sale_date, 7) sale_date
    , count(sale_id) total
from Sales
-- if you dont do lower(trim(product_name)) or 1 **it refers to the original column**
group by 1, 2 -- sauce
order by 1, 2



/*
1555. Bank Account Summary (Medium)
-- https://leetcode.com/problems/bank-account-summary
Leetcode Bank (LCB) helps its coders in making virtual payments. Our bank records all transactions in the table Transaction, we want to find out the current balance of all users and check whether they have breached their credit limit (If their current credit is less than 0).

Write an SQL query to report.

user_id,
user_name,
credit, current balance after performing transactions, and
credit_limit_breached, check credit_limit ("Yes" or "No")
Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+------------+--------------+-------------+
| user_id    | user_name    | credit      |
+------------+--------------+-------------+
| 1          | Moustafa     | 100         |
| 2          | Jonathan     | 200         |
| 3          | Winston      | 10000       |
| 4          | Luis         | 800         |
+------------+--------------+-------------+
Transactions table:
+------------+------------+------------+----------+---------------+
| trans_id   | paid_by    | paid_to    | amount   | transacted_on |
+------------+------------+------------+----------+---------------+
| 1          | 1          | 3          | 400      | 2020-08-01    |
| 2          | 3          | 2          | 500      | 2020-08-02    |
| 3          | 2          | 1          | 200      | 2020-08-03    |
+------------+------------+------------+----------+---------------+
Output:
+------------+------------+------------+-----------------------+
| user_id    | user_name  | credit     | credit_limit_breached |
+------------+------------+------------+-----------------------+
| 1          | Moustafa   | -100       | Yes                   |
| 2          | Jonathan   | 500        | No                    |
| 3          | Winston    | 9900       | No                    |
| 4          | Luis       | 800        | No                    |
+------------+------------+------------+-----------------------+
Explanation:
Moustafa paid $400 on "2020-08-01" and received $200 on "2020-08-03", credit (100 -400 +200) = -$100
Jonathan received $500 on "2020-08-02" and paid $200 on "2020-08-08", credit (200 +500 -200) = $500
Winston received $400 on "2020-08-01" and paid $500 on "2020-08-03", credit (10000 +400 -500) = $9990
Luis did not received any transfer, credit = $800
*/

-- sauce, dont feel bad to use two ctes for unrelated groupings
with payment as (
select
    paid_by user_id
    , sum(amount) payments
from Transactions
group by 1
)
, received as (
select
    paid_to user_id
    , sum(amount) received
from Transactions
group by 1
)
select
    u.user_id
    , u.user_name
    , (u.credit - coalesce(p.payments, 0) + coalesce(r.received, 0)) credit -- sauce, left means nulls
    , case
        when (u.credit - coalesce(p.payments, 0) + coalesce(r.received, 0)) < 0 then 'Yes'
        else 'No'
    end as credit_limit_breached
from Users u
    left join payment p
        on u.user_id = p.user_id
    left join received r
        on u.user_id = r.user_id


/*
1565. Unique Orders and Customers Per Month (Easy)
-- https://leetcode.com/problems/unique-orders-and-customers-per-month
Write an SQL query to find the number of unique orders and the number of unique customers with invoices > $20 for each different month.

Return the result table sorted in any order.

The query result format is in the following example.

Example 1:

Input:
Orders table:
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | invoice    |
+----------+------------+-------------+------------+
| 1        | 2020-09-15 | 1           | 30         |
| 2        | 2020-09-17 | 2           | 90         |
| 3        | 2020-10-06 | 3           | 20         |
| 4        | 2020-10-20 | 3           | 21         |
| 5        | 2020-11-10 | 1           | 10         |
| 6        | 2020-11-21 | 2           | 15         |
| 7        | 2020-12-01 | 4           | 55         |
| 8        | 2020-12-03 | 4           | 77         |
| 9        | 2021-01-07 | 3           | 31         |
| 10       | 2021-01-15 | 2           | 20         |
+----------+------------+-------------+------------+
Output:
+---------+-------------+----------------+
| month   | order_count | customer_count |
+---------+-------------+----------------+
| 2020-09 | 2           | 2              |
| 2020-10 | 1           | 1              |
| 2020-12 | 2           | 1              |
| 2021-01 | 1           | 1              |
+---------+-------------+----------------+
Explanation:
In September 2020 we have two orders from 2 different customers with invoices > $20.
In October 2020 we have two orders from 1 customer, and only one of the two orders has invoice > $20.
In November 2020 we have two orders from 2 different customers but invoices < $20, so we don't include that month.
In December 2020 we have two orders from 1 customer both with invoices > $20.
In January 2021 we have two orders from 2 different customers, but only one of them with invoice > $20.
*/
select left(order_date, 7) month
    , count(order_id) order_count
    , count(distinct customer_id) customer_count
from Orders
where invoice > 20
group by 1


/*
1581. Customer Who Visited but Did Not Make Any Transactions (Easy)
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions
Write an SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

The query result format is in the following example.

Example 1:

Input:
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
Output:
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
Explanation:
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.
*/
-- you cant count nulls, sum em or just count the whole row
-- this example it's easiest to count the rows
select V.customer_id
    , sum(case when T.transaction_id is null then 1 else 0 end) count_no_trans -- sauce
from Visits V
    left join Transactions T
        on V.visit_id = T.visit_id
where T.transaction_id is null
group by V.customer_id

select V.customer_id
    , count(*) count_no_trans -- sauce
from Visits V
    left join Transactions T
        on V.visit_id = T.visit_id
where T.transaction_id is null
group by V.customer_id



/*
1587. Bank Account Summary II (Easy)
-- https://leetcode.com/problems/bank-account-summary-ii
Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+
Transactions table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+
Output:
+------------+------------+
| name       | balance    |
+------------+------------+
| Alice      | 11000      |
+------------+------------+
Explanation:
Alice's balance is (7000 + 7000 - 3000) = 11000.
Bob's balance is 1000.
Charlie's balance is (6000 + 6000 - 4000) = 8000.
*/
select
    U.name
    , sum(T.amount) balance
from Transactions T
    inner join Users U
        on T.account = U.account
group by T.account, U.name
having balance > 10000



/*
1607. Sellers With No Sales (Easy)
-- https://leetcode.com/problems/sellers-with-no-sales
Write an SQL query to report the names of all sellers who did not make any sales in 2020.

Return the result table ordered by seller_name in ascending order.

The query result format is in the following example.

Example 1:

Input:
Customer table:
+--------------+---------------+
| customer_id  | customer_name |
+--------------+---------------+
| 101          | Alice         |
| 102          | Bob           |
| 103          | Charlie       |
+--------------+---------------+
Orders table:
+-------------+------------+--------------+-------------+-------------+
| order_id    | sale_date  | order_cost   | customer_id | seller_id   |
+-------------+------------+--------------+-------------+-------------+
| 1           | 2020-03-01 | 1500         | 101         | 1           |
| 2           | 2020-05-25 | 2400         | 102         | 2           |
| 3           | 2019-05-25 | 800          | 101         | 3           |
| 4           | 2020-09-13 | 1000         | 103         | 2           |
| 5           | 2019-02-11 | 700          | 101         | 2           |
+-------------+------------+--------------+-------------+-------------+
Seller table:
+-------------+-------------+
| seller_id   | seller_name |
+-------------+-------------+
| 1           | Daniel      |
| 2           | Elizabeth   |
| 3           | Frank       |
+-------------+-------------+
Output:
+-------------+
| seller_name |
+-------------+
| Frank       |
+-------------+
Explanation:
Daniel made 1 sale in March 2020.
Elizabeth made 2 sales in 2020 and 1 sale in 2019.
Frank made 1 sale in 2019 but no sales in 2020.
*/
with T as (
select distinct seller_id
from Orders
where year(sale_date) = 2020
)
select seller_name
from Seller
where seller_id not in (select * from T)
order by seller_name


/*
1623. All Valid Triplets That Can Represent a Country (Easy)
-- https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country
There is a country with three schools, where each student is enrolled in exactly one school. The country is joining a competition and wants to select one student from each school to represent the country such that:

member_A is selected from SchoolA,
member_B is selected from SchoolB,
member_C is selected from SchoolC, and
The selected students' names and IDs are pairwise distinct (i.e. no two students share the same name, and no two students share the same ID).
Write an SQL query to find all the possible triplets representing the country under the given constraints.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
SchoolA table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
+------------+--------------+
SchoolB table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
+------------+--------------+
SchoolC table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
| 2          | Jerry        |
| 10         | Alice        |
+------------+--------------+
Output:
+----------+----------+----------+
| member_A | member_B | member_C |
+----------+----------+----------+
| Alice    | Tom      | Jerry    |
| Bob      | Tom      | Alice    |
+----------+----------+----------+
Explanation:
Let us see all the possible triplets.
- (Alice, Tom, Tom) --> Rejected because member_B and member_C have the same name and the same ID.
- (Alice, Tom, Jerry) --> Valid triplet.
- (Alice, Tom, Alice) --> Rejected because member_A and member_C have the same name.
- (Bob, Tom, Tom) --> Rejected because member_B and member_C have the same name and the same ID.
- (Bob, Tom, Jerry) --> Rejected because member_A and member_C have the same ID.
- (Bob, Tom, Alice) --> Valid triplet.
*/
select A.student_name member_A
    , B.student_name member_B
    , C.student_name member_C
from SchoolA A, SchoolB B, SchoolC C
where A.student_name <> B.student_name
    and B.student_name <> C.student_name
    and A.student_name <> C.student_name
    and A.student_id <> B.student_id
    and B.student_id <> C.student_id
    and A.student_id <> C.student_id


/*
1633. Percentage of Users Attended a Contest (Easy)
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest
Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+
Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
Output:
+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+
Explanation:
All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%
*/
select contest_id
    , round(count(user_id) / (select count(*) from Users) * 100, 2) percentage
from Register
group by contest_id
order by 2 desc, contest_id


1635. Hopper Company Queries I (Hard)
-- https://leetcode.com/problems/hopper-company-queries-i
1645. Hopper Company Queries II (Hard)
-- https://leetcode.com/problems/hopper-company-queries-ii
1661. Average Time of Process per Machine (Easy)
-- https://leetcode.com/problems/average-time-of-process-per-machine
/*
1667. Fix Names in a Table (Easy)
-- https://leetcode.com/problems/fix-names-in-a-table
Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The query result format is in the following example.

Example 1:

Input:
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
*/
select
    user_id
    , concat(upper(left(name, 1)), lower(substring(name, 2))) name
from Users
order by user_id


/*
1683. Invalid Tweets (Easy)
-- https://leetcode.com/problems/invalid-tweets
Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation:
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.
*/
select tweet_id
from Tweets
where char_length(content) > 15  -- sauce, mega gotchya dont use length
-- https://stackoverflow.com/questions/1734334/mysql-length-vs-char-length?rq=1

/*
1693. Daily Leads and Partners (Easy)
-- https://leetcode.com/problems/daily-leads-and-partners
Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
Output:
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+
Explanation:
For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].
*/
select date_id
    , make_name
    , count(distinct lead_id) unique_leads
    , count(distinct partner_id) unique_partners
from DailySales
group by date_id, make_name


/*
1709. Biggest Window Between Visits (Medium)
-- https://leetcode.com/problems/biggest-window-between-visits
Assume today's date is '2021-1-1'.

Write an SQL query that will, for each user_id, find out the largest window of days between each visit and the one right after it (or today if you are considering the last visit).

Return the result table ordered by user_id.

The query result format is in the following example.

Example 1:

Input:
UserVisits table:
+---------+------------+
| user_id | visit_date |
+---------+------------+
| 1       | 2020-11-28 |
| 1       | 2020-10-20 |
| 1       | 2020-12-3  |
| 2       | 2020-10-5  |
| 2       | 2020-12-9  |
| 3       | 2020-11-11 |
+---------+------------+
Output:
+---------+---------------+
| user_id | biggest_window|
+---------+---------------+
| 1       | 39            |
| 2       | 65            |
| 3       | 51            |
+---------+---------------+
Explanation:
For the first user, the windows in question are between dates:
    - 2020-10-20 and 2020-11-28 with a total of 39 days.
    - 2020-11-28 and 2020-12-3 with a total of 5 days.
    - 2020-12-3 and 2021-1-1 with a total of 29 days.
Making the biggest window the one with 39 days.
For the second user, the windows in question are between dates:
    - 2020-10-5 and 2020-12-9 with a total of 65 days.
    - 2020-12-9 and 2021-1-1 with a total of 23 days.
Making the biggest window the one with 65 days.
For the third user, the only window in question is between dates 2020-11-11 and 2021-1-1 with a total of 51 days.
*/
SELECT user_id, MAX(diff) AS biggest_window
FROM
(
	SELECT user_id,
	   DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date), visit_date) AS diff
	FROM UserVisits
) a
GROUP BY user_id
ORDER BY user_id
;

/*
1715. Count Apples and Oranges (Medium)
-- https://leetcode.com/problems/count-apples-and-oranges
Write an SQL query to count the number of apples and oranges in all the boxes. If a box contains a chest, you should also include the number of apples and oranges it has.

The query result format is in the following example.

Example 1:

Input:
Boxes table:
+--------+----------+-------------+--------------+
| box_id | chest_id | apple_count | orange_count |
+--------+----------+-------------+--------------+
| 2      | null     | 6           | 15           |
| 18     | 14       | 4           | 15           |
| 19     | 3        | 8           | 4            |
| 12     | 2        | 19          | 20           |
| 20     | 6        | 12          | 9            |
| 8      | 6        | 9           | 9            |
| 3      | 14       | 16          | 7            |
+--------+----------+-------------+--------------+
Chests table:
+----------+-------------+--------------+
| chest_id | apple_count | orange_count |
+----------+-------------+--------------+
| 6        | 5           | 6            |
| 14       | 20          | 10           |
| 2        | 8           | 8            |
| 3        | 19          | 4            |
| 16       | 19          | 19           |
+----------+-------------+--------------+
Output:
+-------------+--------------+
| apple_count | orange_count |
+-------------+--------------+
| 151         | 123          |
+-------------+--------------+
Explanation:
box 2 has 6 apples and 15 oranges.
box 18 has 4 + 20 (from the chest) = 24 apples and 15 + 10 (from the chest) = 25 oranges.
box 19 has 8 + 19 (from the chest) = 27 apples and 4 + 4 (from the chest) = 8 oranges.
box 12 has 19 + 8 (from the chest) = 27 apples and 20 + 8 (from the chest) = 28 oranges.
box 20 has 12 + 5 (from the chest) = 17 apples and 9 + 6 (from the chest) = 15 oranges.
box 8 has 9 + 5 (from the chest) = 14 apples and 9 + 6 (from the chest) = 15 oranges.
box 3 has 16 + 20 (from the chest) = 36 apples and 7 + 10 (from the chest) = 17 oranges.
Total number of apples = 6 + 24 + 27 + 27 + 17 + 14 + 36 = 151
Total number of oranges = 15 + 25 + 8 + 28 + 15 + 15 + 17 = 123
*/
select
    -- sauce, sum with nulls gotchya 1 + null = null, but we really wanted 1!
    sum(b.apple_count + coalesce(c.apple_count, 0)) apple_count
    , sum(b.orange_count + coalesce(c.orange_count, 0)) orange_count
from Boxes b
    left join Chests c
        on b.chest_id = c.chest_id

/*
1731. The Number of Employees Which Report to Each Employee (Easy)
-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee
For this problem, we will consider a manager an employee who has at least 1 other
employee reporting to them.

Write an SQL query to report the ids and the names of all managers, the number of
employees who report directly to them, and the average age of the reports rounded
to the nearest integer.

Return the result table ordered by employee_id.

The query result format is in the following example.

Example 1:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
Output:
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average
age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
*/
select E1.employee_id
    , E1.name
    , count(*) as reports_count
    , round(avg(E2.age/1)) as average_age
from Employees E1
    inner join Employees E2
        on E1.employee_id = E2.reports_to
group by E1.Employee_id, E1.name
order by E1.employee_id


/*
1747. Leetflex Banned Accounts (Medium)
-- https://leetcode.com/problems/leetflex-banned-accounts
Write an SQL query to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

Return the result table in any order.

Example 1:
Input:
LogInfo table:
+------------+------------+---------------------+---------------------+
| account_id | ip_address | login               | logout              |
+------------+------------+---------------------+---------------------+
| 1          | 1          | 2021-02-01 09:00:00 | 2021-02-01 09:30:00 |
| 1          | 2          | 2021-02-01 08:00:00 | 2021-02-01 11:30:00 |
| 2          | 6          | 2021-02-01 20:30:00 | 2021-02-01 22:00:00 |
| 2          | 7          | 2021-02-02 20:30:00 | 2021-02-02 22:00:00 |
| 3          | 9          | 2021-02-01 16:00:00 | 2021-02-01 16:59:59 |
| 3          | 13         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |
| 4          | 10         | 2021-02-01 16:00:00 | 2021-02-01 17:00:00 |
| 4          | 11         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |
+------------+------------+---------------------+---------------------+
Output:
+------------+
| account_id |
+------------+
| 1          |
| 4          |
+------------+
Explanation:
Account ID 1 --> The account was active from "2021-02-01 09:00:00" to "2021-02-01
09:30:00" with two different IP addresses (1 and 2). It should be banned.
Account ID 2 --> The account was active from two different addresses (6, 7) but in
two different times.
Account ID 3 --> The account was active from two different addresses (9, 13) on
the same day but they do not intersect at any moment.
Account ID 4 --> The account was active from "2021-02-01 17:00:00" to "2021-02-01
17:00:00" with two different IP addresses (10 and 11). It should be banned.
*/
-- A harder version is if it was logged in at time, not just login
select distinct a.account_id
from LogInfo a, LogInfo b
where a.login between (b.login) and (b.logout)
    and a.account_id = b.account_id
    and a.ip_address != b.ip_address


1767. Find the Subtasks That Did Not Execute (Hard)
-- https://leetcode.com/problems/find-the-subtasks-that-did-not-execute
/*
1789. Primary Department for Each Employee (Easy)
-- https://leetcode.com/problems/primary-department-for-each-employee
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.


Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

Write an SQL query to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
Output:
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
Explanation:
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.
*/

select employee_id
    , coalesce(max(case when primary_flag='Y' then department_id else null end)
    , max(department_id)) department_id
from Employee
group by employee_id


-- gotchya! ENUMs sort by index number!
select distinct employee_id
    , first_value(department_id) over(partition by employee_id order by primary_flag) department_id
from Employee


select distinct employee_id
    , first_value(department_id) over(partition by employee_id order by cast(primary_flag as char) desc) department_id
from Employee


select distinct employee_id
    , first_value(department_id) over(partition by employee_id order by field(primary_flag, 'Y', 'N')) department_id
from Employee


/*
1809. Ad-Free Sessions (Easy)
+-------------+------+
| Column Name | Type |
+-------------+------+
| session_id  | int  |
| customer_id | int  |
| start_time  | int  |
| end_time    | int  |
+-------------+------+
session_id is the primary key for this table.
customer_id is the ID of the customer watching this session.
The session runs during the inclusive interval between start_time and end_time.
It is guaranteed that start_time <= end_time and that two sessions for the same customer do not intersect.


Table: Ads

+-------------+------+
| Column Name | Type |
+-------------+------+
| ad_id       | int  |
| customer_id | int  |
| timestamp   | int  |
+-------------+------+
ad_id is the primary key for this table.
customer_id is the ID of the customer viewing this ad.
timestamp is the moment of time at which the ad was shown.


Write an SQL query to report all the sessions that did not get shown any ads.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Playback table:
+------------+-------------+------------+----------+
| session_id | customer_id | start_time | end_time |
+------------+-------------+------------+----------+
| 1          | 1           | 1          | 5        |
| 2          | 1           | 15         | 23       |
| 3          | 2           | 10         | 12       |
| 4          | 2           | 17         | 28       |
| 5          | 2           | 2          | 8        |
+------------+-------------+------------+----------+
Ads table:
+-------+-------------+-----------+
| ad_id | customer_id | timestamp |
+-------+-------------+-----------+
| 1     | 1           | 5         |
| 2     | 2           | 17        |
| 3     | 2           | 20        |
+-------+-------------+-----------+
Output:
+------------+
| session_id |
+------------+
| 2          |
| 3          |
| 5          |
+------------+
Explanation:
The ad with ID 1 was shown to user 1 at time 5 while they were in session 1.
The ad with ID 2 was shown to user 2 at time 17 while they were in session 4.
The ad with ID 3 was shown to user 2 at time 20 while they were in session 4.
We can see that sessions 1 and 4 had at least one ad. Sessions 2, 3, and 5 did not have any ads, so we return them.
*/
select
    P.session_id
    -- , P.customer_id
    -- , P.start_time
    -- , P.end_time
    -- , A.ad_id
    -- , A.timestamp
from Playback P
    left join Ads A
        on P.customer_id = A.customer_id
        and timestamp between start_time and end_time
where A.ad_id is null


/*
1821. Find Customers With Positive Revenue this Year (Easy)
-- https://leetcode.com/problems/find-customers-with-positive-revenue-this-year
Write an SQL query to report the customers with postive revenue in the year 2021.

Return the result table in any order.

The query result format is in the following example.

Input:
Customers table:
+-------------+------+---------+
| customer_id | year | revenue |
+-------------+------+---------+
| 1           | 2018 | 50      |
| 1           | 2021 | 30      |
| 1           | 2020 | 70      |
| 2           | 2021 | -50     |
| 3           | 2018 | 10      |
| 3           | 2016 | 50      |
| 4           | 2021 | 20      |
+-------------+------+---------+
Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 4           |
+-------------+
Explanation:
Customer 1 has revenue equal to 30 in the year 2021.
Customer 2 has revenue equal to -50 in the year 2021.
Customer 3 has no revenue in the year 2021.
Customer 4 has revenue equal to 20 in the year 2021.
Thus only customers 1 and 4 have positive revenue in the year 2021.
*/
select customer_id
from Customers
where year = 2021
    and revenue > 0


/*
1831. Maximum Transaction Each Day (Medium)
-- https://leetcode.com/problems/maximum-transaction-each-day
Write an SQL query to report the IDs of the transactions with the maximum amount on
their respective day. If in one day there are multiple such transactions, return all
of them.

Return the result table ordered by transaction_id in ascending order.

Example 1:
Input:
Transactions table:
+----------------+--------------------+--------+
| transaction_id | day                | amount |
+----------------+--------------------+--------+
| 8              | 2021-4-3 15:57:28  | 57     |
| 9              | 2021-4-28 08:47:25 | 21     |
| 1              | 2021-4-29 13:28:30 | 58     |
| 5              | 2021-4-28 16:39:59 | 40     |
| 6              | 2021-4-29 23:39:28 | 58     |
+----------------+--------------------+--------+
Output:
+----------------+
| transaction_id |
+----------------+
| 1              |
| 5              |
| 6              |
| 8              |
+----------------+
Explanation:
"2021-4-3"  --> We have one transaction with ID 8, so we add 8 to the result table.
"2021-4-28" --> We have two transactions with IDs 5 and 9. The transaction with ID 5
has an amount of 40, while the transaction with ID 9 has an amount of 21. We only
include the transaction with ID 5 as it has the maximum amount this day.
"2021-4-29" --> We have two transactions with IDs 1 and 6. Both transactions have the
same amount of 58, so we include both in the result table.
We order the result table by transaction_id after collecting these IDs.
*/
with T as (
select transaction_id
    , amount
    , day(day) day_day
    , max(amount) over(partition by day(day)) max_amount
from Transactions
)
select transaction_id
from Transactions
where (transaction_id) in (select transaction_id from T where amount = max_amount)
order by transaction_id


/*
1843. Suspicious Bank Accounts (Medium)
-- https://leetcode.com/problems/suspicious-bank-accounts
A bank account is suspicious if the total income exceeds the max_income for this account for two or more consecutive months. The total income of an account in some month is the sum of all its deposits in that month (i.e., transactions of the type 'Creditor').

Write an SQL query to report the IDs of all suspicious bank accounts.

Return the result table ordered by transaction_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Accounts table:
+------------+------------+
| account_id | max_income |
+------------+------------+
| 3          | 21000      |
| 4          | 10400      |
+------------+------------+
Transactions table:
+----------------+------------+----------+--------+---------------------+
| transaction_id | account_id | type     | amount | day                 |
+----------------+------------+----------+--------+---------------------+
| 2              | 3          | Creditor | 107100 | 2021-06-02 11:38:14 |
| 4              | 4          | Creditor | 10400  | 2021-06-20 12:39:18 |
| 11             | 4          | Debtor   | 58800  | 2021-07-23 12:41:55 |
| 1              | 4          | Creditor | 49300  | 2021-05-03 16:11:04 |
| 15             | 3          | Debtor   | 75500  | 2021-05-23 14:40:20 |
| 10             | 3          | Creditor | 102100 | 2021-06-15 10:37:16 |
| 14             | 4          | Creditor | 56300  | 2021-07-21 12:12:25 |
| 19             | 4          | Debtor   | 101100 | 2021-05-09 15:21:49 |
| 8              | 3          | Creditor | 64900  | 2021-07-26 15:09:56 |
| 7              | 3          | Creditor | 90900  | 2021-06-14 11:23:07 |
+----------------+------------+----------+--------+---------------------+
Output:
+------------+
| account_id |
+------------+
| 3          |
+------------+
Explanation:
For account 3:
- In 6-2021, the user had an income of 107100 + 102100 + 90900 = 300100.
- In 7-2021, the user had an income of 64900.
We can see that the income exceeded the max income of 21000 for two consecutive months, so we include 3 in the result table.

For account 4:
- In 5-2021, the user had an income of 49300.
- In 6-2021, the user had an income of 10400.
- In 7-2021, the user had an income of 56300.
We can see that the income exceeded the max income in May and July, but not in June. Since the account did not exceed the max income for two consecutive months, we do not include it in the result table.
*/
WITH T AS (
SELECT
    T.account_id
    , DATE_FORMAT(day, '%Y%m') date -- sauce, this is YYYYMM btw
    , SUM(amount) income
    , A.max_income
FROM Transactions T
    LEFT JOIN Accounts A
        ON A.account_id = T.account_id
WHERE T.type = 'Creditor'
GROUP BY T.account_id, date, A.max_income
HAVING income > A.max_income
)
SELECT t1.account_id
FROM T t1, T t2
WHERE t1.account_id = t2.account_id
    AND PERIOD_DIFF(t1.date, t2.date) = 1 -- sauce, diff in months btw
GROUP BY t1.account_id
ORDER BY t1.account_id

/*
1853. Convert Date Format (Easy)
-- https://leetcode.com/problems/convert-date-format
Write an SQL query to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Days table:
+------------+
| day        |
+------------+
| 2022-04-12 |
| 2021-08-09 |
| 2020-06-26 |
+------------+
Output:
+-------------------------+
| day                     |
+-------------------------+
| Tuesday, April 12, 2022 |
| Monday, August 9, 2021  |
| Friday, June 26, 2020   |
+-------------------------+
Explanation: Please note that the output is case-sensitive.
*/
select
    date_format(day, '%W, %M %e, %Y') day -- sauce, %d is 09, %e is 9
from Days


/*
1873. Calculate Special Bonus (Easy)
-- https://leetcode.com/problems/calculate-special-bonus
Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.

Example 1:

Input:
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
Output:
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
Explanation:
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.
*/
select employee_id
    , case
        when employee_id mod 2 = 1 and name not like 'M%' then salary
        else 0
    end bonus
from Employees


1875. Group Employees of the Same Salary (Medium)
-- https://leetcode.com/problems/group-employees-of-the-same-salary
/*
1890. The Latest Login in 2020 (Easy)
-- https://leetcode.com/problems/the-latest-login-in-2020
Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Logins table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+
Output:
+---------+---------------------+
| user_id | last_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
+---------+---------------------+
Explanation:
User 6 logged into their account 3 times but only once in 2020, so we include this login in the result table.
User 8 logged into their account 2 times in 2020, once in February and once in December. We include only the latest one (December) in the result table.
User 2 logged into their account 2 times but only once in 2020, so we include this login in the result table.
User 14 did not login in 2020, so we do not include them in the result table.
*/
select
    user_id
    , max(time_stamp) last_stamp
from Logins
where year(time_stamp) = 2020
group by user_id


1892. Page Recommendations II (Hard)
-- https://leetcode.com/problems/page-recommendations-ii
/*
1907. Count Salary Categories (Medium)
-- https://leetcode.com/problems/count-salary-categories
Write an SQL query to report the number of bank accounts of each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, then report 0.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation:
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
*/
with cte1 as(
    select
        case
            when income < 20000 then 'Low Salary'
            when income >= 20000 and income <= 50000 then 'Average Salary'
            else 'High Salary'
        end as `category`
    from Accounts
    union all select 'Low Salary' union all select 'Average Salary' union all select 'High Salary'
)
select
    `category`
    , coalesce(count(`category`) - 1) as `accounts_count`
from cte1
group by `category`
;


/*
1917. Leetcodify Friends Recommendations (Hard)
-- https://leetcode.com/problems/leetcodify-friends-recommendations
Table: Listens

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| song_id     | int     |
| day         | date    |
+-------------+---------+
There is no primary key for this table. It may contain duplicates.
Each row of this table indicates that the user user_id listened to the song song_id on the day day.


Table: Friendship

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user1_id      | int     |
| user2_id      | int     |
+---------------+---------+
(user1_id, user2_id) is the primary key for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.


Write an SQL query to recommend friends to Leetcodify users. We recommend user x to user y if:

Users x and y are not friends, and
Users x and y listened to the same three or more different songs on the same day.
Note that friend recommendations are unidirectional, meaning if user x and user y should be recommended to each other, the result table should have both user x recommended to user y and user y recommended to user x. Also, note that the result table should not contain duplicates (i.e., user y should not be recommended to user x multiple times.).

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Listens table:
+---------+---------+------------+
| user_id | song_id | day        |
+---------+---------+------------+
| 1       | 10      | 2021-03-15 |
| 1       | 11      | 2021-03-15 |
| 1       | 12      | 2021-03-15 |
| 2       | 10      | 2021-03-15 |
| 2       | 11      | 2021-03-15 |
| 2       | 12      | 2021-03-15 |
| 3       | 10      | 2021-03-15 |
| 3       | 11      | 2021-03-15 |
| 3       | 12      | 2021-03-15 |
| 4       | 10      | 2021-03-15 |
| 4       | 11      | 2021-03-15 |
| 4       | 13      | 2021-03-15 |
| 5       | 10      | 2021-03-16 |
| 5       | 11      | 2021-03-16 |
| 5       | 12      | 2021-03-16 |
+---------+---------+------------+
Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
+----------+----------+
Output:
+---------+----------------+
| user_id | recommended_id |
+---------+----------------+
| 1       | 3              |
| 2       | 3              |
| 3       | 1              |
| 3       | 2              |
+---------+----------------+
Explanation:
Users 1 and 2 listened to songs 10, 11, and 12 on the same day, but they are already friends.
Users 1 and 3 listened to songs 10, 11, and 12 on the same day. Since they are not friends, we recommend them to each other.
Users 1 and 4 did not listen to the same three songs.
Users 1 and 5 listened to songs 10, 11, and 12, but on different days.

Similarly, we can see that users 2 and 3 listened to songs 10, 11, and 12 on the same day and are not friends, so we recommend them to each other.
*/
with T as(
select distinct
    L1.user_id u1
    , L2.user_id u2
from Listens L1
    inner join Listens L2
        on L1.song_id = L2.song_id
        and L1.day = L2.day
        and L1.user_id < L2.user_id
-- WHERE (L1.user_id, L2.user_id) NOT IN (SELECT * FROM Friendship) -- slow as a dog
WHERE NOT EXISTS(SELECT * FROM Friendship f WHERE L1.user_id = f.user1_id AND L2.user_id = f.user2_id) -- fast like a bunny
group by L1.user_id, L2.user_id, L1.day
having count(distinct L1.song_id) >= 3
)
select u1 user_id, u2 recommended_id from T
    union
select u2, u1 from T


1919. Leetcodify Similar Friends (Hard)
-- https://leetcode.com/problems/leetcodify-similar-friends

/*
1934. Confirmation Rate (Medium)
-- https://leetcode.com/problems/confirmation-rate
The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write an SQL query to find the confirmation rate of each user.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
Output:
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
Explanation:
User 6 did not request any confirmation messages. The confirmation rate is 0.
User 3 made 2 requests and both timed out. The confirmation rate is 0.
User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.
*/
with all_users as (
    select
      user_id
    from Signups
    union
    select
      user_id
    from Confirmations
  ),
  confired_requests as (
    select
      user_id,
      count(action) as confirm
    from Confirmations c
    where c.action = 'confirmed'
    group by user_id
  ),
  total_requests as (
    select
      user_id,
      count(action) as total
    from Confirmations
    group by user_id
  )
select
  a.user_id,
  -- c.confirm,
  -- t.total,
  case
    when c.confirm is null then round(0/1, 2)
    else round((c.confirm / t.total)/1, 2)
  end as confirmation_rate
from all_users a
  left join confired_requests c on a.user_id = c.user_id
  left join total_requests t on a.user_id = t.user_id;

/*
1939. Users That Actively Request Confirmation Messages (Easy)
-- https://leetcode.com/problems/users-that-actively-request-confirmation-messages
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the primary key for this table.
Each row contains information about the signup time for the user with ID user_id.

Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key for this table.
user_id is a foreign key with a reference to the Signups table.
action is an ENUM of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').


Write an SQL query to find the IDs of the users that requested a confirmation message twice within a 24-hour window. Two messages exactly 24 hours apart are considered to be within the window. The action does not affect the answer, only the request time.

Return the result table in any order.

The query result format is in the following example.

Input:
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-01-06 03:37:45 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 11:57:30 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-01-23 00:00:00 | timeout   |
| 6       | 2021-10-23 14:14:14 | confirmed |
| 6       | 2021-10-24 14:14:13 | timeout   |
+---------+---------------------+-----------+
Output:
+---------+
| user_id |
+---------+
| 2       |
| 3       |
| 6       |
+---------+
Explanation:
User 2 requested two messages within exactly 24 hours of each other, so we include them.
User 3 requested two messages within 6 minutes and 59 seconds of each other, so we
include them.
User 6 requested two messages within 23 hours, 59 minutes, and 59 seconds of each other,
so we include them.
User 7 requested two messages within 24 hours and 1 second of each other, so we exclude
them from the answer.
*/
select distinct C1.user_id
from Confirmations C1
    inner join Confirmations C2
        on C1.user_id = C2.user_id
            and C1.time_stamp < C2.time_stamp
where timestampdiff(second, C1.time_stamp, C2.time_stamp) <= 24*60*60
order by C1.user_id


SELECT DISTINCT C1.user_id
FROM Confirmations C1
    INNER JOIN Confirmations C2
        ON C1.user_id = C2.user_id
            AND C1.time_stamp < C2.time_stamp
WHERE (C2.time_stamp BETWEEN C1.time_stamp AND ADDDATE(C1.time_stamp, INTERVAL 24 HOUR))


/*
1949. Strong Friendship (Medium)
-- https://leetcode.com/problems/strong-friendship
A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

Write an SQL query to find all the strong friendships.

Note that the result table should not contain duplicates with user1_id < user2_id.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
| 1        | 3        |
| 2        | 3        |
| 1        | 4        |
| 2        | 4        |
| 1        | 5        |
| 2        | 5        |
| 1        | 7        |
| 3        | 7        |
| 1        | 6        |
| 3        | 6        |
| 2        | 6        |
+----------+----------+
Output:
+----------+----------+---------------+
| user1_id | user2_id | common_friend |
+----------+----------+---------------+
| 1        | 2        | 4             |
| 1        | 3        | 3             |
+----------+----------+---------------+
Explanation:
Users 1 and 2 have 4 common friends (3, 4, 5, and 6).
Users 1 and 3 have 3 common friends (2, 6, and 7).
We did not include the friendship of users 2 and 3 because they only have two common friends (1 and 6).
*/
with T as (
    select
        user1_id 'user'
        , user2_id 'fid'
    from Friendship
    union -- sauce, when col1: a->b col2: b<-a, union to make it all a->b
    select
        user2_id 'user'
        , user1_id 'fid'
    from Friendship
)
select
    F.user1_id
    , F.user2_id
    , count(*) 'common_friend'
from Friendship F, T T1, T T2
    where F.user1_id = T1.user
        and F.user2_id = T2.user
        and T1.fid = T2.fid -- checks common friends
group by F.user1_id, F.user2_id
having count(*) >=3

/*
1951. All the Pairs With the Maximum Number of Common Followers (Medium)
-- https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers
Write an SQL query to find all the pairs of users with the maximum number of common followers. In other words, if the maximum number of common followers between any two users is maxCommon, then you have to return all pairs of users that have maxCommon common followers.

The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Relations table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 1       | 3           |
| 2       | 3           |
| 7       | 3           |
| 1       | 4           |
| 2       | 4           |
| 7       | 4           |
| 1       | 5           |
| 2       | 6           |
| 7       | 5           |
+---------+-------------+
Output:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 7        |
+----------+----------+
Explanation:
Users 1 and 2 have two common followers (3 and 4).
Users 1 and 7 have three common followers (3, 4, and 5).
Users 2 and 7 have two common followers (3 and 4).
Since the maximum number of common followers between any two users is 3, we return all pairs of users with three common followers, which is only the pair (1, 7). We return the pair as (1, 7), not as (7, 1).
Note that we do not have any information about the users that follow users 3, 4, and 5, so we consider them to have 0 followers.
*/

WITH cte AS (
SELECT r1.user_id user1_id
    , r2.user_id user2_id
FROM relations r1
    INNER JOIN relations r2
        ON r1.user_id < r2.user_id
WHERE r1.follower_id = r2.follower_id
)
SELECT *
FROM cte
GROUP BY 1, 2
HAVING COUNT(*) = (
    SELECT MAX(_max)
    FROM (SELECT COUNT(*) _max FROM cte GROUP BY user1_id, user2_id) t
);

/*
1965. Employees With Missing Information (Easy)
-- https://leetcode.com/problems/employees-with-missing-information
Write an SQL query to report the IDs of all the employees with missing information.
The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

The query result format is in the following example.

Input:
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+
Output:
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+
Explanation:
Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.
*/
-- TODO this is symmetric difference on one column
-- there HAS to be a better way, maybe not in MySQL
with T as (
select distinct employee_id
from Employees

union all

select distinct employee_id
from Salaries
)
select employee_id
from T
group by employee_id
having count(employee_id) < 2
order by employee_id


/*
1972. First and Last Call On the Same Day (Hard)
-- https://leetcode.com/problems/first-and-last-call-on-the-same-day
Write an SQL query to report the IDs of the users whose first and last calls on any day were with the same person. Calls are counted regardless of being the caller or the recipient.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Calls table:
+-----------+--------------+---------------------+
| caller_id | recipient_id | call_time           |
+-----------+--------------+---------------------+
| 8         | 4            | 2021-08-24 17:46:07 |
| 4         | 8            | 2021-08-24 19:57:13 |
| 5         | 1            | 2021-08-11 05:28:44 |
| 8         | 3            | 2021-08-17 04:04:15 |
| 11        | 3            | 2021-08-17 13:07:00 |
| 8         | 11           | 2021-08-17 22:22:22 |
+-----------+--------------+---------------------+
Output:
+---------+
| user_id |
+---------+
| 1       |
| 4       |
| 5       |
| 8       |
+---------+
Explanation:
On 2021-08-24, the first and last call of this day for user 8 was with user 4. User 8 should be included in the answer.
Similarly, user 4 on 2021-08-24 had their first and last call with user 8. User 4 should be included in the answer.
On 2021-08-11, user 1 and 5 had a call. This call was the only call for both of them on this day. Since this call is the first and last call of the day for both of them, they should both be included in the answer.
*/
with all_calls as (
select caller_id, recipient_id, call_time from Calls
union
select recipient_id, caller_id, call_time from Calls
), user_call as (
select caller_id user_id
	, date(call_time) call_date
	, min(call_time) first_call
	, max(call_time) last_call
from all_calls
group by 1, 2
)
select distinct uc.user_id
from user_call uc
	inner join all_calls ac
		on (ac.caller_id = uc.user_id and (ac.call_time = first_call or ac.call_time = last_call))
group by uc.user_id, uc.first_call, uc.last_call
having count(distinct recipient_id) = 1

/*
1978. Employees Whose Manager Left the Company Easy
-- https://leetcode.com/problemsemployees-whose-manager-left-the-company
Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.

The query result format is in the following example.

Input:
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
Output:
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

Explanation:
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel's manager is employee 11, who is still in the company (Joziah).
Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
*/
select employee_id
from Employees
where salary < 30000
    and manager_id not in (select distinct employee_id from Employees)
order by employee_id

/*
1988. Find Cutoff Score for Each School Medium
-- https://leetcode.com/problems/find-cutoff-score-for-each-school/
Every year, each school announces a minimum score requirement that a student needs to apply to it. The school chooses the minimum score requirement based on the exam results of all the students:
    - They want to ensure that even if every student meeting the requirement applies, the school can accept everyone.
    - They also want to maximize the possible number of students that can apply.
    - They must use a score that is in the Exam table.

Write an SQL query to report the minimum score requirement for each school. If there are multiple score values satisfying the above conditions, choose the smallest one. If the input data is not enough to determine the score, report -1.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Schools table:
+-----------+----------+
| school_id | capacity |
+-----------+----------+
| 11        | 151      |
| 5         | 48       |
| 9         | 9        |
| 10        | 99       |
+-----------+----------+
Exam table:
+-------+---------------+
| score | student_count |
+-------+---------------+
| 975   | 10            |
| 966   | 60            |
| 844   | 76            |
| 749   | 76            |
| 744   | 100           |
+-------+---------------+
Output:
+-----------+-------+
| school_id | score |
+-----------+-------+
| 5         | 975   |
| 9         | -1    |
| 10        | 749   |
| 11        | 744   |
+-----------+-------+
Explanation:
- School 5: The school's capacity is 48. Choosing 975 as the min score requirement, the school will get at most 10 applications, which is within capacity.
- School 10: The school's capacity is 99. Choosing 844 or 749 as the min score requirement, the school will get at most 76 applications, which is within capacity. We choose the smallest of them, which is 749.
- School 11: The school's capacity is 151. Choosing 744 as the min score requirement, the school will get at most 100 applications, which is within capacity.
- School 9: The data given is not enough to determine the min score requirement. Choosing 975 as the min score, the school may get 10 requests while its capacity is 9. We do not have information about higher scores, hence we report -1.
*/

select school_id
    , ifnull(min(score), -1) score
from Schools
    left join Exam
        on capacity >= student_count
group by school_id

1990. Count the Number of Experiments Medium
/*
2004. The Number of Seniors and Juniors to Join the Company Hard
-- https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/
A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Hiring the largest number of seniors.
After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 20000  |
| 11          | Senior     | 20000  |
| 13          | Senior     | 50000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output:
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 2                   |
| Junior     | 2                   |
+------------+---------------------+
Explanation:
We can hire 2 seniors with IDs (2, 11). Since the budget is $70000 and the sum of their salaries is $40000, we still have $30000 but they are not enough to hire the senior candidate with ID 13.
We can hire 2 juniors with IDs (1, 9). Since the remaining budget is $30000 and the sum of their salaries is $20000, we still have $10000 but they are not enough to hire the junior candidate with ID 4.

Example 2:

Input:
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 80000  |
| 11          | Senior     | 80000  |
| 13          | Senior     | 80000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output:
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 0                   |
| Junior     | 3                   |
+------------+---------------------+
Explanation:
We cannot hire any seniors with the current budget as we need at least $80000 to hire one senior.
We can hire all three juniors with the remaining budget.

NOTE experience is an enum with one of the values ('Senior', 'Junior').
*/
WITH CTE AS (
SELECT employee_id
	, experience
	, SUM(salary) OVER(PARTITION BY experience ORDER BY salary, employee_id ASC) rn
FROM Candidates
)
SELECT 'Senior' experience
	, COUNT(employee_id) accepted_candidates
FROM CTE
WHERE experience = 'Senior'
	AND rn <= 70000

UNION

SELECT 'Junior' experience
	, COUNT(employee_id) accepted_candidates
FROM CTE
WHERE experience = 'Junior'
	AND rn <= (
SELECT 70000 - IFNULL(MAX(rn), 0)
FROM CTE
WHERE experience = 'Senior'
	AND rn <= 70000
);

2010. The Number of Seniors and Juniors to Join the Company II Hard

/*
2020. Number of Accounts That Did Not Stream Medium
Write an SQL query to report the number of accounts that bought a subscription in 2021 but did not have any stream session.

The query result format is in the following example.

Example 1:

Input:
Subscriptions table:
+------------+------------+------------+
| account_id | start_date | end_date   |
+------------+------------+------------+
| 9          | 2020-02-18 | 2021-10-30 |
| 3          | 2021-09-21 | 2021-11-13 |
| 11         | 2020-02-28 | 2020-08-18 |
| 13         | 2021-04-20 | 2021-09-22 |
| 4          | 2020-10-26 | 2021-05-08 |
| 5          | 2020-09-11 | 2021-01-17 |
+------------+------------+------------+
Streams table:
+------------+------------+-------------+
| session_id | account_id | stream_date |
+------------+------------+-------------+
| 14         | 9          | 2020-05-16  |
| 16         | 3          | 2021-10-27  |
| 18         | 11         | 2020-04-29  |
| 17         | 13         | 2021-08-08  |
| 19         | 4          | 2020-12-31  |
| 13         | 5          | 2021-01-05  |
+------------+------------+-------------+
Output:
+----------------+
| accounts_count |
+----------------+
| 2              |
+----------------+
Explanation: Users 4 and 9 did not stream in 2021.
User 11 did not subscribe in 2021.
*/
SELECT COUNT(account_id) accounts_count
FROM Subscriptions
WHERE YEAR(start_date) <= 2021 AND YEAR(end_date) >= 2021
	AND account_id NOT IN (SELECT account_id FROM Streams WHERE YEAR(stream_date) = 2021)

/*
2026. Low-Quality Problems Easy
Write an SQL query to report the IDs of the low-quality problems. A LeetCode problem is low-quality if the like percentage of the problem (number of likes divided by the total number of votes) is strictly less than 60%.

Return the result table ordered by problem_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Problems table:
+------------+-------+----------+
| problem_id | likes | dislikes |
+------------+-------+----------+
| 6          | 1290  | 425      |
| 11         | 2677  | 8659     |
| 1          | 4446  | 2760     |
| 7          | 8569  | 6086     |
| 13         | 2050  | 4164     |
| 10         | 9002  | 7446     |
+------------+-------+----------+
Output:
+------------+
| problem_id |
+------------+
| 7          |
| 10         |
| 11         |
| 13         |
+------------+
Explanation: The like percentages are as follows:
- Problem 1: (4446 / (4446 + 2760)) * 100 = 61.69858%
- Problem 6: (1290 / (1290 + 425)) * 100 = 75.21866%
- Problem 7: (8569 / (8569 + 6086)) * 100 = 58.47151%
- Problem 10: (9002 / (9002 + 7446)) * 100 = 54.73006%
- Problem 11: (2677 / (2677 + 8659)) * 100 = 23.61503%
- Problem 13: (2050 / (2050 + 4164)) * 100 = 32.99002%
Problems 7, 10, 11, and 13 are low-quality problems because their like percentages are less than 60%.
*/
select problem_id
from Problems
where (likes / (likes + dislikes)) * 100 < 60
order by problem_id


2041. Accepted Candidates From the Interviews Medium
2051. The Category of Each Member in the Store Medium
/*
2066. Account Balance Medium
-- https://leetcode.com/problems/account-balance/
Write an SQL query to report the balance of each user after each transaction. You may assume that the balance of each account before any transaction is 0 and that the balance will never be below 0 at any moment.

Return the result table in ascending order by account_id, then by day in case of a tie.

The query result format is in the following example.

Example 1:

Input:
Transactions table:
+------------+------------+----------+--------+
| account_id | day        | type     | amount |
+------------+------------+----------+--------+
| 1          | 2021-11-07 | Deposit  | 2000   |
| 1          | 2021-11-09 | Withdraw | 1000   |
| 1          | 2021-11-11 | Deposit  | 3000   |
| 2          | 2021-12-07 | Deposit  | 7000   |
| 2          | 2021-12-12 | Withdraw | 7000   |
+------------+------------+----------+--------+
Output:
+------------+------------+---------+
| account_id | day        | balance |
+------------+------------+---------+
| 1          | 2021-11-07 | 2000    |
| 1          | 2021-11-09 | 1000    |
| 1          | 2021-11-11 | 4000    |
| 2          | 2021-12-07 | 7000    |
| 2          | 2021-12-12 | 0       |
+------------+------------+---------+
Explanation:
Account 1:
- Initial balance is 0.
- 2021-11-07 --> deposit 2000. Balance is 0 + 2000 = 2000.
- 2021-11-09 --> withdraw 1000. Balance is 2000 - 1000 = 1000.
- 2021-11-11 --> deposit 3000. Balance is 1000 + 3000 = 4000.
Account 2:
- Initial balance is 0.
- 2021-12-07 --> deposit 7000. Balance is 0 + 7000 = 7000.
- 2021-12-12 --> withdraw 7000. Balance is 7000 - 7000 = 0.
*/

SELECT account_id
    , day
    , sum(IF(type = 'Deposit', amount, -amount)) OVER(PARTITION BY account_id ORDER BY account_id ASC, day ASC) balance
FROM transactions;


/*
2072. The Winner University Easy
There is a competition between New York University and California University. The competition is held between the same number of students from both universities. The university that has more excellent students wins the competition. If the two universities have the same number of excellent students, the competition ends in a draw.

An excellent student is a student that scored 90% or more in the exam.

Write an SQL query to report:

"New York University" if New York University wins the competition.
"California University" if California University wins the competition.
"No Winner" if the competition ends in a draw.
The query result format is in the following example.

Example 1:
Input:
NewYork table:
+------------+-------+
| student_id | score |
+------------+-------+
| 1          | 90    |
| 2          | 87    |
+------------+-------+
California table:
+------------+-------+
| student_id | score |
+------------+-------+
| 2          | 89    |
| 3          | 88    |
+------------+-------+
Output:
+---------------------+
| winner              |
+---------------------+
| New York University |
+---------------------+
Explanation:
New York University has 1 excellent student, and California University has 0 excellent students.

Example 2:
Input:
NewYork table:
+------------+-------+
| student_id | score |
+------------+-------+
| 1          | 89    |
| 2          | 88    |
+------------+-------+
California table:
+------------+-------+
| student_id | score |
+------------+-------+
| 2          | 90    |
| 3          | 87    |
+------------+-------+
Output:
+-----------------------+
| winner                |
+-----------------------+
| California University |
+-----------------------+
Explanation:
New York University has 0 excellent students, and California University has 1 excellent student.

Example 3:
Input:
NewYork table:
+------------+-------+
| student_id | score |
+------------+-------+
| 1          | 89    |
| 2          | 90    |
+------------+-------+
California table:
+------------+-------+
| student_id | score |
+------------+-------+
| 2          | 87    |
| 3          | 99    |
+------------+-------+
Output:
+-----------+
| winner    |
+-----------+
| No Winner |
+-----------+
Explanation:
Both New York University and California University have 1 excellent student.
*/
with T as (
select count(*)
from NewYork
where score >= 90
) , U as (
select count(*)
from California
where score >= 90
)
select
    case
        when (select * from T) > (select * from U) then 'New York University'
        when (select * from T) < (select * from U) then 'California University'
        else 'No Winner'
    end winner

/*
2082. The Number of Rich Customers Easy
Write an SQL query to report the number of customers who had at least one bill with an amount strictly greater than 500.

The query result format is in the following example.

Example 1:
Input:
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
Output:
+------------+
| rich_count |
+------------+
| 2          |
+------------+
Explanation:
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.
*/
select count(distinct customer_id) rich_count
from Store
where amount > 500


2084. Drop Type 1 Orders for Customers With Type 0 Orders Medium

/*
2142. The Number of Passengers in Each Bus I Medium
-- https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/
Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at time `tbus` and a passenger arrived at time `tpassenger` where `tpassenger <= tbus` and the passenger did not catch any bus, the passenger will use that bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by `bus_id` in ascending order.

The query result format is in the following example.

Example 1:

Input:
Buses table:
+--------+--------------+
| bus_id | arrival_time |
+--------+--------------+
| 1      | 2            |
| 2      | 4            |
| 3      | 7            |
+--------+--------------+
Passengers table:
+--------------+--------------+
| passenger_id | arrival_time |
+--------------+--------------+
| 11           | 1            |
| 12           | 5            |
| 13           | 6            |
| 14           | 7            |
+--------------+--------------+
Output:
+--------+----------------+
| bus_id | passengers_cnt |
+--------+----------------+
| 1      | 1              |
| 2      | 0              |
| 3      | 3              |
+--------+----------------+
Explanation:
- Passenger 11 arrives at time 1.
- Bus 1 arrives at time 2 and collects passenger 11.

- Bus 2 arrives at time 4 and does not collect any passengers.

- Passenger 12 arrives at time 5.
- Passenger 13 arrives at time 6.
- Passenger 14 arrives at time 7.
- Bus 3 arrives at time 7 and collects passengers 12, 13, and 14.
*/

WITH cte AS (
SELECT bus_id
	, arrival_time
	, LAG(arrival_time, 1, 0) OVER (ORDER BY arrival_time) min_time
FROM buses
)
SELECT cte.bus_id
	, COUNT(passenger_id) passengers_cnt
FROM cte
	LEFT JOIN Passengers p
		ON p.arrival_time > cte.min_time
		AND p.arrival_time <= cte.arrival_time
GROUP BY bus_id
ORDER BY bus_id;


/*
2159. Order Two Columns Independently
-- https://leetcode.com/problems/order-two-columns-independently/
Write an SQL query to independently:
    order first_col in ascending order.
    order second_col in descending order.
The query result format is in the following example.

Example 1:

Input:
Data table:
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 4         | 2          |
| 2         | 3          |
| 3         | 1          |
| 1         | 4          |
+-----------+------------+
Output:
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 1         | 4          |
| 2         | 3          |
| 3         | 2          |
| 4         | 1          |
+-----------+------------+
*/

SELECT first_col, second_col
FROM
    (SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS r
    FROM Data) a
    INNER JOIN
    (SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS r
    FROM Data) b
        ON a.r = b.r

/*
2205. The Number of Users That Are Eligible for Discount
-- https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/
A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate] with at least minAmount amount. To convert the dates to times, both dates should be considered as the start of the day (i.e., endDate = 2022-03-05 should be considered as the time 2022-03-05 00:00:00).

Write an SQL query to report the number of users that are eligible for a discount.

The query result format is in the following example.

Example 1:

Input:
Purchases table:
+---------+---------------------+--------+
| user_id | time_stamp          | amount |
+---------+---------------------+--------+
| 1       | 2022-04-20 09:03:00 | 4416   |
| 2       | 2022-03-19 19:24:02 | 678    |
| 3       | 2022-03-18 12:03:09 | 4523   |
| 3       | 2022-03-30 09:43:42 | 626    |
+---------+---------------------+--------+
startDate = 2022-03-08, endDate = 2022-03-20, minAmount = 1000
Output:
+----------+
| user_cnt |
+----------+
| 1        |
+----------+
Explanation:
Out of the three users, only User 3 is eligible for a discount.
 - User 1 had one purchase with at least minAmount amount, but not within the time interval.
 - User 2 had one purchase within the time interval, but with less than minAmount amount.
 - User 3 is the only user who had a purchase that satisfies both conditions.
*/

CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) user_cnt
    FROM Purchases
    WHERE amount >= minAmount
        AND time_stamp BETWEEN startDate AND endDate
    );
END

/*
2230. The Users That Are Eligible for Discount
-- https://leetcode.com/problems/the-users-that-are-eligible-for-discount/
A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate] with at least minAmount amount. To convert the dates to times, both dates should be considered as the start of the day (i.e., endDate = 2022-03-05 should be considered as the time 2022-03-05 00:00:00).

Write an SQL query to report the IDs of the users that are eligible for a discount.

Return the result table ordered by user_id.

The query result format is in the following example.

Example 1:

Input:
Purchases table:
+---------+---------------------+--------+
| user_id | time_stamp          | amount |
+---------+---------------------+--------+
| 1       | 2022-04-20 09:03:00 | 4416   |
| 2       | 2022-03-19 19:24:02 | 678    |
| 3       | 2022-03-18 12:03:09 | 4523   |
| 3       | 2022-03-30 09:43:42 | 626    |
+---------+---------------------+--------+
startDate = 2022-03-08, endDate = 2022-03-20, minAmount = 1000
Output:
+---------+
| user_id |
+---------+
| 3       |
+---------+
Explanation:
Out of the three users, only User 3 is eligible for a discount.
 - User 1 had one purchase with at least minAmount amount, but not within the time interval.
 - User 2 had one purchase within the time interval, but with less than minAmount amount.
 - User 3 is the only user who had a purchase that satisfies both conditions.


Important Note: This problem is basically the same as The Number of Users That Are Eligible for Discount.
*/

CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN (
    SELECT DISTINCT user_id
    FROM Purchases
    WHERE amount >= minAmount
        AND time_stamp BETWEEN startDate AND endDate
    ORDER BY user_id
    );
END

/*
2329. Product Sales Analysis V
-- https://leetcode.com/problems/product-sales-analysis-v/
Write an SQL query that reports the spending of each user.

Return the resulting table ordered by spending in descending order. In case of a tie, order them by user_id in ascending order.

The query result format is in the following example.

Example 1:

Input:
Sales table:
+---------+------------+---------+----------+
| sale_id | product_id | user_id | quantity |
+---------+------------+---------+----------+
| 1       | 1          | 101     | 10       |
| 2       | 2          | 101     | 1        |
| 3       | 3          | 102     | 3        |
| 4       | 3          | 102     | 2        |
| 5       | 2          | 103     | 3        |
+---------+------------+---------+----------+
Product table:
+------------+-------+
| product_id | price |
+------------+-------+
| 1          | 10    |
| 2          | 25    |
| 3          | 15    |
+------------+-------+
Output:
+---------+----------+
| user_id | spending |
+---------+----------+
| 101     | 125      |
| 102     | 75       |
| 103     | 75       |
+---------+----------+
Explanation:
User 101 spent 10 * 10 + 1 * 25 = 125.
User 102 spent 3 * 15 + 2 * 15 = 75.
User 103 spent 3 * 25 = 75.
Users 102 and 103 spent the same amount and we break the tie by their ID while user 101 is on the top.
*/

SELECT s.user_id
    , SUM(s.quantity * p.price) spending
FROM Sales s
    INNER JOIN Product p
        USING (product_id)
GROUP BY s.user_id
ORDER BY 2 DESC, 1 ASC

/*
2339. All the Matches of the League
-- https://leetcode.com/problems/all-the-matches-of-the-league/
Write an SQL query that reports all the possible matches of the league. Note that every two teams play two matches with each other, with one team being the home_team once and the other time being the away_team.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Teams table:
+-------------+
| team_name   |
+-------------+
| Leetcode FC |
| Ahly SC     |
| Real Madrid |
+-------------+
Output:
+-------------+-------------+
| home_team   | away_team   |
+-------------+-------------+
| Real Madrid | Leetcode FC |
| Real Madrid | Ahly SC     |
| Leetcode FC | Real Madrid |
| Leetcode FC | Ahly SC     |
| Ahly SC     | Real Madrid |
| Ahly SC     | Leetcode FC |
+-------------+-------------+
Explanation: All the matches of the league are shown in the table.
*/

-- NOTE Teams t1, Teams t2 ON t1.team_name <> t2.team_name; IS NOT VALID MySQL!

SELECT t1.team_name home_team
    , t2.team_name away_team
FROM Teams t1
    CROSS JOIN Teams t2
        ON t1.team_name <> t2.team_name;

/*
2356. Number of Unique Subjects Taught by Each Teacher
-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
Write an SQL query to report the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

The query result format is shown in the following example.

Example 1:

Input:
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation:
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
*/

SELECT teacher_id
    , COUNT(DISTINCT subject_id) cnt
FROM Teacher
GROUP BY teacher_id;

/*
2377. Sort the Olympic Table
-- https://leetcode.com/problems/sort-the-olympic-table/
The Olympic table is sorted according to the following rules:
    The country with more gold medals comes first.
    If there is a tie in the gold medals, the country with more silver medals comes first.
    If there is a tie in the silver medals, the country with more bronze medals comes first.
    If there is a tie in the bronze medals, the countries with the tie are sorted in ascending order lexicographically.
    Write an SQL query to sort the Olympic table

The query result format is shown in the following example.

Example 1:

Input:
Olympic table:
+-------------+-------------+---------------+---------------+
| country     | gold_medals | silver_medals | bronze_medals |
+-------------+-------------+---------------+---------------+
| China       | 10          | 10            | 20            |
| South Sudan | 0           | 0             | 1             |
| USA         | 10          | 10            | 20            |
| Israel      | 2           | 2             | 3             |
| Egypt       | 2           | 2             | 2             |
+-------------+-------------+---------------+---------------+
Output:
+-------------+-------------+---------------+---------------+
| country     | gold_medals | silver_medals | bronze_medals |
+-------------+-------------+---------------+---------------+
| China       | 10          | 10            | 20            |
| USA         | 10          | 10            | 20            |
| Israel      | 2           | 2             | 3             |
| Egypt       | 2           | 2             | 2             |
| South Sudan | 0           | 0             | 1             |
+-------------+-------------+---------------+---------------+
Explanation:
The tie between China and USA is broken by their lexicographical names. Since "China" is lexicographically smaller than "USA", it comes first.
Israel comes before Egypt because it has more bronze medals.
*/

SELECT country
    , gold_medals
    , silver_medals
    , bronze_medals
FROM Olympic
ORDER BY gold_medals DESC, silver_medals DESC, bronze_medals DESC, country
