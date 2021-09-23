-- leetcode, Customers Who Never Order, mysql

-- 서브쿼리를 이용한 풀이
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (SELECT CustomerId
                 FROM Orders)

-- 조인을 이용한 풀이
SELECT C.Name AS Customers
FROM Customers AS C
LEFT OUTER JOIN Orders AS O ON C.ID = O.CustomerId
WHERE O.Id IS NULL