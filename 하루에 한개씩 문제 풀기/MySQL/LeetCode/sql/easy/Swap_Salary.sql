-- leetcode, Swap Salary, mysql
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END