-- programmers, sql 고득점 kit : 이름에 el이 들어가는 동물 찾기, mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'DOG' AND NAME LIKE '%EL%'
ORDER BY NAME