-- 입양 시각 구하기(1)
-- 코드를 입력하세요
SELECT hour(datetime) as hour, count(hour(datetime)) as count
from animal_outs
where hour(datetime) >= 9 and hour(datetime) <= 19
group by hour
order by hour