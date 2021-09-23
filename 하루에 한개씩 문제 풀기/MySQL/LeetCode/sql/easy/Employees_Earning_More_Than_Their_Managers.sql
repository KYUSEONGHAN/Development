-- leetcode, Employees Earning More Than Their Managers, mysql
SELECT T1.Name AS Employee
FROM Employee AS T1, Employee AS T2
WHERE T1.Salary >= T2.Salary AND T1.ManagerId = T2.Id