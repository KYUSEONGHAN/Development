-- leetcode, Classes More Than 5 Students, mysql
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5