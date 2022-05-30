-- 프로그래머스 SQL 없어진 기록 찾기

-- 나의 풀이
select outs.animal_id, outs.name
from animal_outs as outs
where outs.animal_id not in
(select outs.animal_id
from animal_outs as outs
inner join animal_ins as ins
on ins.animal_id = outs.animal_id)
order by outs.animal_id

-- 다른 사람 풀이
-- select outs.animal_id, outs.name
-- from animal_ins ins
-- right outer join animal_outs outs
-- on outs.animal_id = ins.animal_id
-- where ins.animal_id is null
-- order by outs.animal_id