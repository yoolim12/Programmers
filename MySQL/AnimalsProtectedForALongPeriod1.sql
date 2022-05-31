-- 오랜 기간 보호한 동물(1)
-- 코드를 입력하세요
select ins.name, ins.datetime
from animal_ins as ins
left join animal_outs as outs
on ins.animal_id = outs.animal_id
where outs.datetime is null
order by ins.datetime
limit 3