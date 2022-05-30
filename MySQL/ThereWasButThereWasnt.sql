-- 프로그래머스 SQL 있었는데요 없었습니다
select ins.animal_id, ins.name
from animal_ins as ins
join animal_outs as outs
on ins.animal_id = outs.animal_id
where ins.datetime > outs.datetime
order by ins.datetime