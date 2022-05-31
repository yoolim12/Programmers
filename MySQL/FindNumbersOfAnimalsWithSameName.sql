-- 동명 동물 수 찾기
-- 코드를 입력하세요
SELECT name, count(name)
from animal_ins
group by name
having count(name) >= 2
order by name