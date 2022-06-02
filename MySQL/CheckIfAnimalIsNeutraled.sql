-- 코드를 입력하세요
select animal_id, name, (case when sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%' then 'O' else 'X' end) as sex_upon_intake
from animal_ins
where sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%'
order by animal_id;

-- 주의!!
-- sex_upon_intake like '%Neutered%' or '%Spayed%'
-- 이렇게 작성하면 앞의 '%Neutered%'만 인식해서 sex_upon_intake like '%Neutered%'만 처리한다.