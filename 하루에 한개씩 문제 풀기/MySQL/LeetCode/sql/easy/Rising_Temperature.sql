-- leetcode, Rising Temperature, mysql
SELECT T1.Id AS id
FROM Weather AS T1, Weather AS T2
WHERE T1.Temperature > T2.Temperature AND TO_DAYS(T1.RecordDate) - TO_DAYS(T2.RecordDate) = 1