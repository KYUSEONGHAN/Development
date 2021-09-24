-- leetcode, Not Boring Movies, mysql
SELECT *
FROM Cinema
WHERE id%2 = 1 AND description != 'boring'
ORDER BY rating DESC