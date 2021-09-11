-- programmers, sql 고득점 kit : datetime에서 date로 형변환, mysql
SELECT ANIMAL_ID, NAME,
       DATE_FORMAT(DATETIME, '%Y-%m-%d') as '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID