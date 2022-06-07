-- 상위 n개 레코드
-- 코드를 입력하세요
select name
from animal_ins
order by datetime
limit 1

-- 아래 풀이도 가능!
-- select name
-- from animal_ins
-- where datetime = (select min(datetime) from animal_ins)