-- 오랜 기간 보호한 동물(2)
-- 코드를 입력하세요
SELECT ins.animal_id, ins.name
from animal_ins as ins
inner join animal_outs as outs
on ins.animal_id = outs.animal_id
order by outs.datetime - ins.datetime desc
-- datediff를 통해서도 두 날짜 사이의 기간을 알 수 있다!
-- order by datediff(outs.datetime, ins.datetime) desc 
limit 2