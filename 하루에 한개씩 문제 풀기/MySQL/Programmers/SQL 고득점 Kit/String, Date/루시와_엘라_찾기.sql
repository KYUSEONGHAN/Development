-- programmser, sql 고득점 kit : 루시와 엘라 찾기, mysql

-- (1) or 를 이용한 풀이
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = 'Lucy' or NAME = 'Ella' or NAME = 'Pickle' or NAME = 'Rogan' or NAME = 'Sabrina' or NAME = 'Mitty'

-- (2) in 를 이용한 풀이
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
