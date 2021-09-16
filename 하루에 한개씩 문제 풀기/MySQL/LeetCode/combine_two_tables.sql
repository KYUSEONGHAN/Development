-- leetcode, combine two tables, mysql
SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person as P
LEFT OUTER JOIN Address as A ON P.PersonId = A.PersonId