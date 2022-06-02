-- 동명 동물 수 찾기
-- 코드를 입력하세요
SELECT name, count(name)
from animal_ins
group by name
having count(name) >= 2
order by name

-- INNER JOIN
SELECT A.* FROM PLACES A
JOIN (SELECT * FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2) B
ON A.HOST_ID = B.HOST_ID
ORDER BY A.ID;
-- SELF JOIN
SELECT A.*
FROM PLACES A, PLACES B
WHERE A.ID <> B.ID AND A.HOST_ID = B.HOST_ID
GROUP BY A.ID
ORDER BY A.ID;

-- subquery count로 받기
SELECT ID, NAME, HOST_ID
FROM PLACES A
WHERE (SELECT COUNT(HOST_ID) AS count
      FROM PLACES B
      WHERE A.HOST_ID=B.HOST_ID) >1;