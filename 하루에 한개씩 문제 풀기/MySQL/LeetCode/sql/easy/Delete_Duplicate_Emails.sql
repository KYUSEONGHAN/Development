-- leetcode, Delete Duplicate Emails, mysql
DELETE T1
FROM Person T1, Person T2
WHERE T1.Email = T2.Email AND T1.Id > T2.Id