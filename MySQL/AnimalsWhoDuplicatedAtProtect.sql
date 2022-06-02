-- 보호소에서 중성화한 동물
-- 코드를 입력하세요
select ins.animal_id, ins.animal_type, ins.name
from animal_ins as ins
inner join animal_outs as outs
on ins.animal_id = outs.animal_id
where (ins.sex_upon_intake not like '%Spayed%' 
       and ins.sex_upon_intake not like '%Neutered%')
       and
       (outs.sex_upon_outcome like '%Spayed%'
       or outs.sex_upon_outcome like '%Neutered%')